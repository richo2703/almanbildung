import { useState, useEffect } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api } from '../api'
import { useLang } from '../LangContext'

export default function ExamInfoPage() {
  const { provider, level } = useParams()
  const navigate = useNavigate()
  const { lang } = useLang()
  const [info, setInfo] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    api.exam.getLevelInfo(provider, level)
      .then(setInfo)
      .catch(() => {})
      .finally(() => setLoading(false))
  }, [provider, level])

  if (loading) return <div className="page" style={{ color: 'var(--tg-hint)', textAlign: 'center', paddingTop: 60 }}>...</div>
  if (!info) return <div className="page"><div style={{ color: 'var(--tg-hint)' }}>Not found</div></div>

  return (
    <div className="page">
      <button onClick={() => navigate(`/exam/${provider}/${level}`)}
        style={{ background: 'none', color: 'var(--tg-hint)', fontSize: 13, marginBottom: 20, padding: 0 }}>
        ← {lang === 'uz' ? 'Orqaga' : 'Назад'}
      </button>

      <div style={{ fontSize: 22, fontWeight: 900, marginBottom: 4 }}>
        {info.provider_emoji || '🎓'} {info.provider_title}
      </div>
      <div style={{ fontSize: 16, color: 'var(--tg-hint)', marginBottom: 24 }}>{info.title}</div>

      {/* About */}
      <div className="card" style={{ marginBottom: 12 }}>
        <div style={{ fontSize: 13, fontWeight: 700, marginBottom: 8, color: 'var(--accent)' }}>
          📋 {lang === 'uz' ? 'Imtihon haqida' : 'Об экзамене'}
        </div>
        <div style={{ fontSize: 13, color: 'var(--tg-hint)', lineHeight: 1.6 }}>
          {lang === 'uz' ? info.description_uz : info.description_ru}
        </div>
      </div>

      {/* Target audience */}
      {(info.target_audience_ru || info.target_audience_uz) && (
        <div className="card" style={{ marginBottom: 12 }}>
          <div style={{ fontSize: 13, fontWeight: 700, marginBottom: 8, color: '#A855F7' }}>
            👤 {lang === 'uz' ? 'Kim uchun?' : 'Для кого?'}
          </div>
          <div style={{ fontSize: 13, color: 'var(--tg-hint)', lineHeight: 1.6 }}>
            {lang === 'uz' ? info.target_audience_uz : info.target_audience_ru}
          </div>
        </div>
      )}

      {/* Exam structure */}
      {info.exam_parts?.length > 0 && (
        <div className="card" style={{ marginBottom: 12 }}>
          <div style={{ fontSize: 13, fontWeight: 700, marginBottom: 12, color: '#22C55E' }}>
            🗂 {lang === 'uz' ? "Imtihon tuzilmasi" : "Структура экзамена"}
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
            {info.exam_parts.map((part, i) => (
              <div key={i} style={{
                display: 'flex', alignItems: 'center', justifyContent: 'space-between',
                padding: '8px 10px', background: 'rgba(255,255,255,.04)', borderRadius: 8,
              }}>
                <div>
                  <span style={{ fontWeight: 700, fontSize: 14 }}>{part.name}</span>
                  {part.name_ru && (
                    <span style={{ fontSize: 12, color: 'var(--tg-hint)', marginLeft: 6 }}>
                      — {lang === 'uz' ? (part.name_uz || part.name_ru) : part.name_ru}
                    </span>
                  )}
                </div>
                <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
                  <span style={{ fontSize: 11, color: 'var(--tg-hint)' }}>⏱ {part.duration}</span>
                  {part.points && (
                    <span style={{
                      background: 'var(--accent-dim)', color: 'var(--accent)',
                      borderRadius: 6, padding: '2px 7px', fontSize: 11, fontWeight: 700,
                    }}>{part.points} Pkt.</span>
                  )}
                </div>
              </div>
            ))}
          </div>
          <div style={{ marginTop: 10, fontSize: 12, color: 'var(--tg-hint)' }}>
            ⏱ {lang === 'uz' ? "Jami vaqt:" : "Общее время:"} <strong style={{ color: 'var(--tg-text)' }}>{info.duration_total}</strong>
          </div>
        </div>
      )}

      {/* Pass score */}
      <div className="card" style={{ marginBottom: 12 }}>
        <div style={{ fontSize: 13, fontWeight: 700, marginBottom: 8, color: '#F59E0B' }}>
          🏅 {lang === 'uz' ? 'O\'tish bali' : 'Проходной балл'}
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
          <div style={{ fontSize: 32, fontWeight: 900, color: '#F59E0B' }}>{info.pass_score}%</div>
          <div style={{ fontSize: 12, color: 'var(--tg-hint)', lineHeight: 1.5 }}>
            {lang === 'uz'
              ? `Imtihondan o'tish uchun har bir bo'limdan kamida ${info.pass_score}% to'plash kerak.`
              : `Для сдачи экзамена необходимо набрать не менее ${info.pass_score}% в каждой части.`}
          </div>
        </div>
      </div>

      {/* Tips */}
      {(info.tips_ru || info.tips_uz) && (
        <div style={{
          background: 'rgba(99,102,241,.08)', border: '1px solid rgba(99,102,241,.2)',
          borderRadius: 'var(--radius)', padding: 14, marginBottom: 16,
        }}>
          <div style={{ fontSize: 13, fontWeight: 700, marginBottom: 8 }}>
            💡 {lang === 'uz' ? 'Tayyorlanish maslahatlari' : 'Советы по подготовке'}
          </div>
          <div style={{ fontSize: 12, color: 'var(--tg-hint)', lineHeight: 1.7 }}>
            {lang === 'uz' ? info.tips_uz : info.tips_ru}
          </div>
        </div>
      )}

      <button
        className="btn btn-primary"
        onClick={() => navigate(`/exam/${provider}/${level}`)}
      >
        {lang === 'uz' ? "Mashq qilishni boshlash →" : "Начать подготовку →"}
      </button>
    </div>
  )
}
