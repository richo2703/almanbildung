import { useEffect, useState } from 'react'
import { api } from '../api'

const LEVEL_COLORS = {
  'A1.1': ['#3B82F6','#DBEAFE'],
  'A1.2': ['#8B5CF6','#EDE9FE'],
  'A2.1': ['#10B981','#D1FAE5'],
  'A2.2': ['#F59E0B','#FEF3C7'],
  'B1.1': ['#EF4444','#FEE2E2'],
  'B1.2': ['#EC4899','#FCE7F3'],
}

const TOTAL_PER_LEVEL = 8

export default function ProgressPage() {
  const [stats, setStats] = useState(null)

  useEffect(() => {
    api.getMe().then(me => setStats(me)).catch(() => {})
  }, [])

  if (!stats) return <div className="loading">Загрузка...</div>

  const levels = stats.levels || {}
  const totalDone = Object.values(levels).reduce((s, l) => s + (l.lessons_done || 0), 0)
  const totalAll = Object.keys(levels).length * TOTAL_PER_LEVEL
  const totalVocab = Object.values(levels).reduce((s, l) => s + (l.vocab_known || 0), 0)

  return (
    <div className="page">
      <div className="page-header">
        <h1>Прогресс</h1>
      </div>

      {/* Summary */}
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: 10, marginBottom: 24 }}>
        <div className="card" style={{ textAlign: 'center' }}>
          <div style={{ fontSize: 22, fontWeight: 800, color: 'var(--accent)' }}>{stats.xp}</div>
          <div style={{ fontSize: 12, color: 'var(--tg-hint)' }}>⭐ XP</div>
        </div>
        <div className="card" style={{ textAlign: 'center' }}>
          <div style={{ fontSize: 22, fontWeight: 800, color: 'var(--success)' }}>{totalDone}</div>
          <div style={{ fontSize: 12, color: 'var(--tg-hint)' }}>Уроков</div>
        </div>
        <div className="card" style={{ textAlign: 'center' }}>
          <div style={{ fontSize: 22, fontWeight: 800, color: '#8B5CF6' }}>{totalVocab}</div>
          <div style={{ fontSize: 12, color: 'var(--tg-hint)' }}>Слов</div>
        </div>
      </div>

      {/* Total progress */}
      <div className="section-title">Общий прогресс</div>
      <div className="card" style={{ marginBottom: 20 }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 8 }}>
          <span style={{ fontWeight: 600 }}>Все уровни</span>
          <span style={{ color: 'var(--tg-hint)' }}>{totalDone}/{totalAll} уроков</span>
        </div>
        <div className="progress-bar">
          <div className="progress-bar-fill"
            style={{ width: `${totalAll ? Math.round((totalDone/totalAll)*100) : 0}%` }} />
        </div>
      </div>

      {/* Per level */}
      <div className="section-title">По уровням</div>
      {Object.entries(levels).map(([lvl, data]) => {
        const [fg, bg] = LEVEL_COLORS[lvl] || ['#3B82F6','#DBEAFE']
        const done = data.lessons_done || 0
        const pct = Math.round((done / TOTAL_PER_LEVEL) * 100)

        return (
          <div key={lvl} className="card" style={{ marginBottom: 10 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 8 }}>
              <div className="level-icon" style={{ background: bg, color: fg, width: 36, height: 36, fontSize: 11 }}>
                {lvl}
              </div>
              <div style={{ flex: 1 }}>
                <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                  <span style={{ fontWeight: 600 }}>Уровень {lvl}</span>
                  <span style={{ fontWeight: 700, color: fg }}>{pct}%</span>
                </div>
              </div>
            </div>
            <div className="progress-bar">
              <div className="progress-bar-fill" style={{ width: `${pct}%`, background: fg }} />
            </div>
            <div style={{ display: 'flex', gap: 16, marginTop: 8 }}>
              <span style={{ fontSize: 12, color: 'var(--tg-hint)' }}>
                📚 {done}/{TOTAL_PER_LEVEL} уроков
              </span>
              <span style={{ fontSize: 12, color: 'var(--tg-hint)' }}>
                📝 {data.vocab_known || 0} слов
              </span>
            </div>
          </div>
        )
      })}
    </div>
  )
}
