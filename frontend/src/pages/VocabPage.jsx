import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api } from '../api'
import { useLang } from '../LangContext'

export default function VocabPage() {
  const { level, id } = useParams()
  const navigate = useNavigate()
  const { t, lang } = useLang()
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

  if (!words.length) return (
    <div className="loading"><div className="spinner" /></div>
  )

  if (done) {
    const total = stats.known + stats.unknown
    const pct = total ? Math.round((stats.known / total) * 100) : 0
    return (
      <div className="page" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '85vh', textAlign: 'center' }}>
        <div style={{ fontSize: 72, marginBottom: 16 }}>{pct >= 70 ? '🏆' : '💪'}</div>
        <h2 style={{ fontSize: 26, fontWeight: 800, marginBottom: 8 }}>{t.result}</h2>
        <div style={{ display: 'flex', gap: 24, marginBottom: 24 }}>
          <div>
            <div style={{ fontSize: 32, fontWeight: 800, color: 'var(--success)' }}>{stats.known}</div>
            <div style={{ fontSize: 13, color: 'var(--tg-hint)' }}>{t.know}</div>
          </div>
          <div style={{ width: 1, background: 'var(--card-border)' }} />
          <div>
            <div style={{ fontSize: 32, fontWeight: 800, color: 'var(--danger)' }}>{stats.unknown}</div>
            <div style={{ fontSize: 13, color: 'var(--tg-hint)' }}>{t.dontKnow}</div>
          </div>
        </div>
        <div className="xp-chip" style={{ marginBottom: 28 }}>⭐ +{stats.known * 2} XP</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 10, width: '100%', maxWidth: 320 }}>
          <button className="btn btn-primary" onClick={() => navigate(`/test/${level}/${id}`)}>
            ✅ {t.startTest}
          </button>
          <button className="btn btn-secondary"
            onClick={() => { setIdx(0); setFlipped(false); setDone(false); setStats({ known: 0, unknown: 0 }) }}>
            🔄 {t.tryAgain}
          </button>
          <button className="btn btn-secondary" onClick={() => navigate(`/learn/${level}`)}>
            {t.backToLessons}
          </button>
        </div>
      </div>
    )
  }

  const word = words[idx]
  const progress = (idx / words.length) * 100
  const translation = lang === 'uz' ? word.uz : word.ru

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
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 12 }}>
        <button className="back-btn" onClick={() => navigate(`/lesson/${level}/${id}`)}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="15 18 9 12 15 6"/>
          </svg>
        </button>
        <span style={{ color: 'var(--tg-hint)', fontWeight: 700, fontSize: 14 }}>
          {idx + 1} / {words.length}
        </span>
        <div className="xp-chip">⭐ +2</div>
      </div>

      <div className="progress-bar" style={{ marginBottom: 28 }}>
        <div className="progress-bar-fill" style={{ width: `${progress}%` }} />
      </div>

      {/* Flashcard */}
      <div className="flashcard" onClick={() => setFlipped(f => !f)} style={{ cursor: 'pointer', userSelect: 'none' }}>
        {!flipped ? (
          <>
            <div style={{ fontSize: 12, color: 'var(--tg-hint)', letterSpacing: 1, textTransform: 'uppercase', fontWeight: 600 }}>
              🇩🇪 Deutsch
            </div>
            <div className="flashcard-word">{word.de}</div>
            <div style={{ fontSize: 13, color: 'var(--tg-hint)', marginTop: 8 }}>
              👆 {t.tapToFlip}
            </div>
          </>
        ) : (
          <>
            <div style={{ fontSize: 12, color: 'var(--tg-hint)', letterSpacing: 1, textTransform: 'uppercase', fontWeight: 600 }}>
              {lang === 'uz' ? '🇺🇿 O\'zbek' : '🇷🇺 Русский'}
            </div>
            <div className="flashcard-word" style={{ fontSize: 26 }}>{translation}</div>
            {lang === 'uz' && word.ru && (
              <div className="flashcard-translation">{word.ru}</div>
            )}
            {lang === 'ru' && word.uz && (
              <div className="flashcard-translation">{word.uz}</div>
            )}
            <div style={{ marginTop: 12, fontSize: 14, color: 'var(--accent)', fontWeight: 600 }}>
              🇩🇪 {word.de}
            </div>
          </>
        )}
      </div>

      {/* Buttons */}
      {flipped ? (
        <div className="vocab-actions">
          <button
            className="btn"
            style={{ background: 'var(--danger-dim)', color: 'var(--danger)', border: '1px solid rgba(239,68,68,.3)' }}
            onClick={() => handleKnow(false)}>
            ✗ {t.dontKnow}
          </button>
          <button
            className="btn"
            style={{ background: 'var(--success-dim)', color: 'var(--success)', border: '1px solid rgba(34,197,94,.3)' }}
            onClick={() => handleKnow(true)}>
            ✓ {t.know}
          </button>
        </div>
      ) : (
        <button className="btn btn-secondary" onClick={() => setFlipped(true)}>
          {t.showTranslation}
        </button>
      )}

      {/* Counter */}
      <div style={{ display: 'flex', justifyContent: 'center', gap: 24, marginTop: 20 }}>
        <span style={{ color: 'var(--success)', fontWeight: 700 }}>✓ {stats.known}</span>
        <span style={{ color: 'var(--danger)', fontWeight: 700 }}>✗ {stats.unknown}</span>
      </div>
    </div>
  )
}
