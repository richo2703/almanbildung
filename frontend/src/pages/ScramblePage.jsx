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

// Scramble a word's letters (ensure different from original)
function scrambleWord(word) {
  const letters = word.toUpperCase().split('')
  let scrambled
  let attempts = 0
  do {
    scrambled = shuffle(letters)
    attempts++
  } while (scrambled.join('') === word.toUpperCase() && attempts < 20)
  return scrambled.map((char, i) => ({ char, id: i }))
}

// Strip German article for scrambling (keep article visible as hint)
function splitWord(de) {
  const match = de.match(/^(der|die|das|ein|eine)\s+(.+)$/i)
  if (match) return { article: match[1], base: match[2] }
  return { article: null, base: de }
}

export default function ScramblePage() {
  const { level, id } = useParams()
  const navigate = useNavigate()
  const { t, lang } = useLang()

  const [words, setWords] = useState([])
  const [wIdx, setWIdx] = useState(0)
  const [letters, setLetters] = useState([])    // scrambled pool { char, id, used }
  const [typed, setTyped] = useState([])         // tapped letters { char, id }
  const [status, setStatus] = useState(null)     // null | 'correct' | 'wrong'
  const [score, setScore] = useState(0)
  const [finished, setFinished] = useState(false)

  useEffect(() => {
    api.getLessonVocab(level, parseInt(id)).then(ws => {
      // Only use shorter words (≤12 chars base) for good UX
      const filtered = ws.filter(w => {
        const { base } = splitWord(w.de)
        return base.length >= 3 && base.length <= 12
      })
      setWords(shuffle(filtered.length >= 5 ? filtered : ws))
    })
    window.Telegram?.WebApp?.BackButton?.show()
    window.Telegram?.WebApp?.BackButton?.onClick(() => navigate(`/lesson/${level}/${id}`))
    return () => window.Telegram?.WebApp?.BackButton?.hide()
  }, [level, id])

  // Load current word
  useEffect(() => {
    if (!words.length) return
    const word = words[wIdx % words.length]
    const { base } = splitWord(word.de)
    setLetters(scrambleWord(base).map(l => ({ ...l, used: false })))
    setTyped([])
    setStatus(null)
  }, [wIdx, words])

  const handleLetterTap = useCallback((letter) => {
    if (status !== null || letter.used) return
    const newTyped = [...typed, letter]
    setTyped(newTyped)
    setLetters(prev => prev.map(l => l.id === letter.id ? { ...l, used: true } : l))

    const word = words[wIdx % words.length]
    const { base } = splitWord(word.de)
    const target = base.toUpperCase()
    const current = newTyped.map(l => l.char).join('')

    if (current.length === target.length) {
      if (current === target) {
        setStatus('correct')
        setScore(s => s + 1)
        speakDE(word.de)
        setTimeout(() => {
          if (wIdx + 1 >= words.length) setFinished(true)
          else setWIdx(i => i + 1)
        }, 1000)
      } else {
        setStatus('wrong')
        setTimeout(() => {
          // Reset
          const { base } = splitWord(word.de)
          setLetters(scrambleWord(base).map(l => ({ ...l, used: false })))
          setTyped([])
          setStatus(null)
        }, 800)
      }
    }
  }, [typed, status, words, wIdx])

  const handleUndo = () => {
    if (!typed.length || status !== null) return
    const last = typed[typed.length - 1]
    setTyped(prev => prev.slice(0, -1))
    setLetters(prev => prev.map(l => l.id === last.id ? { ...l, used: false } : l))
  }

  if (!words.length) return (
    <div className="loading"><div className="spinner" /></div>
  )

  if (finished) {
    const pct = Math.round((score / words.length) * 100)
    return (
      <div className="page" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '85vh', textAlign: 'center' }}>
        <div style={{ fontSize: 72, marginBottom: 16 }}>{pct >= 80 ? '🏆' : '💪'}</div>
        <h2 style={{ fontSize: 22, fontWeight: 800, marginBottom: 4 }}>{t.result}</h2>
        <div style={{ fontSize: 48, fontWeight: 900, color: pct >= 80 ? 'var(--success)' : 'var(--warning)', marginBottom: 8 }}>
          {pct}%
        </div>
        <div className="xp-chip" style={{ marginBottom: 24 }}>⭐ +{score * 3} XP</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 10, width: '100%', maxWidth: 300 }}>
          <button className="btn btn-primary" onClick={() => { setWIdx(0); setScore(0); setFinished(false) }}>
            🔄 {t.tryAgain}
          </button>
          <button className="btn btn-secondary" onClick={() => navigate(`/lesson/${level}/${id}`)}>
            {t.backToLessons}
          </button>
        </div>
      </div>
    )
  }

  const word = words[wIdx % words.length]
  const { article, base } = splitWord(word.de)
  const translation = lang === 'uz' ? (word.uz || word.ru) : word.ru
  const progress = (wIdx / words.length) * 100
  const typed_str = typed.map(l => l.char).join('')

  const isCorrect = status === 'correct'
  const isWrong = status === 'wrong'

  return (
    <div className="page">
      {/* Header */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 12 }}>
        <button className="back-btn" onClick={() => navigate(`/lesson/${level}/${id}`)}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="15 18 9 12 15 6"/>
          </svg>
        </button>
        <div style={{ fontWeight: 700, fontSize: 13, color: 'var(--tg-hint)' }}>
          🔤 {wIdx + 1}/{words.length}
        </div>
        <div style={{ fontWeight: 800, color: 'var(--success)', fontSize: 16 }}>✓ {score}</div>
      </div>

      <div className="progress-bar" style={{ marginBottom: 28 }}>
        <div className="progress-bar-fill" style={{ width: `${progress}%` }} />
      </div>

      {/* Hint: translation */}
      <div className="card" style={{ textAlign: 'center', padding: '20px 24px', marginBottom: 20 }}>
        <div style={{ fontSize: 12, color: 'var(--tg-hint)', marginBottom: 4, textTransform: 'uppercase', letterSpacing: 1 }}>
          {lang === 'uz' ? "Tarjima" : 'Перевод'}
        </div>
        <div style={{ fontSize: 22, fontWeight: 800 }}>{translation}</div>
        {article && (
          <div style={{ fontSize: 13, color: 'var(--tg-hint)', marginTop: 6 }}>
            {lang === 'uz' ? 'Artikl:' : 'Артикль:'} <strong style={{ color: 'var(--accent)' }}>{article}</strong>
          </div>
        )}
      </div>

      {/* Typed word display */}
      <div style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        gap: 6,
        minHeight: 60,
        marginBottom: 20,
        padding: '0 8px',
        flexWrap: 'wrap',
      }}>
        {base.split('').map((_, i) => {
          const typedChar = typed[i]?.char || ''
          const isEmpty = !typedChar
          return (
            <div key={i} style={{
              width: 38, height: 44,
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              borderBottom: `2.5px solid ${isCorrect ? 'var(--success)' : isWrong ? 'var(--danger)' : isEmpty ? 'rgba(255,255,255,.3)' : 'var(--accent)'}`,
              fontSize: 22, fontWeight: 800,
              color: isCorrect ? 'var(--success)' : isWrong ? 'var(--danger)' : 'var(--tg-text)',
              transition: 'all .2s',
              animation: isWrong ? 'shake .5s ease' : undefined,
            }}>
              {typedChar}
            </div>
          )
        })}
      </div>

      {/* Letter buttons */}
      <div style={{
        display: 'flex',
        flexWrap: 'wrap',
        gap: 8,
        justifyContent: 'center',
        marginBottom: 20,
      }}>
        {letters.map(letter => (
          <button
            key={letter.id}
            onClick={() => handleLetterTap(letter)}
            disabled={letter.used || status !== null}
            style={{
              width: 46, height: 46,
              borderRadius: 12,
              border: '1.5px solid rgba(255,255,255,.15)',
              background: letter.used ? 'rgba(255,255,255,.03)' : 'rgba(255,255,255,.1)',
              color: letter.used ? 'rgba(255,255,255,.2)' : 'var(--tg-text)',
              fontWeight: 800,
              fontSize: 18,
              cursor: letter.used || status !== null ? 'default' : 'pointer',
              transition: 'all .15s',
              transform: letter.used ? 'scale(.92)' : 'scale(1)',
            }}
          >
            {letter.char}
          </button>
        ))}
      </div>

      {/* Undo + hint */}
      <div style={{ display: 'flex', justifyContent: 'center', gap: 12 }}>
        <button
          onClick={handleUndo}
          disabled={!typed.length || status !== null}
          style={{
            padding: '10px 20px', borderRadius: 12,
            border: '1.5px solid rgba(255,255,255,.15)',
            background: 'rgba(255,255,255,.06)',
            color: typed.length ? 'var(--tg-text)' : 'rgba(255,255,255,.2)',
            fontWeight: 700, fontSize: 14, cursor: 'pointer',
          }}
        >
          ← {lang === 'uz' ? 'Orqaga' : 'Удалить'}
        </button>
        <button
          onClick={() => {
            // Show answer as hint
            const { base } = splitWord(word.de)
            setLetters(scrambleWord(base).map(l => ({ ...l, used: false })))
            setTyped([])
            setStatus(null)
            speakDE(word.de)
          }}
          style={{
            padding: '10px 20px', borderRadius: 12,
            border: '1.5px solid rgba(255,255,255,.1)',
            background: 'transparent',
            color: 'var(--tg-hint)',
            fontWeight: 600, fontSize: 14, cursor: 'pointer',
          }}
        >
          🔊 {lang === 'uz' ? 'Eshitish' : 'Послушать'}
        </button>
      </div>

      {/* Feedback */}
      {status && (
        <div style={{
          marginTop: 16, padding: '12px 16px', borderRadius: 12,
          background: isCorrect ? 'var(--success-dim)' : 'var(--danger-dim)',
          color: isCorrect ? 'var(--success)' : 'var(--danger)',
          fontWeight: 700, textAlign: 'center', fontSize: 15,
        }}>
          {isCorrect
            ? `✓ ${t.correct} — ${word.de}`
            : `✗ ${t.wrong}`}
        </div>
      )}
    </div>
  )
}
