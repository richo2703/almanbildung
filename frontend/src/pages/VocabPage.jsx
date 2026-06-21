import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api } from '../api'

export default function VocabPage() {
  const { level, id } = useParams()
  const navigate = useNavigate()
  const [words, setWords] = useState([])
  const [idx, setIdx] = useState(0)
  const [flipped, setFlipped] = useState(false)
  const [stats, setStats] = useState({ known: 0, unknown: 0 })
  const [done, setDone] = useState(false)

  useEffect(() => {
    api.getLessonVocab(level, parseInt(id)).then(setWords)
    window.Telegram?.WebApp?.BackButton?.show()
    window.Telegram?.WebApp?.BackButton?.onClick(() => navigate(`/lesson/${level}/${id}`))
    return () => window.Telegram?.WebApp?.BackButton?.hide()
  }, [level, id])

  if (!words.length) return <div className="loading">Загрузка...</div>

  if (done) {
    return (
      <div className="page" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '80vh', textAlign: 'center' }}>
        <div style={{ fontSize: 64, marginBottom: 16 }}>🎉</div>
        <h2 style={{ fontSize: 22, fontWeight: 700, marginBottom: 8 }}>Отлично!</h2>
        <p style={{ color: 'var(--tg-hint)', marginBottom: 24 }}>
          Знаешь: <b style={{ color: 'var(--success)' }}>{stats.known}</b> &nbsp;|&nbsp;
          Учить: <b style={{ color: 'var(--danger)' }}>{stats.unknown}</b>
        </p>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 10, width: '100%', maxWidth: 320 }}>
          <button className="btn btn-primary"
            onClick={() => navigate(`/test/${level}/${id}`)}>
            ✅ Пройти тест
          </button>
          <button className="btn btn-secondary"
            onClick={() => { setIdx(0); setFlipped(false); setDone(false); setStats({ known: 0, unknown: 0 }) }}>
            🔄 Повторить
          </button>
          <button className="btn btn-secondary"
            onClick={() => navigate(`/learn/${level}`)}>
            ← К урокам
          </button>
        </div>
      </div>
    )
  }

  const word = words[idx]
  const progress = ((idx) / words.length) * 100

  const handleKnow = async (known) => {
    await api.markVocab(level, word.de, known).catch(() => {})
    setStats(s => ({ ...s, [known ? 'known' : 'unknown']: s[known ? 'known' : 'unknown'] + 1 }))
    if (idx + 1 >= words.length) {
      setDone(true)
    } else {
      setIdx(i => i + 1)
      setFlipped(false)
    }
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
          {idx + 1} / {words.length}
        </span>
        <div className="xp-chip">⭐ +2</div>
      </div>

      <div className="progress-bar" style={{ marginBottom: 24 }}>
        <div className="progress-bar-fill" style={{ width: `${progress}%` }} />
      </div>

      {/* Flashcard */}
      <div
        className="flashcard"
        onClick={() => setFlipped(f => !f)}
        style={{ cursor: 'pointer', userSelect: 'none' }}>
        {!flipped ? (
          <>
            <div style={{ fontSize: 13, color: 'var(--tg-hint)', marginBottom: 8 }}>Немецкий</div>
            <div className="flashcard-word">{word.de}</div>
            <div style={{ fontSize: 13, color: 'var(--tg-hint)', marginTop: 16 }}>
              Нажми чтобы увидеть перевод
            </div>
          </>
        ) : (
          <>
            <div style={{ fontSize: 13, color: 'var(--tg-hint)', marginBottom: 8 }}>Перевод</div>
            <div className="flashcard-word" style={{ fontSize: 24 }}>{word.ru}</div>
            <div className="flashcard-translation">{word.uz}</div>
            <div style={{ fontSize: 13, color: 'var(--tg-hint)', marginTop: 12 }}>🇩🇪 {word.de}</div>
          </>
        )}
      </div>

      {/* Action buttons */}
      {flipped ? (
        <div className="vocab-actions">
          <button className="btn" style={{ background: '#FEF2F2', color: 'var(--danger)', borderRadius: 'var(--radius)' }}
            onClick={() => handleKnow(false)}>
            ✗ Не знаю
          </button>
          <button className="btn" style={{ background: '#F0FDF4', color: 'var(--success)', borderRadius: 'var(--radius)' }}
            onClick={() => handleKnow(true)}>
            ✓ Знаю
          </button>
        </div>
      ) : (
        <button className="btn btn-secondary" onClick={() => setFlipped(true)}>
          Показать перевод
        </button>
      )}

      {/* Counter */}
      <div style={{ display: 'flex', justifyContent: 'center', gap: 20, marginTop: 20 }}>
        <span style={{ color: 'var(--success)', fontWeight: 600 }}>✓ {stats.known}</span>
        <span style={{ color: 'var(--danger)', fontWeight: 600 }}>✗ {stats.unknown}</span>
      </div>
    </div>
  )
}
