/**
 * TTS utility — priority:
 *   1. Backend /api/tts  (Google Translate proxy — natural voice)
 *   2. Best available browser voice for de-DE
 *   3. Generic Web Speech API fallback
 */

// ----- audio pool to avoid re-creating Audio objects -----
let currentAudio = null

// Cache for the best German browser voice (resolved once)
let _bestVoiceCache = undefined

function getBestGermanVoice() {
  if (_bestVoiceCache !== undefined) return _bestVoiceCache
  const voices = window.speechSynthesis?.getVoices() || []
  if (!voices.length) { _bestVoiceCache = null; return null }

  // Prefer enhanced / neural / premium voices first
  const quality = ['Neural', 'Enhanced', 'Premium', 'Natural', 'HD']
  for (const q of quality) {
    const v = voices.find(v => v.lang.startsWith('de') && v.name.includes(q))
    if (v) { _bestVoiceCache = v; return v }
  }
  // Named high-quality voices known to sound good
  const named = ['Anna', 'Hedda', 'Helena', 'Marlene', 'Petra', 'Yannick', 'Markus']
  for (const n of named) {
    const v = voices.find(v => v.lang.startsWith('de') && v.name.includes(n))
    if (v) { _bestVoiceCache = v; return v }
  }
  // Any de-DE
  const any = voices.find(v => v.lang === 'de-DE') || voices.find(v => v.lang.startsWith('de'))
  _bestVoiceCache = any || null
  return _bestVoiceCache
}

// Re-resolve voice after voices list loads (async on some browsers)
if (typeof window !== 'undefined' && window.speechSynthesis) {
  window.speechSynthesis.onvoiceschanged = () => { _bestVoiceCache = undefined }
}

// ----- browser speech fallback -----
function speakBrowser(text) {
  if (!window.speechSynthesis) return
  window.speechSynthesis.cancel()
  const utt = new SpeechSynthesisUtterance(text)
  utt.lang = 'de-DE'
  utt.rate = 0.85
  utt.pitch = 1.0
  utt.volume = 1.0
  const voice = getBestGermanVoice()
  if (voice) utt.voice = voice
  window.speechSynthesis.speak(utt)
}

// ----- main public API -----

/**
 * Speak a German word/phrase.
 * Tries backend Google TTS first; on failure falls back to browser voice.
 */
export function speakDE(text) {
  if (!text) return

  // Stop any currently playing audio
  if (currentAudio) {
    currentAudio.pause()
    currentAudio.src = ''
    currentAudio = null
  }
  if (window.speechSynthesis) window.speechSynthesis.cancel()

  const encoded = encodeURIComponent(text)
  const audio = new Audio(`/api/tts?q=${encoded}`)
  audio.preload = 'auto'
  currentAudio = audio

  audio.play().catch(() => {
    // Backend unavailable — fall back to browser voice
    speakBrowser(text)
  })
}

export function stopSpeech() {
  if (currentAudio) {
    currentAudio.pause()
    currentAudio.src = ''
    currentAudio = null
  }
  window.speechSynthesis?.cancel()
}

export function isSpeechSupported() {
  // Always true — we have at least browser TTS
  return typeof Audio !== 'undefined' || 'speechSynthesis' in window
}
