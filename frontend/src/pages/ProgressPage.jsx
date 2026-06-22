import { useEffect, useState } from 'react'
import { api } from '../api'
import { useLang } from '../LangContext'

const LEVEL_COLORS = {
  'A1.1': '#3B82F6', 'A1.2': '#8B5CF6',
  'A2.1': '#10B981', 'A2.2': '#F59E0B',
  'B1.1': '#EF4444', 'B1.2': '#EC4899',
}
const TOTAL = 8

export default function ProgressPage() {
  const [stats, setStats] = useState(null)
  const { t, lang } = useLang()

  useEffect(() => {
    api.getMe().then(setStats).catch(() => {})
  }, [])

  if (!stats) return <div className="loading"><div className="spinner" /></div>

  const levels = stats.levels || {}
  const totalDone = Object.values(levels).reduce((s, l) => s + (l.lessons_done || 0), 0)
  const totalAll = Object.keys(levels).length * TOTAL
  const totalVocab = Object.values(levels).reduce((s, l) => s + (l.vocab_known || 0), 0)
  const xp = stats.xp || 0

  return (
    <div className="page">
      <div className="page-header">
        <h1>{t.progress}</h1>
      </div>

      {/* XP hero */}
      <div style={{
        background: 'linear-gradient(135deg, rgba(245,158,11,.15), rgba(239,68,68,.1))',
        border: '1px solid rgba(245,158,11,.2)',
        borderRadius: 18,
        padding: '24px',
        textAlign: 'center',
        marginBottom: 20,
      }}>
        <div style={{ fontSize: 48, fontWeight: 900, color: 'var(--warning)' }}>⭐ {xp}</div>
        <div style={{ fontSize: 14, color: 'var(--tg-hint)', marginTop: 4 }}>XP</div>
      </div>

      {/* Stats */}
      <div style={{ display: 'flex', gap: 10, marginBottom: 24 }}>
        <div className="stat-card">
          <div className="stat-value" style={{ color: 'var(--success)' }}>{totalDone}</div>
          <div className="stat-label">{t.completedLessons}</div>
        </div>
        <div className="stat-card">
          <div className="stat-value" style={{ color: 'var(--purple)' }}>{totalVocab}</div>
          <div className="stat-label">{t.knownWords}</div>
        </div>
        <div className="stat-card">
          <div className="stat-value" style={{ color: 'var(--accent)' }}>
            {totalAll ? Math.round((totalDone / totalAll) * 100) : 0}%
          </div>
          <div className="stat-label">{lang === 'uz' ? 'Jami' : 'Итого'}</div>
        </div>
      </div>

      {/* Total bar */}
      <div className="card" style={{ marginBottom: 6 }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 10 }}>
          <span style={{ fontWeight: 700 }}>{lang === 'uz' ? 'Umumiy progress' : 'Общий прогресс'}</span>
          <span style={{ color: 'var(--tg-hint)', fontSize: 13 }}>{totalDone}/{totalAll}</span>
        </div>
        <div className="progress-bar" style={{ height: 8 }}>
          <div className="progress-bar-fill"
            style={{ width: `${totalAll ? Math.round((totalDone / totalAll) * 100) : 0}%` }} />
        </div>
      </div>

      {/* Per level */}
      <div className="section-title">{t.allLevels}</div>
      {Object.entries(levels).map(([lvl, data]) => {
        const color = LEVEL_COLORS[lvl] || '#3B82F6'
        const done = data.lessons_done || 0
        const pct = Math.round((done / TOTAL) * 100)

        return (
          <div key={lvl} className="card" style={{ marginBottom: 10 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 10 }}>
              <div className="level-icon" style={{ background: `${color}22`, color, width: 38, height: 38, fontSize: 11 }}>
                {lvl}
              </div>
              <div style={{ flex: 1 }}>
                <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                  <span style={{ fontWeight: 700 }}>{lvl}</span>
                  <span style={{ fontWeight: 800, color }}>{pct}%</span>
                </div>
              </div>
            </div>
            <div className="progress-bar">
              <div className="progress-bar-fill" style={{ width: `${pct}%`, background: color }} />
            </div>
            <div style={{ display: 'flex', gap: 16, marginTop: 8 }}>
              <span style={{ fontSize: 12, color: 'var(--tg-hint)' }}>
                📚 {done}/{TOTAL} {t.lessons.toLowerCase()}
              </span>
              <span style={{ fontSize: 12, color: 'var(--tg-hint)' }}>
                📝 {data.vocab_known || 0} {t.words.toLowerCase()}
              </span>
            </div>
          </div>
        )
      })}
    </div>
  )
}
