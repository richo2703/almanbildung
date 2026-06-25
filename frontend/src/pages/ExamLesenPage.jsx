import { useState, useEffect } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api } from '../api'
import { useLang } from '../LangContext'

export default function ExamLesenPage() {
  const { provider, level } = useParams()
  const navigate = useNavigate()
  const { lang } = useLang()
  const [section, setSection] = useState(null)
  const [tasks, setTasks] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    api.exam.getSection(provider, level, 'lesen')
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
        <span style={{ fontSize: 24 }}>📖</span>
        <div>
          <div style={{ fontSize: 20, fontWeight: 800 }}>Lesen</div>
          <div style={{ fontSize: 13, color: 'var(--tg-hint)' }}>
            {lang === 'uz' ? "O'qish bo'limi" : "Раздел чтения"} · {section?.duration_minutes || 20} {lang === 'uz' ? "daqiqa" : "минут"}
          </div>
        </div>
      </div>

      <div style={{
        background: 'rgba(59,130,246,.08)', border: '1px solid rgba(59,130,246,.2)',
        borderRadius: 10, padding: '10px 14px', marginBottom: 20, fontSize: 12, color: 'var(--tg-hint)', lineHeight: 1.5
      }}>
        📌 {lang === 'uz'
          ? "Har bir topshiriq uchun vaqt hisoblanadi. Imtihon sharoitida mashq qiling."
          : "Каждое задание засекается по времени. Тренируйтесь в условиях экзамена."}
      </div>

      {tasks.length === 0 ? (
        <div style={{ textAlign: 'center', color: 'var(--tg-hint)', padding: 40 }}>
          {lang === 'uz' ? "Topshiriqlar yo'q" : "Задания отсутствуют"}
        </div>
      ) : (
        tasks.map((task, i) => {
          const best = task.best_attempt
          const pct = best ? Math.round(best.percentage) : null
          const typeLabel = task.task_type === 'truefalse'
            ? 'Richtig / Falsch'
            : task.task_type === 'choice'
              ? 'Multiple Choice'
              : task.task_type

          return (
            <button
              key={task.id}
              onClick={() => navigate(`/exam/${provider}/${level}/lesen/${task.id}`)}
              style={{
                width: '100%', textAlign: 'left',
                background: 'var(--card-bg)', border: '1px solid var(--card-border)',
                borderRadius: 'var(--radius)', padding: 14, marginBottom: 12,
              }}
            >
              <div style={{ display: 'flex', alignItems: 'flex-start', gap: 12 }}>
                <div style={{
                  width: 36, height: 36, borderRadius: 8,
                  background: 'var(--accent-dim)', color: 'var(--accent)',
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  fontWeight: 800, fontSize: 14, flexShrink: 0,
                }}>
                  {i + 1}
                </div>
                <div style={{ flex: 1 }}>
                  <div style={{ fontWeight: 700, fontSize: 14, marginBottom: 4 }}>
                    {lang === 'uz' ? (task.title_ru || task.title_de) : (task.title_ru || task.title_de)}
                  </div>
                  <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap', alignItems: 'center' }}>
                    <span style={{
                      background: 'rgba(59,130,246,.1)', color: 'var(--accent)',
                      borderRadius: 6, padding: '2px 7px', fontSize: 11, fontWeight: 600,
                    }}>{typeLabel}</span>
                    {pct !== null && (
                      <span style={{
                        background: pct >= 60 ? 'var(--success-dim)' : 'var(--warning-dim)',
                        color: pct >= 60 ? 'var(--success)' : 'var(--warning)',
                        borderRadius: 6, padding: '2px 7px', fontSize: 11, fontWeight: 700,
                      }}>
                        {pct >= 60 ? '✅' : '⚡'} {pct}%
                      </span>
                    )}
                  </div>
                  {lang === 'uz'
                    ? <div style={{ fontSize: 11, color: 'var(--tg-hint)', marginTop: 4 }}>{task.instruction_uz || task.instruction_ru}</div>
                    : <div style={{ fontSize: 11, color: 'var(--tg-hint)', marginTop: 4 }}>{task.instruction_ru || task.instruction_de}</div>}
                </div>
                <div style={{ fontSize: 18, color: 'var(--tg-hint)', flexShrink: 0 }}>→</div>
              </div>
            </button>
          )
        })
      )}

      <div style={{ textAlign: 'center', marginTop: 8, fontSize: 11, color: 'var(--tg-hint)' }}>
        {lang === 'uz'
          ? "Barcha topshiriqlarni bajaring va natijangizni kuzating."
          : "Выполните все задания и отслеживайте свой прогресс."}
      </div>
    </div>
  )
}
