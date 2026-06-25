import { useState, useEffect } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api } from '../api'
import { useLang } from '../LangContext'

const TASK_TYPE_LABEL = {
  writing_form: { de: 'Formular', emoji: '📋' },
  writing_free: { de: 'Kurzmitteilung', emoji: '✉️' },
}

export default function ExamSchreibenListPage() {
  const { provider, level } = useParams()
  const navigate = useNavigate()
  const { lang } = useLang()
  const [section, setSection] = useState(null)
  const [tasks, setTasks] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    api.exam.getSection(provider, level, 'schreiben')
      .then(sec => {
        setSection(sec)
        return api.exam.getTasks(sec.id)
      })
      .then(t => setTasks(t))
      .catch(() => {})
      .finally(() => setLoading(false))
  }, [provider, level])

  if (loading) return <div className="page" style={{ color: 'var(--tg-hint)', textAlign: 'center', paddingTop: 60 }}>...</div>

  return (
    <div className="page">
      <button onClick={() => navigate(`/exam/${provider}/${level}`)}
        style={{ background: 'none', color: 'var(--tg-hint)', fontSize: 13, marginBottom: 20, padding: 0 }}>
        ← {lang === 'uz' ? 'Orqaga' : 'Назад'}
      </button>

      <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 6 }}>
        <span style={{ fontSize: 24 }}>✍️</span>
        <div>
          <div style={{ fontSize: 20, fontWeight: 800 }}>Schreiben</div>
          <div style={{ fontSize: 13, color: 'var(--tg-hint)' }}>
            {lang === 'uz' ? "Yozish bo'limi" : "Раздел письма"} · {section?.duration_minutes || 10} {lang === 'uz' ? "daqiqa" : "минут"}
          </div>
        </div>
      </div>

      <div style={{
        background: 'rgba(34,197,94,.08)', border: '1px solid rgba(34,197,94,.2)',
        borderRadius: 10, padding: '10px 14px', marginBottom: 20, fontSize: 12, color: 'var(--tg-hint)', lineHeight: 1.5
      }}>
        ✍️ {lang === 'uz'
          ? "Yozishni mashq qiling. Namunaviy javob bilan solishtiring."
          : "Тренируйте письменную речь. Сравнивайте с примером хорошего ответа."}
      </div>

      {tasks.length === 0 ? (
        <div style={{ textAlign: 'center', color: 'var(--tg-hint)', padding: 40 }}>
          {lang === 'uz' ? "Topshiriqlar yo'q" : "Задания отсутствуют"}
        </div>
      ) : (
        tasks.map((task, i) => {
          const meta = TASK_TYPE_LABEL[task.task_type] || { de: task.task_type, emoji: '📝' }
          return (
            <button
              key={task.id}
              onClick={() => navigate(`/exam/${provider}/${level}/schreiben/${task.id}`)}
              style={{
                width: '100%', textAlign: 'left',
                background: 'var(--card-bg)', border: '1px solid var(--card-border)',
                borderRadius: 'var(--radius)', padding: 14, marginBottom: 12,
              }}
            >
              <div style={{ display: 'flex', alignItems: 'flex-start', gap: 12 }}>
                <div style={{
                  width: 36, height: 36, borderRadius: 8, flexShrink: 0,
                  background: 'rgba(34,197,94,.15)', color: 'var(--success)',
                  display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 18,
                }}>
                  {meta.emoji}
                </div>
                <div style={{ flex: 1 }}>
                  <div style={{ fontWeight: 700, fontSize: 14, marginBottom: 4 }}>
                    {lang === 'uz' ? (task.title_ru || task.title_de) : (task.title_ru || task.title_de)}
                  </div>
                  <div style={{ display: 'flex', gap: 6, alignItems: 'center', marginBottom: 4 }}>
                    <span style={{
                      background: 'rgba(34,197,94,.1)', color: 'var(--success)',
                      borderRadius: 6, padding: '2px 7px', fontSize: 11, fontWeight: 600,
                    }}>{meta.de}</span>
                  </div>
                  <div style={{ fontSize: 11, color: 'var(--tg-hint)' }}>
                    {lang === 'uz' ? task.instruction_uz : (task.instruction_ru || task.instruction_de)}
                  </div>
                </div>
                <div style={{ fontSize: 18, color: 'var(--tg-hint)', flexShrink: 0 }}>→</div>
              </div>
            </button>
          )
        })
      )}
    </div>
  )
}
