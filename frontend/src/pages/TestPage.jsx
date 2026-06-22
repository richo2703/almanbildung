import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api } from '../api'
import { useLang } from '../LangContext'
import { speakDE, isSpeechSupported } from '../speak'

export default function TestPage() {
  const { level, id } = useParams()
  const navigate = useNavigate()
  const { t, lang } = useLang()
  const [questions, setQuestions] = useState([])
  const [qIdx, setQIdx] = useState(0)
  const [selected, setSelected] = useState(null)
  const [score, setScore] = useState(0)
  const [finished, setFinished] = useState(false)

  useEffect(() => {
    api.getLessonExercises(level, parseInt(id)).then(setQuestions)
    window.Telegram?.WebApp?.BackButton?.show()
    window.Telegram?.WebApp?.BackButton?.onClick(() => navigate(`/lesson/${level}/${id}`))
    return () => window.Telegram?.WebApp?.BackButton?.hide()
  }, [level, id])

  if (!questions.length) return (
    <div className="loading"><div className="spinner" /></div>
  )

  if (finished) {
    const pct = Math.round((score / questions.length) * 100)
    const emoji = pct >= 80 ? '🏆' : pct >= 50 ? '👍' : '📚'
    const msg = pct >= 80 ? t.excellent : pct >= 50 ? t.good : t.needMore

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
        <div className="xp-chip" style={{ marginBottom: 8 }}>⭐ +{score * 2} XP</div>
        <p style={{ color: 'var(--tg-hint)', marginBottom: 28, fontSize: 14 }}>{msg}</p>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 10, width: '100%', maxWidth: 320 }}>
          <button className="btn btn-primary" onClick={() => navigate(`/learn/${level}`)}>
            {t.backToLessons}
          </button>
          <button className="btn btn-secondary"
            onClick={() => { setQIdx(0); setSelected(null); setScore(0); setFinished(false) }}>
            🔄 {t.tryAgain}
          </button>
        </div>
      </div>
    )
  }

  const q = questions[qIdx]
  const progress = (qIdx / questions.length) * 100

  const handleAnswer = async (optIdx) => {
    if (selected !== null) return
    setSelected(optIdx)
    const correct = optIdx === q.ans
    const newScore = score + (correct ? 1 : 0)

    setTimeout(async () => {
      if (qIdx + 1 >= questions.length) {
        await api.saveTestResult(level, parseInt(id), newScore, questions.length).catch(() => {})
        setScore(newScore)
        setFinished(true)
      } else {
        if (correct) setScore(s => s + 1)
        setQIdx(i => i + 1)
        setSelected(null)
      }
    }, 1000)
  }

  return (
    <div className="page">
      {/* Header */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 12 }}>
        <button className="back-btn" onClick={() => navigate(`/lesson/${level}/${id}`)}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="15 18 9 12 15 6"/>
          </svg>
        </button>
        <div style={{ textAlign: 'center' }}>
          <div style={{ fontWeight: 700, color: 'var(--tg-hint)', fontSize: 13 }}>
            {t.question} {qIdx + 1} / {questions.length}
          </div>
        </div>
        <div style={{ fontWeight: 800, color: 'var(--success)', fontSize: 16 }}>✓ {score}</div>
      </div>

      <div className="progress-bar" style={{ marginBottom: 28 }}>
        <div className="progress-bar-fill" style={{ width: `${progress}%` }} />
      </div>

      {/* Question */}
      <div className="card" style={{ marginBottom: 20, padding: '20px 18px' }}>
        <div style={{ display: 'flex', alignItems: 'flex-start', gap: 10 }}>
          <div style={{ fontWeight: 600, fontSize: 16, lineHeight: 1.5, flex: 1 }}>{q.q}</div>
          {isSpeechSupported() && (
            <button
              onClick={() => speakDE(q.q)}
              style={{
                background: 'rgba(255,255,255,.07)',
                border: '1px solid rgba(255,255,255,.12)',
                borderRadius: 10,
                padding: '6px 10px',
                cursor: 'pointer',
                fontSize: 16,
                color: 'var(--tg-hint)',
                flexShrink: 0,
              }}
            >🔊</button>
          )}
        </div>
      </div>

      {/* Options */}
      {q.opts.map((opt, i) => {
        let cls = 'quiz-option'
        if (selected !== null) {
          if (i === q.ans) cls += ' correct'
          else if (i === selected && selected !== q.ans) cls += ' wrong'
        }

        return (
          <button key={i} className={cls} onClick={() => handleAnswer(i)}>
            <span style={{
              display: 'inline-flex',
              alignItems: 'center',
              justifyContent: 'center',
              width: 24, height: 24,
              borderRadius: '50%',
              background: 'rgba(255,255,255,.1)',
              fontSize: 12,
              fontWeight: 800,
              marginRight: 10,
              flexShrink: 0,
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
          marginTop: 12,
          padding: '12px 16px',
          borderRadius: 'var(--radius)',
          background: selected === q.ans ? 'var(--success-dim)' : 'var(--danger-dim)',
          color: selected === q.ans ? 'var(--success)' : 'var(--danger)',
          fontWeight: 700,
          textAlign: 'center',
          fontSize: 15,
        }}>
          {selected === q.ans ? `✓ ${t.correct}` : `✗ ${t.wrong}`}
        </div>
      )}
    </div>
  )
}
