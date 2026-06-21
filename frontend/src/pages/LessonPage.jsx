import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api } from '../api'

export default function LessonPage() {
  const { level, id } = useParams()
  const navigate = useNavigate()
  const [lesson, setLesson] = useState(null)
  const [marked, setMarked] = useState(false)

  useEffect(() => {
    api.getLesson(level, parseInt(id)).then(setLesson)
    window.Telegram?.WebApp?.BackButton?.show()
    window.Telegram?.WebApp?.BackButton?.onClick(() => navigate(`/learn/${level}`))
    return () => window.Telegram?.WebApp?.BackButton?.hide()
  }, [level, id])

  const handleDone = async () => {
    if (!marked) {
      await api.markLessonDone(level, parseInt(id)).catch(() => {})
      setMarked(true)
    }
    navigate(`/vocab/${level}/${id}`)
  }

  if (!lesson) return <div className="loading">Загрузка...</div>

  return (
    <div className="page">
      <div className="page-header">
        <button className="back-btn" onClick={() => navigate(`/learn/${level}`)}>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none"
            stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="15 18 9 12 15 6"/>
          </svg>
        </button>
        <div>
          <h1 style={{ fontSize: 18 }}>{lesson.title_de}</h1>
          <div style={{ fontSize: 13, color: 'var(--tg-hint)' }}>{lesson.title_ru}</div>
        </div>
      </div>

      {/* Grammar */}
      {lesson.grammar_topic && (
        <>
          <div className="section-title">Грамматика</div>
          <div className="grammar-box">
            <div style={{ fontWeight: 700, marginBottom: 6 }}>{lesson.grammar_topic}</div>
            <div style={{ fontSize: 14 }}>{lesson.grammar_ru}</div>
          </div>
        </>
      )}

      {/* Vocabulary preview */}
      <div className="section-title">Слова ({lesson.vocab?.length})</div>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6, marginBottom: 16 }}>
        {lesson.vocab?.slice(0, 10).map((w, i) => (
          <span key={i} style={{
            background: 'var(--tg-secondary-bg)',
            borderRadius: 8,
            padding: '4px 10px',
            fontSize: 13,
            fontWeight: 600,
          }}>
            {w.de}
          </span>
        ))}
        {lesson.vocab?.length > 10 && (
          <span style={{ fontSize: 13, color: 'var(--tg-hint)', padding: '4px 6px' }}>
            +{lesson.vocab.length - 10} ещё
          </span>
        )}
      </div>

      {/* Dialogue */}
      {lesson.dialogue?.length > 0 && (
        <>
          <div className="section-title">Диалог</div>
          <div className="dialogue-wrap" style={{ marginBottom: 16 }}>
            {lesson.dialogue.map(([speaker, text], i) => (
              <div key={i}
                className={`dialogue-bubble ${speaker === 'A' ? 'bubble-a' : 'bubble-b'}`}>
                <span style={{ fontWeight: 600, fontSize: 11, opacity: .7, display: 'block', marginBottom: 2 }}>
                  {speaker}:
                </span>
                {text}
              </div>
            ))}
          </div>
        </>
      )}

      {/* Actions */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: 10, marginTop: 8 }}>
        <button className="btn btn-primary" onClick={handleDone}>
          🃏 Учить слова ({lesson.vocab?.length})
        </button>
        <button className="btn btn-secondary"
          onClick={() => navigate(`/test/${level}/${id}`)}>
          ✅ Пройти тест ({lesson.exercises?.length} вопросов)
        </button>
      </div>
    </div>
  )
}
