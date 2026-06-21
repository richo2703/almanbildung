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

export default function HomePage() {
  const [user, setUser] = useState(null)
  const [levels, setLevels] = useState([])
  const navigate = useNavigate()

  useEffect(() => {
    Promise.all([api.getMe(), api.getLevels()]).then(([me, lvls]) => {
      setUser(me)
      setLevels(lvls)
    }).catch(() => {
      api.getLevels().then(setLevels)
    })
  }, [])

  const tgUser = window.Telegram?.WebApp?.initDataUnsafe?.user
  const name = tgUser?.first_name || 'Ученик'
  const xp = user?.xp ?? 0

  return (
    <div className="page">
      {/* Hero */}
      <div style={{ marginBottom: 24 }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 4 }}>
          <h1 style={{ fontSize: 22, fontWeight: 700 }}>Привет, {name}! 👋</h1>
          <div className="xp-chip">⭐ {xp} XP</div>
        </div>
        <p style={{ color: 'var(--tg-hint)', fontSize: 14 }}>Немецкий язык A1 → B1</p>
      </div>

      {/* Quick actions */}
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 10, marginBottom: 24 }}>
        <button className="card" style={{ textAlign: 'left', cursor: 'pointer' }}
          onClick={() => navigate('/learn')}>
          <div style={{ fontSize: 24, marginBottom: 6 }}>📚</div>
          <div style={{ fontWeight: 600, fontSize: 15 }}>Уроки</div>
          <div style={{ color: 'var(--tg-hint)', fontSize: 12 }}>48 тем</div>
        </button>
        <button className="card" style={{ textAlign: 'left', cursor: 'pointer' }}
          onClick={() => navigate('/progress')}>
          <div style={{ fontSize: 24, marginBottom: 6 }}>📊</div>
          <div style={{ fontWeight: 600, fontSize: 15 }}>Прогресс</div>
          <div style={{ color: 'var(--tg-hint)', fontSize: 12 }}>Статистика</div>
        </button>
      </div>

      {/* Levels overview */}
      <div className="section-title">Уровни</div>
      {levels.map(lvl => {
        const [fg, bg] = LEVEL_COLORS[lvl.id] || ['#3B82F6','#DBEAFE']
        const done = user?.levels?.[lvl.id]?.lessons_done ?? 0
        const total = lvl.total_lessons
        const pct = total ? Math.round((done / total) * 100) : 0

        return (
          <div key={lvl.id} className="card card-row"
            style={{ cursor: 'pointer' }}
            onClick={() => navigate(`/learn/${lvl.id}`)}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 12, flex: 1 }}>
              <div className="level-icon" style={{ background: bg, color: fg }}>
                {lvl.id}
              </div>
              <div style={{ flex: 1, minWidth: 0 }}>
                <div style={{ fontWeight: 600, fontSize: 15, marginBottom: 4 }}>
                  {lvl.title_ru}
                </div>
                <div className="progress-bar">
                  <div className="progress-bar-fill" style={{ width: `${pct}%`, background: fg }} />
                </div>
                <div style={{ color: 'var(--tg-hint)', fontSize: 12, marginTop: 3 }}>
                  {done}/{total} уроков
                </div>
              </div>
            </div>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none"
              stroke="var(--tg-hint)" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <polyline points="9 18 15 12 9 6"/>
            </svg>
          </div>
        )
      })}
    </div>
  )
}
