import { useEffect, useState, useCallback } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api } from '../api'
import { useLang } from '../LangContext'
import { speakDE } from '../speak'

function shuffle(arr) {
  const a = [...arr]
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]]
  }
  return a
}

// Tokenize sentence preserving punctuation attached to words
function tokenize(sentence) {
  return sentence.match(/\S+/g) || []
}

// Build questions from dialogue lines
function buildQuestions(dialogue) {
  const questions = []
  for (const [, line] of dialogue) {
    const tokens = tokenize(line)
    if (tokens.length < 3 || tokens.length > 10) continue  // 3–10 words ideal

    let scrambled = shuffle(tokens)
    // Ensure it's actually different from original
    let attempts = 0
    while (scrambled.join(' ') === line && attempts < 10) {
      scrambled = shuffle(tokens)
      attempts++
    }

    questions.push({
      original: line,
      tokens,
      scrambled: scrambled.map((word, i) => ({ word, id: i })),
    })
  }
  return shuffle(questions)
}

export default function OrderPage() {
  const { level, id } = useParams()
  const navigate = useNavigate()
  const { t, lang } = useLang()

  const [questions, setQuestions] = useState([])
  const [qIdx, setQIdx] = useState(0)
  const [pool, setPool] = useState([])      // remaining word chips { word, id, used }
  const [typed, setTyped] = useState([])    // assembled words { word, id }
  const [status, setStatus] = useState(null) // null | 'correct' | 'wrong'
  const [score, setScore] = useState(0)
  const [finished, setFinished] = useState(false)

  useEffect(() => {
    api.getLesson(level, parseInt(id)).then(lesson => {
      const dialogue = lesson.dialogue || []
      const qs = buildQuestions(dialogue)
      if (qs.length) {
        setQuestions(qs)
        loadQuestion(qs, 0)
      }
    })
    window.Telegram?.WebApp?.BackButton?.show()
    window.Telegram?.WebApp?.BackButton?.onClick(() => navigate(`/lesson/${level}/${id}`))
    return () => window.Telegram?.WebApp?.BackButton?.hide()
  }, [level, id])

  function loadQuestion(qs, idx) {
    const q = qs[idx % qs.length]
    setPool(q.scrambled.map(w => ({ ...w, used: false })))
    setTyped([])
    setStatus(null)
  }

  const handleWordTap = useCallback((chip) => {
    if (chip.used || status !== null) return
    const newTyped = [...typed, chip]
    setTyped(newTyped)
    setPool(prev => prev.map(w => w.id === chip.id ? { ...w, used: true } : w))

    const q = questions[qIdx % questions.length]
    // Check if all words placed
    if (newTyped.length === q.tokens.length) {
      const assembled = newTyped.map(w => w.word).join(' ')
      if (assembled === q.original) {
        setStatus('correct')
        setScore(s => s + 1)
        speakDE(q.original)
        setTimeout(() => {
          const nextIdx = qIdx + 1
          if (nextIdx >= questions.length) setFinished(true)
          else { setQIdx(nextIdx); loadQuestion(questions, nextIdx) }
        }, 1200)
      } else {
        setStatus('wrong')
        setTimeout(() => {
          // Reset this question
          loadQuestion(questions, qIdx)
        }, 900)
      }
    }
  }, [typed, status, questions, qIdx])

  const handleUndo = () => {
    if (!typed.length || status !== null) return
    const last = typed[typed.length - 1]
    setTyped(prev => prev.slice(0, -1))
    setPool(prev => prev.map(w => w.id === last.id ? { ...w, used: false } : w))
  }

  if (!questions.length) return (
    <div className="page" style={{ display:'flex', alignItems:'center', justifyContent:'center', minHeight:'60vh', flexDirection:'column', gap:12 }}>
      <div style={{ fontSize:48 }}>😕</div>
      <div style={{ color:'var(--tg-hint)', textAlign:'center' }}>
        {lang === 'uz' ? 'Bu darsda dialog topilmadi' : 'В этом уроке нет диалогов'}
      </div>
      <button className="btn btn-secondary" onClick={() => navigate(`/lesson/${level}/${id}`)}>
        {t.backToLessons}
      </button>
    </div>
  )

  if (finished) {
    const pct = Math.round((score / questions.length) * 100)
    return (
      <div className="page" style={{ display:'flex', flexDirection:'column', alignItems:'center', justifyContent:'center', minHeight:'85vh', textAlign:'center' }}>
        <div style={{ fontSize:72, marginBottom:16 }}>{pct >= 80 ? '🏆' : '💪'}</div>
        <h2 style={{ fontSize:22, fontWeight:800, marginBottom:4 }}>{t.result}</h2>
        <div style={{ fontSize:48, fontWeight:900, marginBottom:4,
          color: pct>=80?'var(--success)':pct>=50?'var(--warning)':'var(--danger)' }}>{pct}%</div>
        <div style={{ fontSize:16, color:'var(--tg-hint)', marginBottom:8 }}>{score} / {questions.length}</div>
        <div className="xp-chip" style={{ marginBottom:24 }}>⭐ +{score * 3} XP</div>
        <div style={{ display:'flex', flexDirection:'column', gap:10, width:'100%', maxWidth:300 }}>
          <button className="btn btn-primary" onClick={() => {
            setQIdx(0); setScore(0); setFinished(false); loadQuestion(questions, 0)
          }}>
            🔄 {t.tryAgain}
          </button>
          <button className="btn btn-secondary" onClick={() => navigate(`/lesson/${level}/${id}`)}>
            {t.backToLessons}
          </button>
        </div>
      </div>
    )
  }

  const q = questions[qIdx % questions.length]
  const progress = (qIdx / questions.length) * 100
  const isCorrect = status === 'correct'
  const isWrong = status === 'wrong'

  return (
    <div className="page">
      {/* Header */}
      <div style={{ display:'flex', alignItems:'center', justifyContent:'space-between', marginBottom:12 }}>
        <button className="back-btn" onClick={() => navigate(`/lesson/${level}/${id}`)}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="15 18 9 12 15 6"/>
          </svg>
        </button>
        <div style={{ fontWeight:700, fontSize:13, color:'var(--tg-hint)' }}>
          🔀 {qIdx+1}/{questions.length}
        </div>
        <div style={{ fontWeight:800, color:'var(--success)', fontSize:16 }}>✓ {score}</div>
      </div>

      <div className="progress-bar" style={{ marginBottom:24 }}>
        <div className="progress-bar-fill" style={{ width:`${progress}%` }} />
      </div>

      {/* Instruction */}
      <div style={{ fontSize:13, color:'var(--tg-hint)', textAlign:'center', marginBottom:16 }}>
        {lang === 'uz'
          ? "So'zlarni to'g'ri tartibda joylashtiring"
          : 'Расставьте слова в правильном порядке'}
      </div>

      {/* Answer area — where typed words appear */}
      <div style={{
        minHeight:80,
        border: `2px solid ${isCorrect ? 'rgba(34,197,94,.5)' : isWrong ? 'rgba(239,68,68,.5)' : 'rgba(255,255,255,.12)'}`,
        borderRadius:16,
        padding:'12px 14px',
        marginBottom:20,
        display:'flex',
        flexWrap:'wrap',
        gap:8,
        alignContent:'flex-start',
        background: isCorrect ? 'rgba(34,197,94,.07)' : isWrong ? 'rgba(239,68,68,.07)' : 'rgba(255,255,255,.03)',
        transition:'all .2s',
        animation: isWrong ? 'shake .5s ease' : undefined,
      }}>
        {typed.length === 0 && (
          <span style={{ color:'rgba(255,255,255,.2)', fontSize:14, alignSelf:'center' }}>
            {lang === 'uz' ? "So'zlarni bosing..." : 'Нажимайте слова...'}
          </span>
        )}
        {typed.map((chip, i) => (
          <span key={`typed-${chip.id}`} style={{
            background:'rgba(99,102,241,.2)',
            border:'1.5px solid rgba(99,102,241,.5)',
            borderRadius:10,
            padding:'6px 12px',
            fontSize:15,
            fontWeight:700,
            color: isCorrect ? 'var(--success)' : isWrong ? 'var(--danger)' : 'var(--accent)',
            transition:'color .2s',
          }}>
            {chip.word}
          </span>
        ))}
      </div>

      {/* Word pool */}
      <div style={{ display:'flex', flexWrap:'wrap', gap:8, marginBottom:20 }}>
        {pool.map(chip => (
          <button
            key={chip.id}
            onClick={() => handleWordTap(chip)}
            disabled={chip.used || status !== null}
            style={{
              padding:'8px 14px',
              borderRadius:12,
              border:'1.5px solid rgba(255,255,255,.15)',
              background: chip.used ? 'rgba(255,255,255,.02)' : 'rgba(255,255,255,.1)',
              color: chip.used ? 'rgba(255,255,255,.2)' : 'var(--tg-text)',
              fontWeight:700,
              fontSize:15,
              cursor: chip.used || status !== null ? 'default' : 'pointer',
              transition:'all .15s',
              transform: chip.used ? 'scale(.92)' : 'scale(1)',
            }}
          >
            {chip.word}
          </button>
        ))}
      </div>

      {/* Controls */}
      <div style={{ display:'flex', gap:10 }}>
        <button
          onClick={handleUndo}
          disabled={!typed.length || status !== null}
          style={{
            flex:1, padding:'12px', borderRadius:12,
            border:'1.5px solid rgba(255,255,255,.15)',
            background:'rgba(255,255,255,.06)',
            color: typed.length ? 'var(--tg-text)' : 'rgba(255,255,255,.2)',
            fontWeight:700, fontSize:14, cursor:'pointer',
          }}
        >
          ← {lang === 'uz' ? 'Orqaga' : 'Удалить'}
        </button>
        <button
          onClick={() => speakDE(q.original)}
          style={{
            flex:1, padding:'12px', borderRadius:12,
            border:'1.5px solid rgba(255,255,255,.1)',
            background:'transparent',
            color:'var(--tg-hint)',
            fontWeight:600, fontSize:14, cursor:'pointer',
          }}
        >
          🔊 {lang === 'uz' ? 'Eshitish' : 'Послушать'}
        </button>
      </div>

      {/* Feedback */}
      {status && (
        <div style={{
          marginTop:14, padding:'12px 16px', borderRadius:12,
          background: isCorrect ? 'var(--success-dim)' : 'var(--danger-dim)',
          color: isCorrect ? 'var(--success)' : 'var(--danger)',
          fontWeight:700, textAlign:'center', fontSize:15,
        }}>
          {isCorrect
            ? `✓ ${t.correct}`
            : `✗ ${lang === 'uz' ? "Noto'g'ri tartib" : 'Неверный порядок'}`}
        </div>
      )}
    </div>
  )
}
