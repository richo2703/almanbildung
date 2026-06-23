import { BrowserRouter, Routes, Route, useLocation } from 'react-router-dom'
import { LangProvider, useLang } from './LangContext'
import BottomNav from './components/BottomNav'
import OnboardingPage from './pages/OnboardingPage'
import HomePage from './pages/HomePage'
import LevelsPage from './pages/LevelsPage'
import LessonsPage from './pages/LessonsPage'
import LessonPage from './pages/LessonPage'
import VocabPage from './pages/VocabPage'
import TestPage from './pages/TestPage'
import ArticlePage from './pages/ArticlePage'
import MatchPage from './pages/MatchPage'
import SpeedPage from './pages/SpeedPage'
import ListenPage from './pages/ListenPage'
import ScramblePage from './pages/ScramblePage'
import FillPage from './pages/FillPage'
import OrderPage from './pages/OrderPage'
import ProgressPage from './pages/ProgressPage'
import SettingsPage from './pages/SettingsPage'

const HIDE_NAV_PATHS = ['/lesson/', '/vocab/', '/test/', '/article/', '/match/', '/speed/', '/listen/', '/scramble/', '/fill/', '/order/']

function Layout() {
  const { lang } = useLang()
  const location = useLocation()

  if (!lang) return <OnboardingPage />

  const hideNav = HIDE_NAV_PATHS.some(p => location.pathname.includes(p))

  return (
    <>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/learn" element={<LevelsPage />} />
        <Route path="/learn/:level" element={<LessonsPage />} />
        <Route path="/lesson/:level/:id" element={<LessonPage />} />
        <Route path="/vocab/:level/:id" element={<VocabPage />} />
        <Route path="/test/:level/:id" element={<TestPage />} />
        <Route path="/article/:level/:id" element={<ArticlePage />} />
        <Route path="/match/:level/:id" element={<MatchPage />} />
        <Route path="/speed/:level/:id" element={<SpeedPage />} />
        <Route path="/listen/:level/:id" element={<ListenPage />} />
        <Route path="/scramble/:level/:id" element={<ScramblePage />} />
        <Route path="/fill/:level/:id" element={<FillPage />} />
        <Route path="/order/:level/:id" element={<OrderPage />} />
        <Route path="/progress" element={<ProgressPage />} />
        <Route path="/settings" element={<SettingsPage />} />
      </Routes>
      {!hideNav && <BottomNav />}
    </>
  )
}

export default function App() {
  return (
    <LangProvider>
      <BrowserRouter>
        <Layout />
      </BrowserRouter>
    </LangProvider>
  )
}
