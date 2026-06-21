import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api } from '../api'

export default function TestPage() {
  const { level, id } = useParams()
  const navigate = useNavigate()
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

  if (!questions.length) return <div className="loading">Загрузка...</div>

  if (finished) {
    const pct = Math.round((score / questions.length) * 100)
    const emoji = pct >= 80 ? '🏆' : pct >= 50 ? '👍' : '📚'

    return (
      <div className="page" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '80vh', textAlign: 'center' }}>
        <div style={{ fontSize: 64, marginBottom: 16 }}>{emoji}</div>
        <h2 style={{ fontSize: 24, fontWeight: 700, marginBottom: 8 }}>
          {score} / {questions.length}
        </h2>
        <div style={{ fontSize: 36, fontWeight: 800, color: pct >= 80 ? 'var(--success)' : pct >= 50 ? 'var(--warning)' : 'var(--danger)', marginBottom: 8 }}>
          {pct}%
        </div>
        <p style={{ color: 'var(--tg-hint)', marginBottom: 8 }}>
          Заработано: <b style={{ color: '#92400E' }}>⭐ +{score * 2} XP</b>
        </p>
        <p style={{ color: 'var(--tg-hint)', marginBottom: 28 }}>
          {pct >= 80 ? 'Отличный результат!' : pct >= 50 ? 'Неплохо, продолжай!' : 'Повтори слова и попробуй снова'}
        </p>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 10, width: '100%', maxWidth: 320 }}>
          <button className="btn btn-primary"
            onClick={() => navigate(`/learn/${level}`)}>
            К урокам
          </button>
          <button className="btn btn-secondary"
            onClick={() => { setQIdx(0); setSelected(null); setScore(0); setFinished(false) }}>
            🔄 Пройти снова
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
    if (correct) setScore(s => s + 1)

    setTimeout(async () => {
      if (qIdx + 1 >= questions.length) {
        const newScore = score + (correct ? 1 : 0)
        await api.saveTestResult(level, parseInt(id), newScore, questions.length).catch(() => {})
        setScore(newScore)
        setFinished(true)
      } else {
        setQIdx(i => i + 1)
        setSelected(null)
      }
    }, 900)
  }

  return (
    <div className="page">
      {/* Header */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 16 }}>
        <button className="back-btn" onClick={() => navigate(`/lesson/${level}/${id}`)}>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none"
            stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="15 18 9 12 15 6"/>
          </svg>
        </button>
        <span style={{ color: 'var(--tg-hint)', fontWeight: 600 }}>
          {qIdx + 1} / {questions.length}
        </span>
        <div style={{ fontWeight: 700, color: 'var(--success)' }}>✓ {score}</div>
      </div>

      <div className="progress-bar" style={{ marginBottom: 24 }}>
        <div className="progress-bar-fill" style={{ width: `${progress}%` }} />
      </div>

      {/* Question */}
      <div className="card" style={{ marginBottom: 20 }}>
        <div style={{ fontWeight: 600, fontSize: 16, lineHeight: 1.4 }}>
          {q.q}
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
            <span style={{ fontWeight: 600, marginRight: 8, color: 'var(--tg-hint)' }}>
              {String.fromCharCode(65 + i)}.
            </span>
            {opt}
          </button>
        )
      })}
    </div>
  )
}
