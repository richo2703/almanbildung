import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api } from '../api'

export default function LessonsPage() {
  const { level } = useParams()
  const navigate = useNavigate()
  const [lessons, setLessons] = useState([])
  const [progress, setProgress] = useState({})

  useEffect(() => {
    api.getLessons(level).then(setLessons)
    api.getLevelProgress(level)
      .then(p => {
        const map = {}
        p.lessons.forEach(l => { map[l.lesson_id] = l })
        setProgress(map)
      })
      .catch(() => {})
  }, [level])

  return (
    <div className="page">
      <div className="page-header">
        <button className="back-btn" onClick={() => navigate('/learn')}>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none"
            stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="15 18 9 12 15 6"/>
          </svg>
        </button>
        <h1>Уровень {level}</h1>
      </div>

      {lessons.map(l => {
        const p = progress[l.id]
        const done = p?.completed === 1

        return (
          <div key={l.id} className="card card-row"
            style={{ cursor: 'pointer', marginBottom: 10, opacity: 1 }}
            onClick={() => navigate(`/lesson/${level}/${l.id}`)}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 12, flex: 1 }}>
              <div style={{
                width: 40, height: 40, borderRadius: 10,
                background: done ? '#F0FDF4' : 'var(--tg-bg)',
                border: `2px solid ${done ? 'var(--success)' : 'rgba(0,0,0,.1)'}`,
                display: 'flex', alignItems: 'center', justifyContent: 'center',
                fontWeight: 700, fontSize: 14,
                color: done ? 'var(--success)' : 'var(--tg-hint)',
                flexShrink: 0,
              }}>
                {done ? '✓' : l.id}
              </div>
              <div style={{ flex: 1, minWidth: 0 }}>
                <div style={{ fontWeight: 600, fontSize: 15 }}>{l.title_de}</div>
                <div style={{ color: 'var(--tg-hint)', fontSize: 13, overflow: 'hidden', whiteSpace: 'nowrap', textOverflow: 'ellipsis' }}>
                  {l.title_ru}
                </div>
              </div>
            </div>
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-end', gap: 4, flexShrink: 0 }}>
              <span style={{ fontSize: 12, color: 'var(--tg-hint)' }}>
                📝 {l.vocab_count}
              </span>
              <span style={{ fontSize: 12, color: 'var(--tg-hint)' }}>
                ✅ {l.exercise_count}
              </span>
            </div>
          </div>
        )
      })}
    </div>
  )
}
