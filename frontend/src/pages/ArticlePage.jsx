import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api } from '../api'
import { useLang } from '../LangContext'
import { speakDE } from '../speak'

// Parse article from "der Hund" -> { article: "der", base: "Hund" }
function parseNoun(de) {
  const match = de.match(/^(der|die|das)\s+(.+)$/i)
  if (!match) return null
  return { article: match[1].toLowerCase(), base: match[2] }
}

const ARTICLES = ['der', 'die', 'das']

const ARTICLE_COLORS = {
  der: { bg: 'rgba(59,130,246,.15)', border: 'rgba(59,130,246,.4)', text: '#3B82F6' },   // blue - masculine
  die: { bg: 'rgba(236,72,153,.15)', border: 'rgba(236,72,153,.4)', text: '#EC4899' },   // pink - feminine
  das: { bg: 'rgba(16,185,129,.15)', border: 'rgba(16,185,129,.4)', text: '#10B981' },   // green - neuter
}

export default function ArticlePage() {
  const { level, id } = useParams()
  const navigate = useNavigate()
  const { t, lang } = useLang()

  const [nouns, setNouns] = useState([])       // filtered nouns with articles
  const [idx, setIdx] = useState(0)
  const [selected, setSelected] = useState(null) // which article was tapped
  const [score, setScore] = useState(0)
  const [finished, setFinished] = useState(false)
  const [shake, setShake] = useState(false)

  useEffect(() => {
    api.getLessonVocab(level, parseInt(id)).then(words => {
      const parsed = words
        .map(w => ({ ...w, parsed: parseNoun(w.de) }))
        .filter(w => w.parsed !== null)
      // Shuffle
      for (let i = parsed.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [parsed[i], parsed[j]] = [parsed[j], parsed[i]]
      }
      setNouns(parsed)
    })
    window.Telegram?.WebApp?.BackButton?.show()
    window.Telegram?.WebApp?.BackButton?.onClick(() => navigate(`/lesson/${level}/${id}`))
    return () => window.Telegram?.WebApp?.BackButton?.hide()
  }, [level, id])

  // Pronounce current noun when it changes
  useEffect(() => {
    if (nouns.length && !finished) {
      const noun = nouns[idx]
      if (noun) setTimeout(() => speakDE(noun.de), 300)
    }
  }, [idx, nouns, finished])

  if (!nouns.length) {
    return (
      <div className="page" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '60vh', flexDirection: 'column', gap: 12 }}>
        <div style={{ fontSize: 48 }}>😕</div>
        <div style={{ color: 'var(--tg-hint)', textAlign: 'center' }}>
          {lang === 'uz' ? "Bu darsda ot so'zlari topilmadi" : 'В этом уроке нет существительных с артиклем'}
        </div>
        <button className="btn btn-secondary" onClick={() => navigate(`/lesson/${level}/${id}`)}>
          {t.backToLessons}
        </button>
      </div>
    )
  }

  if (finished) {
    const pct = Math.round((score / nouns.length) * 100)
    const emoji = pct >= 80 ? '🏆' : pct >= 50 ? '👍' : '📚'
    return (
      <div className="page" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '85vh', textAlign: 'center' }}>
        <div style={{ fontSize: 72, marginBottom: 16 }}>{emoji}</div>
        <h2 style={{ fontSize: 22, fontWeight: 800, marginBottom: 4 }}>{t.result}</h2>
        <div style={{ fontSize: 48, fontWeight: 900, marginBottom: 4,
          color: pct >= 80 ? 'var(--success)' : pct >= 50 ? 'var(--warning)' : 'var(--danger)' }}>
          {pct}%
        </div>
        <div style={{ fontSize: 16, color: 'var(--tg-hint)', marginBottom: 8 }}>
          {score} / {nouns.length}
        </div>
        <div className="xp-chip" style={{ marginBottom: 8 }}>⭐ +{score * 2} XP</div>

        {/* Article legend */}
        <div style={{ display: 'flex', gap: 10, marginBottom: 24, marginTop: 8 }}>
          {ARTICLES.map(a => (
            <div key={a} style={{ background: ARTICLE_COLORS[a].bg, border: `1px solid ${ARTICLE_COLORS[a].border}`, borderRadius: 10, padding: '4px 12px', fontSize: 13, fontWeight: 700, color: ARTICLE_COLORS[a].text }}>
              {a}
            </div>
          ))}
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: 10, width: '100%', maxWidth: 320 }}>
          <button className="btn btn-primary" onClick={() => { setIdx(0); setSelected(null); setScore(0); setFinished(false) }}>
            🔄 {t.tryAgain}
          </button>
          <button className="btn btn-secondary" onClick={() => navigate(`/lesson/${level}/${id}`)}>
            {t.backToLessons}
          </button>
        </div>
      </div>
    )
  }

  const noun = nouns[idx]
  const progress = (idx / nouns.length) * 100
  const correct = noun.parsed.article
  const isAnswered = selected !== null

  const handleAnswer = (art) => {
    if (isAnswered) return
    setSelected(art)
    const ok = art === correct
    if (ok) {
      setScore(s => s + 1)
    } else {
      setShake(true)
      setTimeout(() => setShake(false), 600)
    }
    setTimeout(() => {
      if (idx + 1 >= nouns.length) {
        setFinished(true)
      } else {
        setIdx(i => i + 1)
        setSelected(null)
      }
    }, 1000)
  }

  return (
    <div className="page">
      {/* Header */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 12 }}>
        <button className="back-btn" onClick={() => navigate(`/lesson/${level}/${id}`)}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="15 18 9 12 15 6"/>
          </svg>
        </button>
        <div style={{ fontWeight: 700, fontSize: 13, color: 'var(--tg-hint)' }}>
          {lang === 'uz' ? 'Artikl' : 'Артикль'} {idx + 1}/{nouns.length}
        </div>
        <div style={{ fontWeight: 800, color: 'var(--success)', fontSize: 16 }}>✓ {score}</div>
      </div>

      <div className="progress-bar" style={{ marginBottom: 32 }}>
        <div className="progress-bar-fill" style={{ width: `${progress}%` }} />
      </div>

      {/* Question card */}
      <div
        className="card"
        style={{
          textAlign: 'center',
          padding: '40px 24px',
          marginBottom: 28,
          animation: shake ? 'shake .5s ease' : undefined,
        }}
      >
        <div style={{ fontSize: 12, color: 'var(--tg-hint)', letterSpacing: 1, marginBottom: 8, textTransform: 'uppercase' }}>
          {lang === 'uz' ? 'Artiklni tanlang' : 'Выбери артикль'}
        </div>
        <div style={{ fontSize: 36, fontWeight: 900, color: 'var(--tg-text)', marginBottom: 8 }}>
          {noun.parsed.base}
        </div>
        <div style={{ fontSize: 14, color: 'var(--tg-hint)' }}>
          {lang === 'uz' ? noun.uz : noun.ru}
        </div>
        {/* Speak button */}
        <button
          onClick={() => speakDE(noun.de)}
          style={{ marginTop: 14, background: 'rgba(255,255,255,.07)', border: '1px solid rgba(255,255,255,.12)', borderRadius: 10, padding: '6px 14px', cursor: 'pointer', fontSize: 18, color: 'var(--tg-hint)' }}
        >🔊</button>
      </div>

      {/* Article buttons */}
      <div style={{ display: 'flex', gap: 10 }}>
        {ARTICLES.map(art => {
          const c = ARTICLE_COLORS[art]
          let bg = c.bg
          let border = c.border
          let scale = 1
          let opacity = 1

          if (isAnswered) {
            if (art === correct) { bg = c.bg; border = c.border; scale = 1.04 }
            else if (art === selected) { bg = 'var(--danger-dim)'; border = 'rgba(239,68,68,.4)'; opacity = .7 }
            else { opacity = .35 }
          }

          return (
            <button
              key={art}
              onClick={() => handleAnswer(art)}
              style={{
                flex: 1,
                padding: '20px 0',
                borderRadius: 16,
                border: `2px solid ${border}`,
                background: bg,
                color: isAnswered && art === correct ? c.text : isAnswered && art === selected ? 'var(--danger)' : c.text,
                fontWeight: 900,
                fontSize: 20,
                cursor: isAnswered ? 'default' : 'pointer',
                transition: 'all .25s',
                transform: `scale(${scale})`,
                opacity,
              }}
            >
              {art}
              {isAnswered && art === correct && <div style={{ fontSize: 13, marginTop: 4 }}>✓</div>}
              {isAnswered && art === selected && art !== correct && <div style={{ fontSize: 13, marginTop: 4 }}>✗</div>}
            </button>
          )
        })}
      </div>

      {/* Color legend */}
      <div style={{ display: 'flex', justifyContent: 'center', gap: 16, marginTop: 20 }}>
        <span style={{ fontSize: 12, color: ARTICLE_COLORS.der.text }}>der = м.р.</span>
        <span style={{ fontSize: 12, color: ARTICLE_COLORS.die.text }}>die = ж.р.</span>
        <span style={{ fontSize: 12, color: ARTICLE_COLORS.das.text }}>das = с.р.</span>
      </div>
    </div>
  )
}
