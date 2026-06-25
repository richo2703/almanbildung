import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { api } from '../api'
import { useLang } from '../LangContext'

const PROVIDER_INFO = {
  goethe: {
    emoji: '🏛️',
    color: '#3B82F6',
    tagRu: 'Виза • Гражданство • Работа',
    tagUz: 'Viza • Fuqarolik • Ish',
    popular: true,
  },
  telc: {
    emoji: '📋',
    color: '#A855F7',
    tagRu: 'Образование • Интеграция',
    tagUz: "Ta'lim • Integratsiya",
    popular: false,
  },
  osd: {
    emoji: '🇦🇹',
    color: '#22C55E',
    tagRu: 'Австрия • Гражданство • Учёба',
    tagUz: 'Avstriya • Fuqarolik • O\'qish',
    popular: false,
  },
}

export default function ExamPage() {
  const navigate = useNavigate()
  const { lang, t } = useLang()
  const [providers, setProviders] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    api.exam.getProviders()
      .then(setProviders)
      .catch(() => setProviders([]))
      .finally(() => setLoading(false))
  }, [])

  return (
    <div className="page">
      {/* Header */}
      <div style={{ marginBottom: 24 }}>
        <div style={{ fontSize: 22, fontWeight: 800, marginBottom: 4 }}>
          🎓 {lang === 'uz' ? 'Imtihonga tayyorgarlik' : 'Подготовка к экзамену'}
        </div>
        <div style={{ fontSize: 13, color: 'var(--tg-hint)', lineHeight: 1.5 }}>
          {lang === 'uz'
            ? "Rasmiy nemis tili imtihoniga tayyorlanish uchun modul"
            : 'Модуль подготовки к официальным экзаменам по немецкому языку'}
        </div>
      </div>

      {/* Disclaimer */}
      <div style={{
        background: 'rgba(245,158,11,.08)',
        border: '1px solid rgba(245,158,11,.2)',
        borderRadius: 10,
        padding: '10px 14px',
        fontSize: 11,
        color: 'var(--tg-hint)',
        marginBottom: 20,
        lineHeight: 1.5,
      }}>
        ⚠️ Diese Übungen dienen zur Prüfungsvorbereitung und sind keine offiziellen Prüfungsunterlagen von Goethe-Institut, telc oder ÖSD.
      </div>

      {/* Providers */}
      <div style={{ fontSize: 12, fontWeight: 700, color: 'var(--tg-hint)', letterSpacing: 1, textTransform: 'uppercase', marginBottom: 12 }}>
        {lang === 'uz' ? 'Imtihon turini tanlang' : 'Выберите экзамен'}
      </div>

      {loading ? (
        <div style={{ textAlign: 'center', padding: 40, color: 'var(--tg-hint)' }}>...</div>
      ) : (
        providers.map(p => {
          const info = PROVIDER_INFO[p.name] || {}
          return (
            <button
              key={p.name}
              onClick={() => navigate(`/exam/${p.name}`)}
              style={{
                width: '100%', textAlign: 'left',
                background: 'var(--card-bg)',
                border: `1px solid var(--card-border)`,
                borderRadius: 'var(--radius)',
                padding: '16px',
                marginBottom: 12,
                position: 'relative',
                overflow: 'hidden',
              }}
            >
              {info.popular && (
                <div style={{
                  position: 'absolute', top: 10, right: 10,
                  background: 'var(--warning-dim)', color: 'var(--warning)',
                  borderRadius: 99, padding: '2px 10px', fontSize: 11, fontWeight: 700,
                }}>
                  {lang === 'uz' ? 'Mashhur' : 'Популярный'}
                </div>
              )}
              <div style={{ display: 'flex', alignItems: 'center', gap: 12, marginBottom: 8 }}>
                <div style={{
                  width: 44, height: 44, borderRadius: 12,
                  background: info.color ? info.color + '22' : 'var(--accent-dim)',
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  fontSize: 22,
                }}>
                  {info.emoji || '🎓'}
                </div>
                <div>
                  <div style={{ fontWeight: 800, fontSize: 16 }}>{p.title}</div>
                  <div style={{ fontSize: 11, color: info.color || 'var(--accent)', fontWeight: 600 }}>
                    {lang === 'uz' ? info.tagUz : info.tagRu}
                  </div>
                </div>
              </div>
              <div style={{ fontSize: 12, color: 'var(--tg-hint)', lineHeight: 1.5 }}>
                {lang === 'uz' ? p.description_uz : p.description_ru}
              </div>
              <div style={{
                marginTop: 12, fontSize: 12, color: info.color || 'var(--accent)',
                fontWeight: 700, display: 'flex', alignItems: 'center', gap: 4,
              }}>
                {lang === 'uz' ? "Darajani tanlash →" : "Выбрать уровень →"}
              </div>
            </button>
          )
        })
      )}

      {/* Info about levels */}
      <div style={{ marginTop: 8, padding: 16, background: 'var(--card-bg)', borderRadius: 'var(--radius)', border: '1px solid var(--card-border)' }}>
        <div style={{ fontSize: 13, fontWeight: 700, marginBottom: 8 }}>
          {lang === 'uz' ? '📊 Mavjud darajalar' : '📊 Доступные уровни'}
        </div>
        {['A1', 'A2', 'B1', 'B2'].map(l => (
          <div key={l} style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 6 }}>
            <span style={{
              background: 'var(--accent-dim)', color: 'var(--accent)',
              padding: '2px 8px', borderRadius: 6, fontSize: 12, fontWeight: 700, minWidth: 28,
            }}>{l}</span>
            <span style={{ fontSize: 12, color: 'var(--tg-hint)' }}>
              {l === 'A1' && (lang === 'uz' ? 'Boshlang\'ich — Viza uchun' : 'Начальный — Для визы')}
              {l === 'A2' && (lang === 'uz' ? 'Asosiy — Ish va integratsiya' : 'Базовый — Работа и интеграция')}
              {l === 'B1' && (lang === 'uz' ? 'O\'rta — Fuqarolik' : 'Средний — Гражданство')}
              {l === 'B2' && (lang === 'uz' ? 'Yuqori o\'rta — Universitet' : 'Выше среднего — Университет')}
            </span>
          </div>
        ))}
      </div>
    </div>
  )
}
