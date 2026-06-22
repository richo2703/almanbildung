import { useEffect, useState, useCallback } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api } from '../api'
import { useLang } from '../LangContext'
import { speakDE } from '../speak'

const PAIRS_COUNT = 4   // 4 pairs = 8 cards

function shuffle(arr) {
  const a = [...arr]
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]]
  }
  return a
}

function buildCards(words, lang) {
  // Pick PAIRS_COUNT random words
  const picked = shuffle(words).slice(0, PAIRS_COUNT)
  const cards = []
  picked.forEach((w, i) => {
    cards.push({ id: `de-${i}`, pairId: i, type: 'de', text: w.de, word: w })
    cards.push({ id: `tr-${i}`, pairId: i, type: 'tr', text: lang === 'uz' ? (w.uz || w.ru) : w.ru, word: w })
  })
  return shuffle(cards)
}

export default function MatchPage() {
  const { level, id } = useParams()
  const navigate = useNavigate()
  const { t, lang } = useLang()

  const [allWords, setAllWords] = useState([])
  const [cards, setCards] = useState([])
  const [matched, setMatched] = useState(new Set())    // matched pairIds
  const [selected, setSelected] = useState(null)       // { id, pairId, type }
  const [wrong, setWrong] = useState(new Set())        // card ids briefly shown as wrong
  const [moves, setMoves] = useState(0)
  const [finished, setFinished] = useState(false)
  const [startTime, setStartTime] = useState(null)
  const [elapsed, setElapsed] = useState(0)

  useEffect(() => {
    api.getLessonVocab(level, parseInt(id)).then(words => {
      setAllWords(words)
      setCards(buildCards(words, lang))
      setStartTime(Date.now())
    })
    window.Telegram?.WebApp?.BackButton?.show()
    window.Telegram?.WebApp?.BackButton?.onClick(() => navigate(`/lesson/${level}/${id}`))
    return () => window.Telegram?.WebApp?.BackButton?.hide()
  }, [level, id, lang])

  // Timer
  useEffect(() => {
    if (!startTime || finished) return
    const interval = setInterval(() => setElapsed(Math.floor((Date.now() - startTime) / 1000)), 1000)
    return () => clearInterval(interval)
  }, [startTime, finished])

  const handleCard = useCallback((card) => {
    if (matched.has(card.pairId)) return
    if (wrong.size > 0) return
    if (selected?.id === card.id) return  // same card tapped again

    if (card.type === 'de') speakDE(card.word.de)

    if (!selected) {
      setSelected(card)
      return
    }

    setMoves(m => m + 1)

    if (selected.pairId === card.pairId && selected.type !== card.type) {
      // Correct match!
      const newMatched = new Set(matched)
      newMatched.add(card.pairId)
      setMatched(newMatched)
      setSelected(null)
      if (newMatched.size === PAIRS_COUNT) {
        setElapsed(Math.floor((Date.now() - startTime) / 1000))
        setTimeout(() => setFinished(true), 400)
      }
    } else {
      // Wrong
      setWrong(new Set([selected.id, card.id]))
      setTimeout(() => {
        setWrong(new Set())
        setSelected(null)
      }, 700)
    }
  }, [selected, matched, wrong, startTime])

  const restart = () => {
    setCards(buildCards(allWords, lang))
    setMatched(new Set())
    setSelected(null)
    setWrong(new Set())
    setMoves(0)
    setFinished(false)
    setStartTime(Date.now())
    setElapsed(0)
  }

  if (!cards.length) return (
    <div className="loading"><div className="spinner" /></div>
  )

  const formatTime = (s) => `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`

  if (finished) {
    const stars = moves <= PAIRS_COUNT + 2 ? 3 : moves <= PAIRS_COUNT + 5 ? 2 : 1
    return (
      <div className="page" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '85vh', textAlign: 'center' }}>
        <div style={{ fontSize: 64, marginBottom: 8 }}>{'⭐'.repeat(stars)}</div>
        <h2 style={{ fontSize: 22, fontWeight: 800, marginBottom: 16 }}>
          {lang === 'uz' ? 'Barakalla!' : 'Отлично!'}
        </h2>
        <div style={{ display: 'flex', gap: 20, marginBottom: 24 }}>
          <div className="stat-card">
            <div className="stat-value" style={{ color: 'var(--accent)' }}>{moves}</div>
            <div className="stat-label">{lang === 'uz' ? 'Harakatlar' : 'Ходов'}</div>
          </div>
          <div className="stat-card">
            <div className="stat-value" style={{ color: 'var(--success)' }}>{formatTime(elapsed)}</div>
            <div className="stat-label">{lang === 'uz' ? 'Vaqt' : 'Время'}</div>
          </div>
          <div className="stat-card">
            <div className="stat-value" style={{ color: 'var(--warning)' }}>+{PAIRS_COUNT * 3} XP</div>
            <div className="stat-label">XP</div>
          </div>
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 10, width: '100%', maxWidth: 320 }}>
          <button className="btn btn-primary" onClick={restart}>
            🔄 {lang === 'uz' ? 'Yangi o\'yin' : 'Новая игра'}
          </button>
          <button className="btn btn-secondary" onClick={() => navigate(`/lesson/${level}/${id}`)}>
            {t.backToLessons}
          </button>
        </div>
      </div>
    )
  }

  return (
    <div className="page">
      {/* Header */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 16 }}>
        <button className="back-btn" onClick={() => navigate(`/lesson/${level}/${id}`)}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="15 18 9 12 15 6"/>
          </svg>
        </button>
        <div style={{ fontWeight: 700, color: 'var(--tg-hint)', fontSize: 14 }}>
          {lang === 'uz' ? 'Juftlarni top' : 'Найди пары'} · {matched.size}/{PAIRS_COUNT}
        </div>
        <div style={{ fontWeight: 700, color: 'var(--tg-hint)', fontSize: 14 }}>
          ⏱ {formatTime(elapsed)}
        </div>
      </div>

      {/* Progress */}
      <div className="progress-bar" style={{ marginBottom: 24 }}>
        <div className="progress-bar-fill" style={{ width: `${(matched.size / PAIRS_COUNT) * 100}%` }} />
      </div>

      {/* Hint */}
      <div style={{ textAlign: 'center', fontSize: 13, color: 'var(--tg-hint)', marginBottom: 16 }}>
        {lang === 'uz'
          ? "Nemischa so'z va uning tarjimasini juftlashtiring"
          : 'Соедини немецкое слово с переводом'}
      </div>

      {/* Card grid */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: '1fr 1fr',
        gap: 10,
      }}>
        {cards.map(card => {
          const isMatched = matched.has(card.pairId)
          const isSelected = selected?.id === card.id
          const isWrong = wrong.has(card.id)
          const isDe = card.type === 'de'

          return (
            <button
              key={card.id}
              onClick={() => !isMatched && handleCard(card)}
              style={{
                padding: '14px 10px',
                borderRadius: 14,
                fontWeight: 700,
                fontSize: 14,
                lineHeight: 1.3,
                cursor: isMatched ? 'default' : 'pointer',
                transition: 'all .2s',
                minHeight: 64,
                border: isMatched
                  ? '1.5px solid rgba(34,197,94,.4)'
                  : isWrong
                  ? '1.5px solid rgba(239,68,68,.6)'
                  : isSelected
                  ? '1.5px solid var(--accent)'
                  : '1.5px solid rgba(255,255,255,.1)',
                background: isMatched
                  ? 'rgba(34,197,94,.1)'
                  : isWrong
                  ? 'rgba(239,68,68,.12)'
                  : isSelected
                  ? 'rgba(99,102,241,.18)'
                  : isDe
                  ? 'rgba(99,102,241,.07)'
                  : 'rgba(255,255,255,.05)',
                color: isMatched
                  ? 'var(--success)'
                  : isWrong
                  ? 'var(--danger)'
                  : isSelected
                  ? 'var(--accent)'
                  : 'var(--tg-text)',
                transform: isSelected ? 'scale(1.03)' : isWrong ? 'scale(.97)' : 'scale(1)',
                opacity: isMatched ? .55 : 1,
              }}
            >
              {isMatched ? '✓' : card.text}
              {isDe && !isMatched && (
                <div style={{ fontSize: 10, color: 'var(--tg-hint)', marginTop: 3, fontWeight: 500 }}>🇩🇪</div>
              )}
            </button>
          )
        })}
      </div>

      {/* Move counter */}
      <div style={{ textAlign: 'center', marginTop: 20, fontSize: 13, color: 'var(--tg-hint)' }}>
        {lang === 'uz' ? 'Harakatlar' : 'Ходов'}: <strong style={{ color: 'var(--tg-text)' }}>{moves}</strong>
      </div>
    </div>
  )
}
