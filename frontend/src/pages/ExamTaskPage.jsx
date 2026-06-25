import { useState, useEffect, useRef } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api } from '../api'
import { useLang } from '../LangContext'

function Timer({ seconds, onExpire }) {
  const [left, setLeft] = useState(seconds)
  const ref = useRef()
  useEffect(() => {
    if (left <= 0) { onExpire && onExpire(); return }
    ref.current = setTimeout(() => setLeft(l => l - 1), 1000)
    return () => clearTimeout(ref.current)
  }, [left])
  const m = Math.floor(left / 60)
  const s = left % 60
  const urgent = left < 60
  return (
    <div style={{
      display: 'flex', alignItems: 'center', gap: 6,
      color: urgent ? 'var(--danger)' : 'var(--tg-hint)',
      fontWeight: 700, fontSize: 14,
    }}>
      ⏱ {m}:{String(s).padStart(2, '0')}
    </div>
  )
}

export default function ExamTaskPage() {
  const { provider, level, taskId } = useParams()
  const navigate = useNavigate()
  const { lang } = useLang()
  const [task, setTask] = useState(null)
  const [answers, setAnswers] = useState({})
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(true)
  const [submitting, setSubmitting] = useState(false)
  const [showText, setShowText] = useState(true)

  useEffect(() => {
    api.exam.getTask(parseInt(taskId))
      .then(t => { setTask(t); setLoading(false) })
      .catch(() => setLoading(false))
  }, [taskId])

  const handleSelect = (questionId, optionText) => {
    if (result) return
    setAnswers(prev => ({ ...prev, [questionId]: optionText }))
  }

  const handleSubmit = async () => {
    if (submitting) return
    setSubmitting(true)
    try {
      const res = await api.exam.submitAttempt(parseInt(taskId), answers)
      setResult(res)
    } catch (e) {
      alert(lang === 'uz' ? "Xatolik yuz berdi" : "Ошибка при отправке")
    } finally {
      setSubmitting(false)
    }
  }

  const allAnswered = task && task.questions.every(q => answers[q.id] !== undefined)
  const sectionPath = `/exam/${provider}/${level}/lesen`

  if (loading) return <div className="page" style={{ color: 'var(--tg-hint)', textAlign: 'center', paddingTop: 60 }}>...</div>
  if (!task) return <div className="page"><div style={{ color: 'var(--tg-hint)' }}>{lang === 'uz' ? 'Topshiriq topilmadi' : 'Задание не найдено'}</div></div>

  // ── Results screen ─────────────────────────────────────────────────────────
  if (result) {
    const pct = Math.round(result.percentage)
    const passed = result.passed
    return (
      <div className="page">
        <div style={{
          textAlign: 'center', marginBottom: 24,
          padding: 20, background: passed ? 'var(--success-dim)' : 'var(--danger-dim)',
          borderRadius: 'var(--radius)', border: `1px solid ${passed ? 'rgba(34,197,94,.3)' : 'rgba(239,68,68,.3)'}`,
        }}>
          <div style={{ fontSize: 48 }}>{passed ? '🎉' : '📝'}</div>
          <div style={{ fontSize: 28, fontWeight: 900, color: passed ? 'var(--success)' : 'var(--danger)' }}>
            {result.score}/{result.max_score}
          </div>
          <div style={{ fontSize: 20, fontWeight: 700, color: passed ? 'var(--success)' : 'var(--danger)' }}>
            {pct}%
          </div>
          <div style={{ fontSize: 14, marginTop: 6, fontWeight: 600 }}>
            {passed
              ? (lang === 'uz' ? '✅ Ajoyib! Imtihon uchun tayyor.' : '✅ Отлично! Готов к экзамену.')
              : (lang === 'uz' ? '💪 Yana mashq qiling.' : '💪 Нужно ещё потренироваться.')}
          </div>
        </div>

        {/* Per-question results */}
        <div style={{ fontSize: 13, fontWeight: 700, marginBottom: 12 }}>
          {lang === 'uz' ? "Natijalar tahlili:" : "Разбор ответов:"}
        </div>
        {result.question_results.map((qr, i) => (
          <div key={i} style={{
            background: qr.is_correct ? 'rgba(34,197,94,.05)' : 'rgba(239,68,68,.05)',
            border: `1px solid ${qr.is_correct ? 'rgba(34,197,94,.2)' : 'rgba(239,68,68,.2)'}`,
            borderRadius: 'var(--radius-sm)', padding: 12, marginBottom: 8,
          }}>
            <div style={{ display: 'flex', gap: 8, alignItems: 'flex-start', marginBottom: 6 }}>
              <span style={{ fontSize: 16 }}>{qr.is_correct ? '✅' : '❌'}</span>
              <span style={{ fontSize: 13, fontWeight: 600 }}>{qr.question_text}</span>
            </div>
            <div style={{ fontSize: 12, marginLeft: 24 }}>
              {!qr.is_correct && (
                <div style={{ color: 'var(--danger)', marginBottom: 2 }}>
                  {lang === 'uz' ? "Sizning javobingiz:" : "Ваш ответ:"} <strong>{qr.user_answer || '—'}</strong>
                </div>
              )}
              <div style={{ color: 'var(--success)' }}>
                {lang === 'uz' ? "To'g'ri javob:" : "Правильный ответ:"} <strong>{qr.correct_answer}</strong>
              </div>
              {(qr.explanation_ru || qr.explanation_uz) && (
                <div style={{ color: 'var(--tg-hint)', marginTop: 4, fontStyle: 'italic' }}>
                  💬 {lang === 'uz' ? qr.explanation_uz : qr.explanation_ru}
                </div>
              )}
            </div>
          </div>
        ))}

        <div style={{ display: 'flex', gap: 10, marginTop: 16 }}>
          <button className="btn btn-secondary" style={{ flex: 1 }}
            onClick={() => { setResult(null); setAnswers({}) }}>
            🔄 {lang === 'uz' ? "Qayta" : "Повторить"}
          </button>
          <button className="btn btn-primary" style={{ flex: 1 }}
            onClick={() => navigate(sectionPath)}>
            {lang === 'uz' ? "Ro'yxatga qaytish" : "К списку"}
          </button>
        </div>
      </div>
    )
  }

  // ── Task screen ────────────────────────────────────────────────────────────
  return (
    <div className="page">
      {/* Top bar */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 16 }}>
        <button onClick={() => navigate(sectionPath)}
          style={{ background: 'none', color: 'var(--tg-hint)', fontSize: 13, padding: 0 }}>
          ← {lang === 'uz' ? 'Chiqish' : 'Выйти'}
        </button>
        <Timer seconds={20 * 60} onExpire={() => {}} />
      </div>

      {/* Task title */}
      <div style={{ marginBottom: 12 }}>
        <div style={{ fontSize: 17, fontWeight: 800, marginBottom: 4 }}>
          {lang === 'uz' ? (task.title_ru || task.title_de) : (task.title_ru || task.title_de)}
        </div>
        <div style={{ fontSize: 12, color: 'var(--tg-hint)' }}>
          {lang === 'uz' ? task.instruction_uz : (task.instruction_ru || task.instruction_de)}
        </div>
      </div>

      {/* Text content */}
      {task.text_content && (
        <div style={{ marginBottom: 16 }}>
          <button
            onClick={() => setShowText(!showText)}
            style={{
              background: 'none', color: 'var(--accent)',
              fontSize: 12, fontWeight: 700, padding: '4px 0', marginBottom: 8,
            }}
          >
            {showText ? '▼' : '▶'} {lang === 'uz' ? "Matnni ko'rsatish" : "Показать текст"}
          </button>
          {showText && (
            <div style={{
              background: 'rgba(59,130,246,.06)', border: '1px solid rgba(59,130,246,.15)',
              borderRadius: 'var(--radius-sm)', padding: 14,
              fontSize: 13, lineHeight: 1.7, color: 'var(--tg-text)',
              whiteSpace: 'pre-wrap',
            }}>
              {task.text_content}
            </div>
          )}
        </div>
      )}

      {/* Questions */}
      <div style={{ fontSize: 12, fontWeight: 700, color: 'var(--tg-hint)', letterSpacing: 1, textTransform: 'uppercase', marginBottom: 10 }}>
        {lang === 'uz' ? "Savollar" : "Вопросы"} ({task.questions.length})
      </div>

      {task.questions.map((q, qi) => (
        <div key={q.id} style={{
          background: 'var(--card-bg)', border: '1px solid var(--card-border)',
          borderRadius: 'var(--radius-sm)', padding: 12, marginBottom: 10,
        }}>
          <div style={{ fontSize: 13, fontWeight: 600, marginBottom: 10 }}>
            {qi + 1}. {q.question_text}
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
            {q.options.map((opt, oi) => {
              const selected = answers[q.id] === opt.option_text
              return (
                <button
                  key={oi}
                  onClick={() => handleSelect(q.id, opt.option_text)}
                  style={{
                    textAlign: 'left', padding: '10px 12px', borderRadius: 8,
                    fontSize: 13, fontWeight: selected ? 700 : 400,
                    background: selected ? 'var(--accent-dim)' : 'rgba(255,255,255,.04)',
                    border: `2px solid ${selected ? 'var(--accent)' : 'transparent'}`,
                    color: selected ? 'var(--accent)' : 'var(--tg-text)',
                    transition: 'all .15s',
                  }}
                >
                  {opt.option_text}
                </button>
              )
            })}
          </div>
        </div>
      ))}

      {/* Submit */}
      <div style={{ marginTop: 16 }}>
        <div style={{ fontSize: 11, color: 'var(--tg-hint)', textAlign: 'center', marginBottom: 10 }}>
          {Object.keys(answers).length}/{task.questions.length} {lang === 'uz' ? "savolga javob berildi" : "вопросов отвечено"}
        </div>
        <button
          className="btn btn-primary"
          disabled={!allAnswered || submitting}
          onClick={handleSubmit}
          style={{ opacity: allAnswered ? 1 : 0.4 }}
        >
          {submitting
            ? (lang === 'uz' ? "Tekshirilmoqda..." : "Проверяем...")
            : (lang === 'uz' ? "Natijani ko'rish →" : "Посмотреть результат →")}
        </button>
      </div>
    </div>
  )
}
