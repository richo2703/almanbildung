import { useNavigate } from 'react-router-dom'
import { useLang, LANGS } from '../LangContext'
import { api } from '../api'

export default function SettingsPage() {
  const { lang, setLang, t } = useLang()
  const navigate = useNavigate()

  const handleLangChange = async (code) => {
    setLang(code)
    await api.setLang(code).catch(() => {})
  }

  return (
    <div className="page">
      <div className="page-header">
        <h1>{t.settings}</h1>
      </div>

      {/* Language */}
      <div className="section-title">{t.changeLanguage}</div>
      {Object.values(LANGS).map(l => (
        <div
          key={l.code}
          className="card card-row"
          style={{ cursor: 'pointer', marginBottom: 10, border: lang === l.code ? '1.5px solid var(--accent)' : undefined }}
          onClick={() => handleLangChange(l.code)}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
            <span style={{ fontSize: 28 }}>{l.flag}</span>
            <div>
              <div style={{ fontWeight: 700, fontSize: 16 }}>{l.name}</div>
              <div style={{ fontSize: 13, color: 'var(--tg-hint)' }}>
                {l.code === 'ru' ? 'Грамматика и переводы на русском' : "Grammatika va tarjimalar o'zbekcha"}
              </div>
            </div>
          </div>
          {lang === l.code && (
            <div style={{ color: 'var(--accent)', fontSize: 20, fontWeight: 800 }}>✓</div>
          )}
        </div>
      ))}

      {/* About */}
      <div className="section-title">{t.aboutApp}</div>
      <div className="card">
        <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
          <span style={{ fontSize: 32 }}>🇩🇪</span>
          <div>
            <div style={{ fontWeight: 700 }}>{t.version}</div>
            <div style={{ fontSize: 13, color: 'var(--tg-hint)' }}>
              {lang === 'uz'
                ? '48 dars · 2304 so\'z · 576 test'
                : '48 уроков · 2304 слова · 576 тестов'}
            </div>
          </div>
        </div>
      </div>

      <div className="card" style={{ marginTop: 0 }}>
        <div style={{ fontSize: 13, color: 'var(--tg-hint)', lineHeight: 1.7 }}>
          {lang === 'uz'
            ? "A1.1 dan B1.2 gacha nemis tilini o'rganish platformasi. Grammatika rus va o'zbek tillarida tushuntiriladi."
            : 'Платформа изучения немецкого языка от A1.1 до B1.2. Грамматика объясняется на русском и узбекском языках.'}
        </div>
      </div>
    </div>
  )
}
