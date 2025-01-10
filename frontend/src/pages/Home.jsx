import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import ChatBox from '../components/ChatBox'
import ResponseCard from '../components/ResponseCard'
import ToggleModel from '../components/ToggleModel'
import Loader from '../components/Loader'
import { askQuestion } from '../services/api'

export default function Home() {
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)
  const [view, setView] = useState('both')

  async function handleSubmit(question) {
    setLoading(true)
    setError(null)
    setResult(null)
    try {
      const data = await askQuestion(question)
      setResult(data)
    } catch (err) {
      setError(err?.response?.data?.detail || 'Something went wrong. Is the backend running?')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="home">
      <motion.header
        className="header"
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <h1 className="header__title">MediMind AI 🧠</h1>
        <p className="header__subtitle">
          Base vs Fine-Tuned flan-t5 — Medical Q&A Comparison
        </p>
      </motion.header>

      <main className="main">
        <ChatBox onSubmit={handleSubmit} loading={loading} />

        <AnimatePresence>
          {loading && <Loader key="loader" />}

          {error && (
            <motion.div
              key="error"
              className="error-banner"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
            >
              ⚠️ {error}
            </motion.div>
          )}

          {result && !loading && (
            <motion.section
              key="results"
              className="results"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 0.4 }}
            >
              <div className="results__question">
                <span className="results__question-label">Your question</span>
                <p>{result.question}</p>
              </div>

              <ToggleModel active={view} onChange={setView} />

              <div className={`results__grid ${view !== 'both' ? 'results__grid--single' : ''}`}>
                {(view === 'both' || view === 'base') && (
                  <ResponseCard
                    title="Base Model (flan-t5-base)"
                    answer={result.base_answer}
                    variant="base"
                  />
                )}
                {(view === 'both' || view === 'finetuned') && (
                  <ResponseCard
                    title="Fine-Tuned (Medical)"
                    answer={result.finetuned_answer}
                    variant="finetuned"
                  />
                )}
              </div>
            </motion.section>
          )}
        </AnimatePresence>
      </main>
    </div>
  )
}
