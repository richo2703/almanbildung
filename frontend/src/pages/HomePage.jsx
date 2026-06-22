import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { api } from '../api'
import { useLang } from '../LangContext'

const LEVEL_COLORS = {
  'A1.1': ['#3B82F6', '#1d4ed8'],
  'A1.2': ['#8B5CF6', '#6d28d9'],
  'A2.1': ['#10B981', '#059669'],
  'A2.2': ['#F59E0B', '#d97706'],
  'B1.1': ['#EF4444', '#dc2626'],
  'B1.2': ['#EC4899', '#db2777'],
}

export default function HomePage() {
  const [user, setUser] = useState(null)
  const [levels, setLevels] = useState([])
  const navigate = useNavigate()
  const { t, lang } = useLang()

  useEffect(() => {
    Promise.all([api.getMe(), api.getLevels()]).then(([me, lvls]) => {
      setUser(me)
      setLevels(lvls)
    }).catch(() => api.getLevels().then(setLevels))
  }, [])

  const tgUser = window.Telegram?.WebApp?.initDataUnsafe?.user
  const name = tgUser?.first_name || (lang === 'uz' ? 'Talaba' : 'Ученик')
  const xp = user?.xp ?? 0

  // Find first incomplete level
  const nextLevel = levels.find(lvl => {
    const done = user?.levels?.[lvl.id]?.lessons_done ?? 0
    return done < lvl.total_lessons
  })

  return (
    <div className="page">
      {/* Header */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 24 }}>
        <div>
          <div style={{ fontSize: 13, color: 'var(--tg-hint)', marginBottom: 2 }}>
            {t.greeting}, {name} 👋
          </div>
          <h1 style={{ fontSize: 24, fontWeight: 800 }}>Alman Bildung</h1>
        </div>
        <div className="xp-chip">⭐ {xp} XP</div>
      </div>

      {/* Continue learning */}
      {nextLevel && (
        <>
          <div className="section-title">{lang === 'uz' ? 'Davom eting' : 'Продолжить'}</div>
          <div
            onClick={() => navigate(`/learn/${nextLevel.id}`)}
            style={{
              background: `linear-gradient(135deg, ${LEVEL_COLORS[nextLevel.id]?.[0]}22, ${LEVEL_COLORS[nextLevel.id]?.[1]}33)`,
              border: `1px solid ${LEVEL_COLORS[nextLevel.id]?.[0]}44`,
              borderRadius: 18,
              padding: '20px',
              marginBottom: 24,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: 16,
            }}>
            <div style={{
              width: 56, height: 56,
              borderRadius: 14,
              background: LEVEL_COLORS[nextLevel.id]?.[0],
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              fontSize: 13, fontWeight: 800, color: '#fff',
              flexShrink: 0,
            }}>
              {nextLevel.id}
            </div>
            <div style={{ flex: 1 }}>
              <div style={{ fontWeight: 700, fontSize: 16, marginBottom: 6 }}>
                {nextLevel.title_ru}
              </div>
              <div className="progress-bar">
                <div className="progress-bar-fill" style={{
                  width: `${Math.round(((user?.levels?.[nextLevel.id]?.lessons_done ?? 0) / nextLevel.total_lessons) * 100)}%`,
                  background: LEVEL_COLORS[nextLevel.id]?.[0],
                }} />
              </div>
              <div style={{ fontSize: 12, color: 'var(--tg-hint)', marginTop: 4 }}>
                {user?.levels?.[nextLevel.id]?.lessons_done ?? 0} / {nextLevel.total_lessons} {t.lessons.toLowerCase()}
              </div>
            </div>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke={LEVEL_COLORS[nextLevel.id]?.[0]} strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
              <polyline points="9 18 15 12 9 6"/>
            </svg>
          </div>
        </>
      )}

      {/* Stats row */}
      <div style={{ display: 'flex', gap: 10, marginBottom: 24 }}>
        <div className="stat-card">
          <div className="stat-value" style={{ color: 'var(--warning)' }}>⭐ {xp}</div>
          <div className="stat-label">XP</div>
        </div>
        <div className="stat-card">
          <div className="stat-value" style={{ color: 'var(--success)' }}>
            {Object.values(user?.levels || {}).reduce((s, l) => s + (l.lessons_done || 0), 0)}
          </div>
          <div className="stat-label">{t.lessons}</div>
        </div>
        <div className="stat-card">
          <div className="stat-value" style={{ color: 'var(--purple)' }}>
            {Object.values(user?.levels || {}).reduce((s, l) => s + (l.vocab_known || 0), 0)}
          </div>
          <div className="stat-label">{t.words}</div>
        </div>
      </div>

      {/* All levels */}
      <div className="section-title">{t.allLevels}</div>
      {levels.map(lvl => {
        const [c1] = LEVEL_COLORS[lvl.id] || ['#3B82F6']
        const done = user?.levels?.[lvl.id]?.lessons_done ?? 0
        const total = lvl.total_lessons
        const pct = total ? Math.round((done / total) * 100) : 0

        return (
          <div key={lvl.id} className="card card-row"
            style={{ cursor: 'pointer' }}
            onClick={() => navigate(`/learn/${lvl.id}`)}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 12, flex: 1 }}>
              <div className="level-icon" style={{ background: `${c1}22`, color: c1 }}>
                {lvl.id}
              </div>
              <div style={{ flex: 1, minWidth: 0 }}>
                <div style={{ fontWeight: 600, marginBottom: 5 }}>
                  {lang === 'uz' ? lvl.title_uz : lvl.title_ru}
                </div>
                <div className="progress-bar">
                  <div className="progress-bar-fill" style={{ width: `${pct}%`, background: c1 }} />
                </div>
                <div style={{ color: 'var(--tg-hint)', fontSize: 12, marginTop: 3 }}>
                  {done}/{total} {t.lessons.toLowerCase()}
                </div>
              </div>
              <div style={{ fontWeight: 800, color: c1, fontSize: 15 }}>{pct}%</div>
            </div>
          </div>
        )
      })}
    </div>
  )
}
