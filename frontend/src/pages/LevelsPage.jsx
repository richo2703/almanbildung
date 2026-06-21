import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { api } from '../api'

const LEVEL_COLORS = {
  'A1.1': ['#3B82F6','#DBEAFE'],
  'A1.2': ['#8B5CF6','#EDE9FE'],
  'A2.1': ['#10B981','#D1FAE5'],
  'A2.2': ['#F59E0B','#FEF3C7'],
  'B1.1': ['#EF4444','#FEE2E2'],
  'B1.2': ['#EC4899','#FCE7F3'],
}

export default function LevelsPage() {
  const [levels, setLevels] = useState([])
  const [user, setUser] = useState(null)
  const navigate = useNavigate()

  useEffect(() => {
    api.getLevels().then(setLevels)
    api.getMe().then(setUser).catch(() => {})
  }, [])

  return (
    <div className="page">
      <div className="page-header">
        <h1>Выбери уровень</h1>
      </div>

      {levels.map(lvl => {
        const [fg, bg] = LEVEL_COLORS[lvl.id] || ['#3B82F6','#DBEAFE']
        const done = user?.levels?.[lvl.id]?.lessons_done ?? 0
        const total = lvl.total_lessons
        const pct = total ? Math.round((done / total) * 100) : 0

        return (
          <div key={lvl.id} className="card"
            style={{ cursor: 'pointer', marginBottom: 10 }}
            onClick={() => navigate(`/learn/${lvl.id}`)}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
              <div className="level-icon" style={{ background: bg, color: fg }}>
                {lvl.id}
              </div>
              <div style={{ flex: 1 }}>
                <div style={{ fontWeight: 700, fontSize: 16 }}>{lvl.id}</div>
                <div style={{ color: 'var(--tg-hint)', fontSize: 13 }}>{lvl.title_ru}</div>
              </div>
              <div style={{ textAlign: 'right' }}>
                <div style={{ fontWeight: 700, color: fg }}>{pct}%</div>
                <div style={{ fontSize: 12, color: 'var(--tg-hint)' }}>{done}/{total}</div>
              </div>
            </div>
            <div className="progress-bar" style={{ marginTop: 10 }}>
              <div className="progress-bar-fill" style={{ width: `${pct}%`, background: fg }} />
            </div>
          </div>
        )
      })}
    </div>
  )
}
