import { useState, useEffect } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api } from '../api'
import { useLang } from '../LangContext'

export default function ExamSchreibenPage() {
  const { provider, level, taskId } = useParams()
  const navigate = useNavigate()
  const { lang } = useLang()
  const [task, setTask] = useState(null)
  const [text, setText] = useState('')
  const [loading, setLoading] = useState(true)
  const [submitting, setSubmitting] = useState(false)
  const [result, setResult] = useState(null)
  const [showModel, setShowModel] = useState(false)
  const [showRedemittel, setShowRedemittel] = useState(false)

  useEffect(() => {
    const id = parseInt(taskId)
    api.exam.getTask(id)
      .then(t => {
        setTask(t)
        return api.exam.getLatestWriting(id).catch(() => null)
      })
      .then(prev => { if (prev?.user_text) setText(prev.user_text) })
      .catch(() => {})
      .finally(() => setLoading(false))
  }, [taskId])

  const handleSubmit = async () => {
    if (!text.trim() || submitting) return
    setSubmitting(true)
    try {
      const res = await api.exam.submitWriting(parseInt(taskId), text)
      setResult(res)
      setShowModel(true)
    } catch (e) {
      alert(lang === 'uz' ? "Xatolik yuz berdi" : "Ошибка при отправке")
    } finally {
      setSubmitting(false)
    }
  }

  const wordCount = text.trim().split(/\s+/).filter(Boolean).length
  const extra = task?.extra || {}
  const minWords = extra.word_count_min || 20
  const maxWords = extra.word_count_max || 40

  if (loading) return <div className="page" style={{ color: 'var(--tg-hint)', textAlign: 'center', paddingTop: 60 }}>...</div>
  if (!task) return <div className="page"><div style={{ color: 'var(--tg-hint)' }}>Задание не найдено</div></div>

  const sectionPath = `/exam/${provider}/${level}/schreiben`

  return (
    <div className="page">
      <button onClick={() => navigate(sectionPath)}
        style={{ background: 'none', color: 'var(--tg-hint)', fontSize: 13, marginBottom: 20, padding: 0 }}>
        ← {lang === 'uz' ? 'Orqaga' : 'Назад'}
      </button>

      {/* Title */}
      <div style={{ marginBottom: 16 }}>
        <div style={{ fontSize: 17, fontWeight: 800, marginBottom: 4 }}>
          ✍️ {lang === 'uz' ? (task.title_ru || task.title_de) : (task.title_ru || task.title_de)}
        </div>
        <div style={{ fontSize: 12, color: 'var(--tg-hint)' }}>
          {lang === 'uz' ? task.instruction_uz : (task.instruction_ru || task.instruction_de)}
        </div>
      </div>

      {/* Task prompt */}
      {task.text_content && (
        <div style={{
          background: 'rgba(99,102,241,.08)', border: '1px solid rgba(99,102,241,.2)',
          borderRadius: 'var(--radius-sm)', padding: 14, marginBottom: 16,
          fontSize: 13, lineHeight: 1.7, whiteSpace: 'pre-wrap',
        }}>
          {task.text_content}
        </div>
      )}

      {/* Redemittel toggle */}
      {extra.redemittel?.length > 0 && (
        <div style={{ marginBottom: 12 }}>
          <button
            onClick={() => setShowRedemittel(!showRedemittel)}
            style={{
              background: 'rgba(168,85,247,.1)', border: '1px solid rgba(168,85,247,.2)',
              borderRadius: 8, padding: '8px 14px', color: '#A855F7',
              fontSize: 12, fontWeight: 700, width: '100%', textAlign: 'left',
            }}
          >
            {showRedemittel ? '▼' : '▶'} 💬 {lang === 'uz' ? "Foydali iboralar (Redemittel)" : "Полезные фразы (Redemittel)"}
          </button>
          {showRedemittel && (
            <div style={{
              background: 'rgba(168,85,247,.05)', border: '1px solid rgba(168,85,247,.15)',
              borderRadius: '0 0 8px 8px', padding: 12, marginTop: -1,
            }}>
              {extra.redemittel.map((r, i) => (
                <div key={i} style={{
                  fontSize: 13, padding: '5px 0',
                  borderBottom: i < extra.redemittel.length - 1 ? '1px solid rgba(255,255,255,.06)' : 'none',
                }}>
                  {r}
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* Text area */}
      <div style={{ position: 'relative', marginBottom: 8 }}>
        <textarea
          value={text}
          onChange={e => setText(e.target.value)}
          placeholder={lang === 'uz' ? "Shu yerga yozing..." : "Пишите здесь..."}
          style={{
            width: '100%', minHeight: 160, padding: 14, borderRadius: 'var(--radius-sm)',
            background: 'rgba(255,255,255,.05)', border: '1px solid var(--card-border)',
            color: 'var(--tg-text)', fontSize: 14, lineHeight: 1.7, resize: 'vertical',
            fontFamily: 'inherit', outline: 'none',
          }}
        />
        <div style={{
          position: 'absolute', bottom: 8, right: 12,
          fontSize: 11,
          color: wordCount < minWords ? 'var(--warning)' : wordCount > maxWords ? 'var(--danger)' : 'var(--success)',
          fontWeight: 700,
        }}>
          {wordCount} {lang === 'uz' ? "so'z" : "слов"}
          {extra.word_count_max && ` / ${minWords}–${maxWords}`}
        </div>
      </div>

      {/* Checklist (show after submit) */}
      {result && extra.checklist?.length > 0 && (
        <div style={{
          background: 'rgba(34,197,94,.06)', border: '1px solid rgba(34,197,94,.2)',
          borderRadius: 'var(--radius-sm)', padding: 14, marginBottom: 12,
        }}>
          <div style={{ fontSize: 13, fontWeight: 700, marginBottom: 8, color: 'var(--success)' }}>
            ✅ {lang === 'uz' ? "O'z-o'zini tekshirish" : "Самопроверка"}
          </div>
          {extra.checklist.map((item, i) => (
            <div key={i} style={{ display: 'flex', gap: 8, fontSize: 13, marginBottom: 5 }}>
              <span style={{ color: 'var(--success)', flexShrink: 0 }}>□</span>
              <span>{item}</span>
            </div>
          ))}
        </div>
      )}

      {/* Model answer */}
      {result && (
        <div style={{ marginBottom: 16 }}>
          <button
            onClick={() => setShowModel(!showModel)}
            style={{
              background: 'rgba(59,130,246,.1)', border: '1px solid rgba(59,130,246,.2)',
              borderRadius: 8, padding: '8px 14px', color: 'var(--accent)',
              fontSize: 12, fontWeight: 700, width: '100%', textAlign: 'left',
            }}
          >
            {showModel ? '▼' : '▶'} 📝 {lang === 'uz' ? "Namunaviy javob" : "Пример хорошего ответа"}
          </button>
          {showModel && result.model_answer && (
            <div style={{
              background: 'rgba(59,130,246,.05)', border: '1px solid rgba(59,130,246,.15)',
              borderRadius: '0 0 8px 8px', padding: 14, marginTop: -1,
              fontSize: 13, lineHeight: 1.7, whiteSpace: 'pre-wrap',
            }}>
              {result.model_answer}
            </div>
          )}
        </div>
      )}

      {/* AI feedback placeholder */}
      {result && (
        <div style={{
          background: 'rgba(245,158,11,.06)', border: '1px solid rgba(245,158,11,.15)',
          borderRadius: 'var(--radius-sm)', padding: 12, marginBottom: 16,
          fontSize: 12, color: 'var(--tg-hint)',
        }}>
          🤖 {lang === 'uz'
            ? "AI-tekshiruv keyingi versiyada mavjud bo'ladi. Namunaviy javob bilan solishtiring."
            : "AI-проверка будет доступна в следующей версии. Сравните с примером хорошего ответа."}
        </div>
      )}

      {/* Action buttons */}
      {!result ? (
        <button
          className="btn btn-primary"
          onClick={handleSubmit}
          disabled={!text.trim() || submitting}
          style={{ opacity: text.trim() ? 1 : 0.4 }}
        >
          {submitting
            ? (lang === 'uz' ? "Saqlanmoqda..." : "Сохраняем...")
            : (lang === 'uz' ? "Javobni saqlash →" : "Сохранить ответ →")}
        </button>
      ) : (
        <div style={{ display: 'flex', gap: 10 }}>
          <button className="btn btn-secondary" style={{ flex: 1 }}
            onClick={() => { setResult(null); setShowModel(false) }}>
            ✏️ {lang === 'uz' ? "Qayta yozish" : "Переписать"}
          </button>
          <button className="btn btn-primary" style={{ flex: 1 }}
            onClick={() => navigate(sectionPath)}>
            {lang === 'uz' ? "Davom etish →" : "Продолжить →"}
          </button>
        </div>
      )}
    </div>
  )
}
