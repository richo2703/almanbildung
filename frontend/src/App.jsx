import { BrowserRouter, Routes, Route, useLocation } from 'react-router-dom'
import BottomNav from './components/BottomNav'
import HomePage from './pages/HomePage'
import LevelsPage from './pages/LevelsPage'
import LessonsPage from './pages/LessonsPage'
import LessonPage from './pages/LessonPage'
import VocabPage from './pages/VocabPage'
import TestPage from './pages/TestPage'
import ProgressPage from './pages/ProgressPage'

function Layout() {
  const location = useLocation()
  const hideNav = ['/lesson/', '/vocab/', '/test/'].some(p => location.pathname.includes(p))

  return (
    <>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/learn" element={<LevelsPage />} />
        <Route path="/learn/:level" element={<LessonsPage />} />
        <Route path="/lesson/:level/:id" element={<LessonPage />} />
        <Route path="/vocab/:level/:id" element={<VocabPage />} />
        <Route path="/test/:level/:id" element={<TestPage />} />
        <Route path="/progress" element={<ProgressPage />} />
      </Routes>
      {!hideNav && <BottomNav />}
    </>
  )
}

export default function App() {
  return (
    <BrowserRouter>
      <Layout />
    </BrowserRouter>
  )
}
