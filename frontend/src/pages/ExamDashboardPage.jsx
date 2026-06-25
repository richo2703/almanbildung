import { useState, useEffect } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api } from '../api'
import { useLang } from '../LangContext'

const SECTION_META = {
  lesen:     { emoji: '📖', color: '#3B82F6', en: 'Lesen' },
  hoeren:    { emoji: '🎧', color: '#A855F7', en: 'Hören' },
  schreiben: { emoji: '✍️', color: '#22C55E', en: 'Schreiben' },
  sprechen:  { emoji: '🗣️', color: '#F59E0B', en: 'Sprechen' },
  grammatik: { emoji: '📚', color: '#EF4444', en: 'Grammatik' },
}

function ProgressRing({ pct, color, size = 40 }) {
  const r = (size / 2) - 4
  const circ = 2 * Math.PI * r
  const fill = (pct / 100) * circ
  return (
    <svg width={size} height={size} style={{ transform: 'rotate(-90deg)' }}>
      <circle cx={size/2} cy={size/2} r={r} fill="none" stroke="rgba(255,255,255,.08)" strokeWidth={4} />
      <circle cx={size/2} cy={size/2} r={r} fill="none" stroke={color} strokeWidth={4}
        strokeDasharray={`${fill} ${circ}`} strokeLinecap="round"
        style={{ transition: 'stroke-dasharray .5s' }} />
    </svg>
  )
}

export default function ExamDashboardPage() {
  const { provider, level } = useParams()
  const navigate = useNavigate()
  const { lang } = useLang()
  const [levelInfo, setLevelInfo] = useState(null)
  const [sections, setSections] = useState([])
  const [progress, setProgress] = useState({})
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    Promise.all([
      api.exam.getLevelInfo(provider, level),
      api.exam.getSections(provider, level),
      api.exam.getProgress(provider, level).catch(() => ({})),
    ]).then(([info, secs, prog]) => {
      setLevelInfo(info)
      setSections(secs)
      setProgress(prog)
    }).catch(() => {}).finally(() => setLoading(false))
  }, [provider, level])

  const overallPct = Object.values(progress).length
    ? Math.round(Object.values(progress).reduce((s, p) => s + (p.average_score || 0), 0) / Object.values(progress).length)
    : 0

  if (loading) return <div className="page" style={{ textAlign: 'center', paddingTop: 80, color: 'var(--tg-hint)' }}>...</div>

  return (
    <div className="page">
      <button onClick={() => navigate(`/exam/${provider}`)}
        style={{ background: 'none', color: 'var(--tg-hint)', fontSize: 13, marginBottom: 16, padding: 0 }}>
        ← {lang === 'uz' ? 'Orqaga' : 'Назад'}
      </button>

      {/* Header */}
      <div style={{
        background: 'linear-gradient(135deg, rgba(59,130,246,.15), rgba(168,85,247,.1))',
        border: '1px solid rgba(59,130,246,.2)',
        borderRadius: 'var(--radius)', padding: 16, marginBottom: 20,
      }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div>
            <div style={{ fontSize: 13, color: 'var(--tg-hint)', marginBottom: 2 }}>
              {levelInfo?.provider_title || provider}
            </div>
            <div style={{ fontSize: 24, fontWeight: 900 }}>{level}</div>
            <div style={{ fontSize: 13, color: 'var(--tg-hint)' }}>{levelInfo?.title}</div>
          </div>
          <div style={{ textAlign: 'center' }}>
            <ProgressRing pct={overallPct} color="var(--accent)" size={56} />
            <div style={{ fontSize: 11, color: 'var(--tg-hint)', marginTop: 2 }}>{overallPct}%</div>
          </div>
        </div>

        <div style={{ marginTop: 12, display: 'flex', gap: 8 }}>
          <button
            onClick={() => navigate(`/exam/${provider}/${level}/info`)}
            style={{
              flex: 1, background: 'rgba(59,130,246,.15)', border: '1px solid rgba(59,130,246,.3)',
              color: 'var(--accent)', borderRadius: 8, padding: '8px 12px', fontSize: 12, fontWeight: 700,
            }}
          >
            ℹ️ {lang === 'uz' ? "Imtihon haqida" : "Об экзамене"}
          </button>
          <div style={{
            flex: 1, background: 'rgba(255,255,255,.05)', border: '1px solid var(--card-border)',
            borderRadius: 8, padding: '8px 12px', fontSize: 11, color: 'var(--tg-hint)',
            textAlign: 'center', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 4
          }}>
            ⏱ {levelInfo?.duration_total || '–'}
          </div>
        </div>
      </div>

      {/* Sections */}
      <div style={{ fontSize: 12, fontWeight: 700, color: 'var(--tg-hint)', letterSpacing: 1, textTransform: 'uppercase', marginBottom: 12 }}>
        {lang === 'uz' ? "Bo'limlar" : "Разделы"}
      </div>

      {sections.map(sec => {
        const meta = SECTION_META[sec.type] || { emoji: '📝', color: 'var(--accent)' }
        const prog = progress[sec.type] || {}
        const pct = Math.round(prog.average_score || 0)
        const done = prog.completed_tasks || 0
        const total = prog.total_tasks || 0
        const isAvailable = sec.type === 'lesen' || sec.type === 'schreiben'
        const status = done > 0 ? 'in_progress' : 'not_started'

        return (
          <button
            key={sec.id}
            onClick={() => {
              if (!isAvailable) return
              navigate(`/exam/${provider}/${level}/${sec.type}`)
            }}
            style={{
              width: '100%', textAlign: 'left',
              background: 'var(--card-bg)',
              border: `1px solid ${isAvailable ? 'var(--card-border)' : 'rgba(255,255,255,.04)'}`,
              borderRadius: 'var(--radius)',
              padding: 14, marginBottom: 10,
              opacity: isAvailable ? 1 : 0.5,
            }}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
              <div style={{
                width: 42, height: 42, borderRadius: 10,
                background: meta.color + '20',
                display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 20,
                flexShrink: 0,
              }}>
                {meta.emoji}
              </div>

              <div style={{ flex: 1 }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 2 }}>
                  <span style={{ fontWeight: 700, fontSize: 15 }}>{sec.title_de}</span>
                  {lang === 'uz'
                    ? <span style={{ fontSize: 12, color: 'var(--tg-hint)' }}>{sec.title_uz}</span>
                    : <span style={{ fontSize: 12, color: 'var(--tg-hint)' }}>{sec.title_ru}</span>}
                </div>
                <div style={{ fontSize: 11, color: 'var(--tg-hint)' }}>
                  ⏱ {sec.duration_minutes} {lang === 'uz' ? 'daq' : 'мин'}
                  {total > 0 && <> · {done}/{total} {lang === 'uz' ? "topshiriq" : "задания"}</>}
                </div>
              </div>

              <div style={{ textAlign: 'right', flexShrink: 0 }}>
                {!isAvailable ? (
                  <span style={{ fontSize: 10, color: 'var(--tg-hint)', fontWeight: 600 }}>
                    {lang === 'uz' ? 'Tez kunda' : 'Скоро'}
                  </span>
                ) : pct > 0 ? (
                  <div>
                    <div style={{ fontSize: 16, fontWeight: 800, color: meta.color }}>{pct}%</div>
                    <div style={{ fontSize: 10, color: 'var(--tg-hint)' }}>
                      {pct >= 60
                        ? (lang === 'uz' ? '✅ Tayyor' : '✅ Готов')
                        : (lang === 'uz' ? '📝 Mashq' : '📝 Практика')}
                    </div>
                  </div>
                ) : (
                  <span style={{ fontSize: 18, color: 'var(--tg-hint)' }}>→</span>
                )}
              </div>
            </div>

            {pct > 0 && (
              <div className="progress-bar" style={{ marginTop: 8 }}>
                <div className="progress-bar-fill" style={{ width: `${pct}%`, background: meta.color }} />
              </div>
            )}
          </button>
        )
      })}

      {/* Tips */}
      {(levelInfo?.tips_ru || levelInfo?.tips_uz) && (
        <div style={{
          marginTop: 8, background: 'rgba(245,158,11,.06)', border: '1px solid rgba(245,158,11,.2)',
          borderRadius: 'var(--radius)', padding: 14,
        }}>
          <div style={{ fontSize: 13, fontWeight: 700, marginBottom: 6 }}>💡 {lang === 'uz' ? 'Maslahat' : 'Советы'}</div>
          <div style={{ fontSize: 12, color: 'var(--tg-hint)', lineHeight: 1.6 }}>
            {lang === 'uz' ? levelInfo.tips_uz : levelInfo.tips_ru}
          </div>
        </div>
      )}
    </div>
  )
}
