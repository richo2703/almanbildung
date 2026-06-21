const BASE = import.meta.env.VITE_API_URL || ''

function getInitData() {
  return window.Telegram?.WebApp?.initData || ''
}

async function request(path, options = {}) {
  const res = await fetch(`${BASE}${path}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      'x-init-data': getInitData(),
      ...(options.headers || {}),
    },
  })
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: res.statusText }))
    throw new Error(err.detail || 'API error')
  }
  return res.json()
}

export const api = {
  // Content
  getLevels: () => request('/api/levels'),
  getLessons: (level) => request(`/api/levels/${level}/lessons`),
  getLesson: (level, id) => request(`/api/levels/${level}/lessons/${id}`),
  getLessonVocab: (level, id) => request(`/api/levels/${level}/lessons/${id}/vocab`),
  getLessonExercises: (level, id) => request(`/api/levels/${level}/lessons/${id}/exercises`),
  getLevelVocab: (level) => request(`/api/levels/${level}/vocab`),

  // User
  getMe: () => request('/api/me'),
  setLang: (lang) => request('/api/me/lang', { method: 'POST', body: JSON.stringify({ lang }) }),
  getLevelProgress: (level) => request(`/api/me/progress/${level}`),

  // Actions
  markLessonDone: (level, lesson_id, score = 0, max_score = 0) =>
    request('/api/me/lesson-done', {
      method: 'POST',
      body: JSON.stringify({ level, lesson_id, score, max_score }),
    }),
  markVocab: (level, word_de, known) =>
    request('/api/me/vocab', {
      method: 'POST',
      body: JSON.stringify({ level, word_de, known }),
    }),
  saveTestResult: (level, lesson_id, score, max_score) =>
    request('/api/me/test-result', {
      method: 'POST',
      body: JSON.stringify({ level, lesson_id, score, max_score }),
    }),
}
