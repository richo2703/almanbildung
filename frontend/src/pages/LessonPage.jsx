import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api } from '../api'
import { useLang } from '../LangContext'
import { speakDE, isSpeechSupported } from '../speak'

function SpeakBtn({ text, size = 'sm' }) {
  const [active, setActive] = useState(false)
  if (!isSpeechSupported()) return null
  const handleSpeak = (e) => {
    e.stopPropagation()
    setActive(true)
    speakDE(text)
    setTimeout(() => setActive(false), 1200)
  }
  return (
    <button onClick={handleSpeak} style={{
      background: active ? 'rgba(99,102,241,.2)' : 'transparent',
      border: 'none',
      borderRadius: 8,
      padding: size === 'sm' ? '2px 6px' : '5px 10px',
      cursor: 'pointer',
      fontSize: size === 'sm' ? 14 : 18,
      color: active ? 'var(--accent)' : 'var(--tg-hint)',
      transition: 'all .2s',
      flexShrink: 0,
    }}>
      {active ? '🔈' : '🔊'}
    </button>
  )
}

export default function LessonPage() {
  const { level, id } = useParams()
  const navigate = useNavigate()
  const { t, lang } = useLang()
  const [lesson, setLesson] = useState(null)
  const [marked, setMarked] = useState(false)

  useEffect(() => {
    api.getLesson(level, parseInt(id)).then(setLesson)
    window.Telegram?.WebApp?.BackButton?.show()
    window.Telegram?.WebApp?.BackButton?.onClick(() => navigate(`/learn/${level}`))
    return () => window.Telegram?.WebApp?.BackButton?.hide()
  }, [level, id])

  const handleStartVocab = async () => {
    if (!marked) {
      await api.markLessonDone(level, parseInt(id)).catch(() => {})
      setMarked(true)
    }
    navigate(`/vocab/${level}/${id}`)
  }

  if (!lesson) return (
    <div className="loading">
      <div className="spinner" />
      <span>{lang === 'uz' ? 'Yuklanmoqda...' : 'Загрузка...'}</span>
    </div>
  )

  const grammarText = lang === 'uz' ? lesson.grammar_uz : lesson.grammar_ru
  const titleText = lang === 'uz' ? lesson.title_uz : lesson.title_ru

  return (
    <div className="page">
      {/* Header */}
      <div className="page-header">
        <button className="back-btn" onClick={() => navigate(`/learn/${level}`)}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="15 18 9 12 15 6"/>
          </svg>
        </button>
        <div style={{ flex: 1, minWidth: 0 }}>
          <div style={{ fontSize: 12, color: 'var(--tg-hint)', marginBottom: 2 }}>{level}</div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
            <h1 style={{ fontSize: 17, fontWeight: 700, whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
              {lesson.title_de}
            </h1>
            <SpeakBtn text={lesson.title_de} size="sm" />
          </div>
          <div style={{ fontSize: 13, color: 'var(--tg-hint)' }}>{titleText}</div>
        </div>
      </div>

      {/* Grammar */}
      {lesson.grammar_topic && (
        <>
          <div className="section-title">📖 {t.grammar}</div>
          <div className="grammar-box">
            <div style={{ fontWeight: 700, marginBottom: 6, color: 'var(--accent)', fontSize: 15 }}>
              {lesson.grammar_topic}
            </div>
            <div style={{ fontSize: 14, lineHeight: 1.7, color: 'var(--tg-text)' }}>
              {grammarText || lesson.grammar_ru}
            </div>
          </div>
        </>
      )}

      {/* Vocab preview */}
      <div className="section-title">📝 {t.words} ({lesson.vocab?.length})</div>
      <div className="card" style={{ marginBottom: 16 }}>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 4 }}>
          {lesson.vocab?.slice(0, 12).map((w, i) => (
            <span
              key={i}
              className="word-chip"
              onClick={() => speakDE(w.de)}
              style={{ cursor: 'pointer', display: 'inline-flex', alignItems: 'center', gap: 4 }}
            >
              {w.de} <span style={{ fontSize: 11, opacity: .6 }}>🔊</span>
            </span>
          ))}
          {lesson.vocab?.length > 12 && (
            <span className="word-chip" style={{ color: 'var(--tg-hint)' }}>
              +{lesson.vocab.length - 12}
            </span>
          )}
        </div>
      </div>

      {/* Dialogue */}
      {lesson.dialogue?.length > 0 && (
        <>
          <div className="section-title">💬 {t.dialogue}</div>
          <div className="card" style={{ marginBottom: 16 }}>
            <div className="dialogue-wrap">
              {lesson.dialogue.map(([speaker, text], i) => (
                <div key={i} className={`dialogue-bubble ${speaker === 'A' ? 'bubble-a' : 'bubble-b'}`}>
                  <span style={{ fontWeight: 700, fontSize: 10, opacity: .7, display: 'block', marginBottom: 3 }}>
                    {speaker}
                  </span>
                  {text}
                </div>
              ))}
            </div>
          </div>
        </>
      )}

      {/* Actions */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: 10, marginTop: 12 }}>
        <button className="btn btn-primary" onClick={handleStartVocab}>
          🃏 {t.startVocab} ({lesson.vocab?.length})
        </button>
        <button className="btn btn-secondary"
          onClick={() => navigate(`/test/${level}/${id}`)}>
          ✅ {t.startTest} ({lesson.exercises?.length})
        </button>
      </div>
    </div>
  )
}
