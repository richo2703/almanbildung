import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api } from '../api'
import { useLang } from '../LangContext'
import { speakDE } from '../speak'

// Words too common/short to blank out
const SKIP_WORDS = new Set([
  'ich','du','er','sie','es','wir','ihr','Sie',
  'der','die','das','ein','eine','einen','einem','einer','eines',
  'und','oder','aber','denn','weil','dass','wenn','ob',
  'ist','bin','bist','sind','war','waren','hat','habe','haben','hatte',
  'in','auf','an','von','zu','mit','für','aus','bei','nach','vor',
  'über','unter','neben','zwischen','durch','gegen',
  'nicht','kein','keine','keinen','auch','schon','noch','ja','nein',
  'wie','was','wer','wo','woher','wohin','wann','warum','wie viel',
  'mein','meine','dein','deine','sein','ihre','unser','euer',
  'a','b','c',
])

function shuffle(arr) {
  const a = [...arr]
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]]
  }
  return a
}

// Strip punctuation for comparison
const clean = s => s.replace(/[.,!?;:'"()]/g, '').trim()

// Generate fill-in-blank questions from dialogue lines + vocab
function generateFromDialogue(dialogue, vocab, lang) {
  const questions = []
  const vocabWords = vocab.map(w => w.de)

  for (const [, line] of dialogue) {
    const words = line.split(/\s+/)
    if (words.length < 4) continue  // skip too-short lines

    // Find a good word to blank (not in skip list, length >= 3)
    const candidates = words
      .map((w, i) => ({ w, i }))
      .filter(({ w }) => {
        const c = clean(w)
        return c.length >= 3 && !SKIP_WORDS.has(c.toLowerCase()) && !SKIP_WORDS.has(c)
      })

    if (!candidates.length) continue

    const { w: targetRaw, i: targetIdx } = candidates[Math.floor(Math.random() * candidates.length)]
    const targetClean = clean(targetRaw)

    // Build sentence with blank
    const withBlank = words.map((w, i) => i === targetIdx ? '_____' : w).join(' ')

    // Distractors: pick random vocab words different from target
    const distractors = shuffle(vocabWords.filter(v => clean(v) !== targetClean))
      .slice(0, 3)
      .map(v => v)

    const opts = shuffle([targetClean, ...distractors])
    const ans = opts.indexOf(targetClean)

    // Translation hint: look up in vocab
    const match = vocab.find(v => clean(v.de) === targetClean)
    const hint = match ? (lang === 'uz' ? (match.uz || match.ru) : match.ru) : null

    questions.push({ sentence: withBlank, original: line, opts, ans, hint })
  }

  return questions
}

// Merge existing fill exercises (type:"fill") with generated ones
function buildQuestions(exercises, dialogue, vocab, lang) {
  const fromExercises = exercises
    .filter(e => e.type === 'fill' || (e.q && e.q.includes('___')))
    .map(e => ({ sentence: e.q, opts: e.opts, ans: e.ans, hint: null, original: null }))

  const generated = generateFromDialogue(dialogue, vocab, lang)

  const all = shuffle([...fromExercises, ...generated])
  return all.length ? all : generated  // fallback to generated only
}

export default function FillPage() {
  const { level, id } = useParams()
  const navigate = useNavigate()
  const { t, lang } = useLang()

  const [questions, setQuestions] = useState([])
  const [qIdx, setQIdx] = useState(0)
  const [selected, setSelected] = useState(null)
  const [score, setScore] = useState(0)
  const [finished, setFinished] = useState(false)

  useEffect(() => {
    Promise.all([
      api.getLesson(level, parseInt(id)),
      api.getLessonVocab(level, parseInt(id)),
      api.getLessonExercises(level, parseInt(id)),
    ]).then(([lesson, vocab, exercises]) => {
      const dialogue = lesson.dialogue || []
      const qs = buildQuestions(exercises, dialogue, vocab, lang)
      setQuestions(qs)
    })
    window.Telegram?.WebApp?.BackButton?.show()
    window.Telegram?.WebApp?.BackButton?.onClick(() => navigate(`/lesson/${level}/${id}`))
    return () => window.Telegram?.WebApp?.BackButton?.hide()
  }, [level, id, lang])

  const handleAnswer = (optIdx) => {
    if (selected !== null) return
    setSelected(optIdx)
    if (optIdx === questions[qIdx].ans) setScore(s => s + 1)
    setTimeout(() => {
      if (qIdx + 1 >= questions.length) setFinished(true)
      else { setQIdx(i => i + 1); setSelected(null) }
    }, 1100)
  }

  if (!questions.length) return (
    <div className="loading"><div className="spinner" /></div>
  )

  if (finished) {
    const pct = Math.round((score / questions.length) * 100)
    const emoji = pct >= 80 ? '🏆' : pct >= 50 ? '👍' : '📚'
    return (
      <div className="page" style={{ display:'flex', flexDirection:'column', alignItems:'center', justifyContent:'center', minHeight:'85vh', textAlign:'center' }}>
        <div style={{ fontSize:72, marginBottom:16 }}>{emoji}</div>
        <h2 style={{ fontSize:22, fontWeight:800, marginBottom:4 }}>{t.result}</h2>
        <div style={{ fontSize:48, fontWeight:900, marginBottom:4,
          color: pct>=80?'var(--success)':pct>=50?'var(--warning)':'var(--danger)' }}>{pct}%</div>
        <div style={{ fontSize:16, color:'var(--tg-hint)', marginBottom:8 }}>{score} / {questions.length}</div>
        <div className="xp-chip" style={{ marginBottom:24 }}>⭐ +{score * 2} XP</div>
        <div style={{ display:'flex', flexDirection:'column', gap:10, width:'100%', maxWidth:300 }}>
          <button className="btn btn-primary" onClick={() => { setQIdx(0); setScore(0); setFinished(false); setSelected(null) }}>
            🔄 {t.tryAgain}
          </button>
          <button className="btn btn-secondary" onClick={() => navigate(`/lesson/${level}/${id}`)}>
            {t.backToLessons}
          </button>
        </div>
      </div>
    )
  }

  const q = questions[qIdx]
  const progress = (qIdx / questions.length) * 100

  // Render sentence with blank highlighted
  const parts = q.sentence.split('_____')
  const correctWord = q.opts[q.ans]

  return (
    <div className="page">
      {/* Header */}
      <div style={{ display:'flex', alignItems:'center', justifyContent:'space-between', marginBottom:12 }}>
        <button className="back-btn" onClick={() => navigate(`/lesson/${level}/${id}`)}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="15 18 9 12 15 6"/>
          </svg>
        </button>
        <div style={{ fontWeight:700, fontSize:13, color:'var(--tg-hint)' }}>
          ✍️ {qIdx + 1}/{questions.length}
        </div>
        <div style={{ fontWeight:800, color:'var(--success)', fontSize:16 }}>✓ {score}</div>
      </div>

      <div className="progress-bar" style={{ marginBottom:28 }}>
        <div className="progress-bar-fill" style={{ width:`${progress}%` }} />
      </div>

      {/* Sentence card */}
      <div className="card" style={{ padding:'24px 20px', marginBottom:24, textAlign:'center' }}>
        <div style={{ fontSize:12, color:'var(--tg-hint)', marginBottom:12, textTransform:'uppercase', letterSpacing:1 }}>
          {lang === 'uz' ? "Bo'sh joyni to'ldiring" : 'Вставьте пропущенное слово'}
        </div>

        <div style={{ fontSize:19, fontWeight:600, lineHeight:1.8 }}>
          {parts[0]}
          <span style={{
            display:'inline-block',
            minWidth:80,
            borderBottom: selected !== null
              ? `2.5px solid ${selected === q.ans ? 'var(--success)' : 'var(--danger)'}`
              : '2.5px solid var(--accent)',
            color: selected !== null
              ? (selected === q.ans ? 'var(--success)' : 'var(--danger)')
              : 'var(--accent)',
            fontWeight:800,
            padding:'0 4px',
            transition:'all .2s',
          }}>
            {selected !== null ? correctWord : '?'}
          </span>
          {parts[1] || ''}
        </div>

        {/* Hint: translation of blank word */}
        {q.hint && (
          <div style={{ fontSize:13, color:'var(--tg-hint)', marginTop:10 }}>
            💡 {q.hint}
          </div>
        )}

        {/* Speak original sentence after answering */}
        {selected !== null && q.original && (
          <button
            onClick={() => speakDE(q.original)}
            style={{ marginTop:12, background:'rgba(255,255,255,.07)', border:'1px solid rgba(255,255,255,.12)', borderRadius:10, padding:'6px 14px', cursor:'pointer', fontSize:16, color:'var(--tg-hint)' }}
          >
            🔊 {q.original}
          </button>
        )}
      </div>

      {/* Options */}
      {q.opts.map((opt, i) => {
        let bg = 'rgba(255,255,255,.05)'
        let border = 'rgba(255,255,255,.1)'
        let color = 'var(--tg-text)'

        if (selected !== null) {
          if (i === q.ans) { bg='var(--success-dim)'; border='rgba(34,197,94,.4)'; color='var(--success)' }
          else if (i === selected) { bg='var(--danger-dim)'; border='rgba(239,68,68,.4)'; color='var(--danger)' }
          else { color='rgba(255,255,255,.3)' }
        }

        return (
          <button key={i} onClick={() => handleAnswer(i)} style={{
            display:'block', width:'100%',
            padding:'15px 20px', marginBottom:10,
            borderRadius:14, border:`1.5px solid ${border}`,
            background:bg, color, fontWeight:700, fontSize:16,
            cursor: selected !== null ? 'default' : 'pointer',
            transition:'all .2s', textAlign:'left',
          }}>
            <span style={{
              display:'inline-flex', alignItems:'center', justifyContent:'center',
              width:26, height:26, borderRadius:'50%',
              background:'rgba(255,255,255,.08)',
              fontSize:12, fontWeight:800, marginRight:12,
            }}>
              {String.fromCharCode(65+i)}
            </span>
            {opt}
          </button>
        )
      })}

      {selected !== null && (
        <div style={{
          marginTop:4, padding:'12px 16px', borderRadius:12,
          background: selected===q.ans ? 'var(--success-dim)' : 'var(--danger-dim)',
          color: selected===q.ans ? 'var(--success)' : 'var(--danger)',
          fontWeight:700, textAlign:'center', fontSize:15,
        }}>
          {selected===q.ans ? `✓ ${t.correct}` : `✗ ${t.wrong} — ${correctWord}`}
        </div>
      )}
    </div>
  )
}
