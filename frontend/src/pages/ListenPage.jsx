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

function buildQuestion(word, allWords, lang) {
  const correct = lang === 'uz' ? (word.uz || word.ru) : word.ru
  // Pick 3 wrong options
  const others = shuffle(allWords.filter(w => w.de !== word.de))
    .slice(0, 3)
    .map(w => lang === 'uz' ? (w.uz || w.ru) : w.ru)
  const opts = shuffle([correct, ...others])
  return { word, correct, opts }
}

export default function ListenPage() {
  const { level, id } = useParams()
  const navigate = useNavigate()
  const { t, lang } = useLang()

  const [questions, setQuestions] = useState([])
  const [qIdx, setQIdx] = useState(0)
  const [selected, setSelected] = useState(null)
  const [score, setScore] = useState(0)
  const [finished, setFinished] = useState(false)
  const [isPlaying, setIsPlaying] = useState(false)

  useEffect(() => {
    api.getLessonVocab(level, parseInt(id)).then(words => {
      const shuffled = shuffle(words)
      const qs = shuffled.map(w => buildQuestion(w, shuffled, lang))
      setQuestions(qs)
    })
    window.Telegram?.WebApp?.BackButton?.show()
    window.Telegram?.WebApp?.BackButton?.onClick(() => navigate(`/lesson/${level}/${id}`))
    return () => window.Telegram?.WebApp?.BackButton?.hide()
  }, [level, id, lang])

  // Auto-play audio when question changes
  useEffect(() => {
    if (!questions.length || finished) return
    const q = questions[qIdx]
    if (q) {
      setSelected(null)
      setIsPlaying(true)
      setTimeout(() => {
        speakDE(q.word.de)
        setTimeout(() => setIsPlaying(false), 1500)
      }, 400)
    }
  }, [qIdx, questions, finished])

  const handlePlay = useCallback(() => {
    if (!questions.length) return
    setIsPlaying(true)
    speakDE(questions[qIdx].word.de)
    setTimeout(() => setIsPlaying(false), 1500)
  }, [qIdx, questions])

  const handleAnswer = (opt) => {
    if (selected !== null) return
    setSelected(opt)
    const correct = questions[qIdx].correct
    if (opt === correct) setScore(s => s + 1)

    setTimeout(() => {
      if (qIdx + 1 >= questions.length) {
        setFinished(true)
      } else {
        setQIdx(i => i + 1)
      }
    }, 1100)
  }

  if (!questions.length) return (
    <div className="loading"><div className="spinner" /></div>
  )

  if (finished) {
    const pct = Math.round((score / questions.length) * 100)
    const emoji = pct >= 80 ? '🏆' : pct >= 50 ? '👍' : '📚'
    return (
      <div className="page" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '85vh', textAlign: 'center' }}>
        <div style={{ fontSize: 72, marginBottom: 16 }}>{emoji}</div>
        <h2 style={{ fontSize: 22, fontWeight: 800, marginBottom: 4 }}>{t.result}</h2>
        <div style={{ fontSize: 48, fontWeight: 900, marginBottom: 4,
          color: pct >= 80 ? 'var(--success)' : pct >= 50 ? 'var(--warning)' : 'var(--danger)' }}>
          {pct}%
        </div>
        <div style={{ fontSize: 16, color: 'var(--tg-hint)', marginBottom: 8 }}>
          {score} / {questions.length}
        </div>
        <div className="xp-chip" style={{ marginBottom: 24 }}>⭐ +{score * 2} XP</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 10, width: '100%', maxWidth: 300 }}>
          <button className="btn btn-primary" onClick={() => { setQIdx(0); setScore(0); setFinished(false); setSelected(null) }}>
            🔄 {t.tryAgain}
          </button>
          <button className="btn btn-secondary" onClick={() => navigate(`/lesson/${level}/${id}`)}>
            {t.backToLessons}
          </button>
        </div>
      </div>
    )
  }

  const q = questions[qIdx]
  const progress = (qIdx / questions.length) * 100

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
          🎧 {qIdx + 1}/{questions.length}
        </div>
        <div style={{ fontWeight: 800, color: 'var(--success)', fontSize: 16 }}>✓ {score}</div>
      </div>

      <div className="progress-bar" style={{ marginBottom: 32 }}>
        <div className="progress-bar-fill" style={{ width: `${progress}%` }} />
      </div>

      {/* Listen card */}
      <div className="card" style={{ textAlign: 'center', padding: '44px 24px', marginBottom: 28 }}>
        <div style={{ fontSize: 13, color: 'var(--tg-hint)', marginBottom: 16 }}>
          {lang === 'uz' ? "Eshiting va tarjimani tanlang" : 'Слушайте и выберите перевод'}
        </div>

        {/* Big play button */}
        <button
          onClick={handlePlay}
          style={{
            width: 80, height: 80,
            borderRadius: '50%',
            border: `3px solid ${isPlaying ? 'var(--accent)' : 'rgba(255,255,255,.2)'}`,
            background: isPlaying ? 'rgba(99,102,241,.2)' : 'rgba(255,255,255,.06)',
            fontSize: 32,
            cursor: 'pointer',
            transition: 'all .2s',
            display: 'inline-flex',
            alignItems: 'center',
            justifyContent: 'center',
            animation: isPlaying ? 'pulse 1s ease infinite' : 'none',
          }}
        >
          {isPlaying ? '🔈' : '🔊'}
        </button>

        <div style={{ fontSize: 13, color: 'var(--tg-hint)', marginTop: 14 }}>
          {lang === 'uz' ? "Yana eshitish uchun bosing" : 'Нажмите чтобы послушать снова'}
        </div>

        {/* Reveal DE word after answering */}
        {selected !== null && (
          <div style={{ marginTop: 16, fontSize: 18, fontWeight: 800, color: 'var(--accent)' }}>
            🇩🇪 {q.word.de}
          </div>
        )}
      </div>

      {/* Options */}
      {q.opts.map((opt, i) => {
        let bg = 'rgba(255,255,255,.05)'
        let border = 'rgba(255,255,255,.1)'
        let color = 'var(--tg-text)'

        if (selected !== null) {
          if (opt === q.correct) { bg = 'var(--success-dim)'; border = 'rgba(34,197,94,.4)'; color = 'var(--success)' }
          else if (opt === selected) { bg = 'var(--danger-dim)'; border = 'rgba(239,68,68,.4)'; color = 'var(--danger)' }
          else { bg = 'rgba(255,255,255,.03)'; color = 'rgba(255,255,255,.3)' }
        }

        return (
          <button
            key={i}
            onClick={() => handleAnswer(opt)}
            style={{
              display: 'block',
              width: '100%',
              padding: '16px 20px',
              marginBottom: 10,
              borderRadius: 14,
              border: `1.5px solid ${border}`,
              background: bg,
              color,
              fontWeight: 700,
              fontSize: 16,
              cursor: selected !== null ? 'default' : 'pointer',
              transition: 'all .2s',
              textAlign: 'left',
            }}
          >
            <span style={{
              display: 'inline-flex', alignItems: 'center', justifyContent: 'center',
              width: 26, height: 26, borderRadius: '50%',
              background: 'rgba(255,255,255,.08)',
              fontSize: 12, fontWeight: 800, marginRight: 12,
            }}>
              {String.fromCharCode(65 + i)}
            </span>
            {opt}
          </button>
        )
      })}

      {/* Feedback */}
      {selected !== null && (
        <div style={{
          marginTop: 4, padding: '12px 16px', borderRadius: 12,
          background: selected === q.correct ? 'var(--success-dim)' : 'var(--danger-dim)',
          color: selected === q.correct ? 'var(--success)' : 'var(--danger)',
          fontWeight: 700, textAlign: 'center', fontSize: 15,
        }}>
          {selected === q.correct ? `✓ ${t.correct}` : `✗ ${t.wrong}`}
        </div>
      )}
    </div>
  )
}
