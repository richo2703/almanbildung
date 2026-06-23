import { useEffect, useState, useRef, useCallback } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api } from '../api'
import { useLang } from '../LangContext'

const DURATION = 30   // seconds

function shuffle(arr) {
  const a = [...arr]
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]]
  }
  return a
}

function buildQueue(words, lang) {
  // Repeat words if fewer than 20
  let pool = [...words]
  while (pool.length < 20) pool = [...pool, ...words]
  return shuffle(pool).map(w => ({
    word: w,
    correctTranslation: lang === 'uz' ? (w.uz || w.ru) : w.ru,
  }))
}

function getWrongOption(allWords, correct, lang) {
  const others = allWords.filter(w => {
    const t = lang === 'uz' ? (w.uz || w.ru) : w.ru
    return t !== correct
  })
  const pick = others[Math.floor(Math.random() * others.length)]
  return lang === 'uz' ? (pick?.uz || pick?.ru) : pick?.ru
}

export default function SpeedPage() {
  const { level, id } = useParams()
  const navigate = useNavigate()
  const { t, lang } = useLang()

  const [allWords, setAllWords] = useState([])
  const [queue, setQueue] = useState([])
  const [qIdx, setQIdx] = useState(0)
  const [score, setScore] = useState(0)
  const [wrong, setWrong] = useState(0)
  const [timeLeft, setTimeLeft] = useState(DURATION)
  const [phase, setPhase] = useState('ready') // ready | playing | finished
  const [flash, setFlash] = useState(null)    // 'correct' | 'wrong'
  const [options, setOptions] = useState([])

  const timerRef = useRef(null)

  useEffect(() => {
    api.getLessonVocab(level, parseInt(id)).then(words => {
      setAllWords(words)
      setQueue(buildQueue(words, lang))
    })
    window.Telegram?.WebApp?.BackButton?.show()
    window.Telegram?.WebApp?.BackButton?.onClick(() => navigate(`/lesson/${level}/${id}`))
    return () => {
      window.Telegram?.WebApp?.BackButton?.hide()
      clearInterval(timerRef.current)
    }
  }, [level, id, lang])

  // Build options for current question
  useEffect(() => {
    if (!queue.length || !allWords.length) return
    const current = queue[qIdx % queue.length]
    const correct = current.correctTranslation
    const wrong = getWrongOption(allWords, correct, lang)
    const opts = shuffle([
      { text: correct, isCorrect: true },
      { text: wrong || '—', isCorrect: false },
    ])
    setOptions(opts)
  }, [qIdx, queue, allWords, lang])

  const startGame = () => {
    setPhase('playing')
    setScore(0)
    setWrong(0)
    setQIdx(0)
    setTimeLeft(DURATION)
    setQueue(buildQueue(allWords, lang))

    timerRef.current = setInterval(() => {
      setTimeLeft(prev => {
        if (prev <= 1) {
          clearInterval(timerRef.current)
          setPhase('finished')
          return 0
        }
        return prev - 1
      })
    }, 1000)
  }

  const handleAnswer = useCallback((isCorrect) => {
    if (phase !== 'playing') return
    setFlash(isCorrect ? 'correct' : 'wrong')
    if (isCorrect) setScore(s => s + 1)
    else setWrong(w => w + 1)
    setTimeout(() => {
      setFlash(null)
      setQIdx(i => i + 1)
    }, 300)
  }, [phase])

  const pct = timeLeft / DURATION
  const timerColor = pct > 0.5 ? 'var(--success)' : pct > 0.25 ? 'var(--warning)' : 'var(--danger)'

  if (phase === 'ready') {
    return (
      <div className="page" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '85vh', textAlign: 'center' }}>
        <div style={{ fontSize: 72, marginBottom: 16 }}>⚡</div>
        <h2 style={{ fontSize: 24, fontWeight: 800, marginBottom: 8 }}>
          {lang === 'uz' ? 'Tezkor raund' : 'Speed Round'}
        </h2>
        <p style={{ color: 'var(--tg-hint)', marginBottom: 8, fontSize: 15 }}>
          {lang === 'uz'
            ? '30 soniya — to\'g\'ri tarjimani tanlang!'
            : '30 секунд — выбирай правильный перевод!'}
        </p>
        <div style={{ display: 'flex', gap: 20, marginBottom: 32 }}>
          <div className="stat-card">
            <div className="stat-value" style={{ color: 'var(--warning)' }}>30</div>
            <div className="stat-label">{lang === 'uz' ? 'soniya' : 'секунд'}</div>
          </div>
          <div className="stat-card">
            <div className="stat-value" style={{ color: 'var(--accent)' }}>2</div>
            <div className="stat-label">{lang === 'uz' ? 'variant' : 'варианта'}</div>
          </div>
        </div>
        <button className="btn btn-primary" style={{ width: '100%', maxWidth: 280, fontSize: 18, padding: '16px' }} onClick={startGame}>
          ▶ {lang === 'uz' ? 'Boshlash' : 'Старт!'}
        </button>
        <button className="btn btn-secondary" style={{ marginTop: 10, maxWidth: 280 }} onClick={() => navigate(`/lesson/${level}/${id}`)}>
          {t.backToLessons}
        </button>
      </div>
    )
  }

  if (phase === 'finished') {
    const total = score + wrong
    const accuracy = total ? Math.round((score / total) * 100) : 0
    const emoji = score >= 20 ? '🔥' : score >= 12 ? '⚡' : score >= 6 ? '👍' : '💪'
    return (
      <div className="page" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '85vh', textAlign: 'center' }}>
        <div style={{ fontSize: 72, marginBottom: 8 }}>{emoji}</div>
        <h2 style={{ fontSize: 22, fontWeight: 800, marginBottom: 16 }}>
          {lang === 'uz' ? 'Vaqt tugadi!' : 'Время вышло!'}
        </h2>
        <div style={{ display: 'flex', gap: 12, marginBottom: 24 }}>
          <div className="stat-card">
            <div className="stat-value" style={{ color: 'var(--success)' }}>{score}</div>
            <div className="stat-label">{lang === 'uz' ? "To'g'ri" : 'Правильно'}</div>
          </div>
          <div className="stat-card">
            <div className="stat-value" style={{ color: 'var(--danger)' }}>{wrong}</div>
            <div className="stat-label">{lang === 'uz' ? 'Noto\'g\'ri' : 'Ошибок'}</div>
          </div>
          <div className="stat-card">
            <div className="stat-value" style={{ color: 'var(--accent)' }}>{accuracy}%</div>
            <div className="stat-label">{lang === 'uz' ? 'Aniqlik' : 'Точность'}</div>
          </div>
        </div>
        <div className="xp-chip" style={{ marginBottom: 24 }}>⭐ +{score * 3} XP</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 10, width: '100%', maxWidth: 300 }}>
          <button className="btn btn-primary" onClick={startGame}>
            🔄 {lang === 'uz' ? 'Qayta' : 'Снова'}
          </button>
          <button className="btn btn-secondary" onClick={() => navigate(`/lesson/${level}/${id}`)}>
            {t.backToLessons}
          </button>
        </div>
      </div>
    )
  }

  // Playing
  const current = queue[qIdx % queue.length]
  const bgFlash = flash === 'correct'
    ? 'rgba(34,197,94,.12)' : flash === 'wrong'
    ? 'rgba(239,68,68,.12)' : 'transparent'

  return (
    <div className="page" style={{ transition: 'background .15s', background: bgFlash }}>
      {/* Timer row */}
      <div style={{ display: 'flex', alignItems: 'center', gap: 12, marginBottom: 8 }}>
        <div style={{ flex: 1, height: 8, background: 'rgba(255,255,255,.1)', borderRadius: 99, overflow: 'hidden' }}>
          <div style={{ height: '100%', width: `${pct * 100}%`, background: timerColor, borderRadius: 99, transition: 'width 1s linear, background .3s' }} />
        </div>
        <div style={{ fontSize: 24, fontWeight: 900, color: timerColor, minWidth: 36, textAlign: 'right', transition: 'color .3s' }}>
          {timeLeft}
        </div>
      </div>

      {/* Score */}
      <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 28 }}>
        <span style={{ color: 'var(--success)', fontWeight: 800, fontSize: 18 }}>✓ {score}</span>
        <span style={{ color: 'var(--tg-hint)', fontSize: 14 }}>
          {lang === 'uz' ? 'so\'z' : 'слов'}: {qIdx}
        </span>
        <span style={{ color: 'var(--danger)', fontWeight: 800, fontSize: 18 }}>✗ {wrong}</span>
      </div>

      {/* Word card */}
      <div className="card" style={{ textAlign: 'center', padding: '40px 24px', marginBottom: 24 }}>
        <div style={{ fontSize: 11, color: 'var(--tg-hint)', letterSpacing: 1, textTransform: 'uppercase', marginBottom: 10 }}>
          🇩🇪 {lang === 'uz' ? "Nemischa" : 'Немецкий'}
        </div>
        <div style={{ fontSize: 34, fontWeight: 900, color: 'var(--tg-text)' }}>
          {current?.word?.de}
        </div>
      </div>

      {/* Answer buttons */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
        {options.map((opt, i) => (
          <button
            key={`${qIdx}-${i}`}
            onClick={() => handleAnswer(opt.isCorrect)}
            style={{
              padding: '18px 20px',
              borderRadius: 16,
              border: '1.5px solid rgba(255,255,255,.12)',
              background: 'rgba(255,255,255,.05)',
              color: 'var(--tg-text)',
              fontWeight: 700,
              fontSize: 17,
              cursor: 'pointer',
              transition: 'transform .1s',
              textAlign: 'center',
            }}
          >
            {opt.text}
          </button>
        ))}
      </div>
    </div>
  )
}
