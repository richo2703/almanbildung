import { useState, useEffect } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api } from '../api'
import { useLang } from '../LangContext'

const LEVEL_COLORS = { A1: '#22C55E', A2: '#3B82F6', B1: '#F59E0B', B2: '#EF4444' }
const LEVEL_ICONS  = { A1: '🌱', A2: '📗', B1: '🏆', B2: '🎓' }

export default function ExamLevelPage() {
  const { provider } = useParams()
  const navigate = useNavigate()
  const { lang } = useLang()
  const [levels, setLevels] = useState([])
  const [providerInfo, setProviderInfo] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    Promise.all([
      api.exam.getProviders(),
      api.exam.getLevels(provider),
    ]).then(([providers, lvls]) => {
      setProviderInfo(providers.find(p => p.name === provider) || null)
      setLevels(lvls)
    }).catch(() => {}).finally(() => setLoading(false))
  }, [provider])

  return (
    <div className="page">
      <button
        onClick={() => navigate('/exam')}
        style={{ background: 'none', color: 'var(--tg-hint)', fontSize: 13, marginBottom: 16, padding: 0 }}
      >
        ← {lang === 'uz' ? 'Orqaga' : 'Назад'}
      </button>

      <div style={{ marginBottom: 24 }}>
        <div style={{ fontSize: 20, fontWeight: 800, marginBottom: 4 }}>
          {providerInfo?.logo_emoji || '🎓'} {providerInfo?.title || provider}
        </div>
        <div style={{ fontSize: 13, color: 'var(--tg-hint)' }}>
          {lang === 'uz' ? 'Darajani tanlang' : 'Выберите уровень подготовки'}
        </div>
      </div>

      {loading ? (
        <div style={{ textAlign: 'center', padding: 40, color: 'var(--tg-hint)' }}>...</div>
      ) : (
        levels.map(lv => {
          const color = LEVEL_COLORS[lv.level] || 'var(--accent)'
          const icon  = LEVEL_ICONS[lv.level]  || '📘'
          return (
            <button
              key={lv.level}
              onClick={() => navigate(`/exam/${provider}/${lv.level}`)}
              style={{
                width: '100%', textAlign: 'left',
                background: 'var(--card-bg)',
                border: `1px solid var(--card-border)`,
                borderRadius: 'var(--radius)',
                padding: 16, marginBottom: 12,
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: 12, marginBottom: 8 }}>
                <div style={{
                  width: 48, height: 48, borderRadius: 12,
                  background: color + '20',
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  fontSize: 22,
                }}>
                  {icon}
                </div>
                <div>
                  <div style={{ fontWeight: 800, fontSize: 18, color }}>{lv.level}</div>
                  <div style={{ fontSize: 13, fontWeight: 600 }}>{lv.title}</div>
                </div>
                <div style={{ marginLeft: 'auto', fontSize: 18, color: 'var(--tg-hint)' }}>→</div>
              </div>

              <div style={{ fontSize: 12, color: 'var(--tg-hint)', marginBottom: 8, lineHeight: 1.5 }}>
                {lang === 'uz' ? lv.description_uz : lv.description_ru}
              </div>

              {(lv.target_audience_ru || lv.target_audience_uz) && (
                <div style={{
                  background: color + '15', borderRadius: 8, padding: '6px 10px',
                  fontSize: 11, color, fontWeight: 600, lineHeight: 1.4,
                }}>
                  👤 {lang === 'uz' ? lv.target_audience_uz : lv.target_audience_ru}
                </div>
              )}

              <div style={{ marginTop: 10, display: 'flex', gap: 8, flexWrap: 'wrap' }}>
                {(lv.exam_parts || []).map(part => (
                  <span key={part.name} style={{
                    background: 'var(--card-bg)', border: '1px solid var(--card-border)',
                    borderRadius: 6, padding: '3px 8px', fontSize: 11, color: 'var(--tg-hint)',
                  }}>
                    {part.name} · {part.duration}
                  </span>
                ))}
              </div>
            </button>
          )
        })
      )}
    </div>
  )
}
