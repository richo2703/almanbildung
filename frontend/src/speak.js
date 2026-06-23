/**
 * Web Speech API — German pronunciation utility
 */

let currentUtterance = null

export function speak(text, langCode = 'de-DE', rate = 0.85) {
  if (!window.speechSynthesis) return

  // Cancel any ongoing speech
  window.speechSynthesis.cancel()

  const utt = new SpeechSynthesisUtterance(text)
  utt.lang = langCode
  utt.rate = rate
  utt.pitch = 1.0
  utt.volume = 1.0

  currentUtterance = utt
  window.speechSynthesis.speak(utt)
}

export function speakDE(text) {
  speak(text, 'de-DE', 0.85)
}

export function stopSpeech() {
  if (window.speechSynthesis) {
    window.speechSynthesis.cancel()
  }
}

export function isSpeechSupported() {
  return 'speechSynthesis' in window
}
