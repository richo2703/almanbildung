import { useLang, LANGS } from '../LangContext'

export default function OnboardingPage() {
  const { setLang } = useLang()

  return (
    <div style={{
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '32px 24px',
      background: 'linear-gradient(160deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%)',
    }}>
      {/* Logo */}
      <div style={{ textAlign: 'center', marginBottom: 48 }}>
        <div style={{ fontSize: 72, marginBottom: 16 }}>🇩🇪</div>
        <h1 style={{ color: '#fff', fontSize: 32, fontWeight: 800, marginBottom: 8 }}>
          Alman Bildung
        </h1>
        <p style={{ color: 'rgba(255,255,255,.6)', fontSize: 16 }}>
          Немецкий язык A1 → B1
        </p>
      </div>

      {/* Language choice */}
      <div style={{ width: '100%', maxWidth: 340 }}>
        <p style={{
          color: 'rgba(255,255,255,.8)',
          textAlign: 'center',
          marginBottom: 20,
          fontSize: 16,
          fontWeight: 500,
        }}>
          Выберите язык обучения / O'qitish tilini tanlang
        </p>

        {Object.values(LANGS).map(l => (
          <button
            key={l.code}
            onClick={() => setLang(l.code)}
            style={{
              width: '100%',
              display: 'flex',
              alignItems: 'center',
              gap: 16,
              padding: '18px 24px',
              marginBottom: 12,
              borderRadius: 16,
              background: 'rgba(255,255,255,.1)',
              border: '2px solid rgba(255,255,255,.15)',
              color: '#fff',
              fontSize: 17,
              fontWeight: 600,
              cursor: 'pointer',
              transition: 'all .2s',
              backdropFilter: 'blur(10px)',
            }}
            onMouseOver={e => e.currentTarget.style.background = 'rgba(255,255,255,.2)'}
            onMouseOut={e => e.currentTarget.style.background = 'rgba(255,255,255,.1)'}
          >
            <span style={{ fontSize: 36 }}>{l.flag}</span>
            <div style={{ textAlign: 'left' }}>
              <div style={{ fontSize: 18, fontWeight: 700 }}>{l.name}</div>
              <div style={{ fontSize: 13, opacity: .7, fontWeight: 400 }}>
                {l.code === 'ru' ? 'Правила на русском языке' : "Qoidalar o'zbek tilida"}
              </div>
            </div>
            <span style={{ marginLeft: 'auto', opacity: .6, fontSize: 20 }}>→</span>
          </button>
        ))}
      </div>

      <p style={{ color: 'rgba(255,255,255,.4)', fontSize: 12, marginTop: 32, textAlign: 'center' }}>
        Можно изменить в настройках в любое время
      </p>
    </div>
  )
}
