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
import ExamPage from './pages/ExamPage'
import ExamLevelPage from './pages/ExamLevelPage'
import ExamDashboardPage from './pages/ExamDashboardPage'
import ExamInfoPage from './pages/ExamInfoPage'
import ExamLesenPage from './pages/ExamLesenPage'
import ExamTaskPage from './pages/ExamTaskPage'
import ExamSchreibenListPage from './pages/ExamSchreibenListPage'
import ExamSchreibenPage from './pages/ExamSchreibenPage'

const HIDE_NAV_PATHS = [
  '/lesson/', '/vocab/', '/test/', '/article/', '/match/', '/speed/',
  '/listen/', '/scramble/', '/fill/', '/order/',
  '/exam/',
]

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
        {/* Exam preparation module */}
        <Route path="/exam" element={<ExamPage />} />
        <Route path="/exam/:provider" element={<ExamLevelPage />} />
        <Route path="/exam/:provider/:level" element={<ExamDashboardPage />} />
        <Route path="/exam/:provider/:level/info" element={<ExamInfoPage />} />
        <Route path="/exam/:provider/:level/lesen" element={<ExamLesenPage />} />
        <Route path="/exam/:provider/:level/lesen/:taskId" element={<ExamTaskPage />} />
        <Route path="/exam/:provider/:level/schreiben" element={<ExamSchreibenListPage />} />
        <Route path="/exam/:provider/:level/schreiben/:taskId" element={<ExamSchreibenPage />} />
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
