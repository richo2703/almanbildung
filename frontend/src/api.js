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

  // ── Exam preparation ─────────────────────────────────────────────────────
  exam: {
    getProviders: () => request('/api/exam/providers'),
    getProvider: (name) => request(`/api/exam/providers/${name}`),
    getLevels: (provider) => request(`/api/exam/${provider}/levels`),
    getLevelInfo: (provider, level) => request(`/api/exam/${provider}/${level}`),
    getSections: (provider, level) => request(`/api/exam/${provider}/${level}/sections`),
    getSection: (provider, level, type) => request(`/api/exam/${provider}/${level}/sections/${type}`),
    getTasks: (sectionId) => request(`/api/exam/sections/${sectionId}/tasks`),
    getTask: (taskId) => request(`/api/exam/tasks/${taskId}`),
    submitAttempt: (taskId, answers) =>
      request(`/api/exam/tasks/${taskId}/attempt`, {
        method: 'POST',
        body: JSON.stringify({ answers }),
      }),
    getProgress: (provider, level) => request(`/api/exam/me/${provider}/${level}/progress`),
    submitWriting: (taskId, userText) =>
      request('/api/exam/writing/submit', {
        method: 'POST',
        body: JSON.stringify({ task_id: taskId, user_text: userText }),
      }),
    getLatestWriting: (taskId) => request(`/api/exam/writing/${taskId}/latest`),
  },
}
