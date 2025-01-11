// ChatBox — textarea input with animated submit button
import { useState } from 'react'
import { motion } from 'framer-motion'

export default function ChatBox({ onSubmit, loading }) {
  const [question, setQuestion] = useState('')

  function handleSubmit(e) {
    e.preventDefault()
    if (question.trim() && !loading) {
      onSubmit(question.trim())
    }
  }

  return (
    <form className="chatbox" onSubmit={handleSubmit}>
      <textarea
        className="chatbox__input"
        placeholder="Ask a medical question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        rows={3}
        disabled={loading}
        onKeyDown={(e) => {
          if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault()
            handleSubmit(e)
          }
        }}
      />
      <motion.button
        type="submit"
        className="chatbox__btn"
        disabled={loading || !question.trim()}
        whileTap={{ scale: 0.96 }}
        whileHover={{ scale: 1.02 }}
      >
        {loading ? (
          <span className="btn-spinner" />
        ) : (
          'Ask MediMind 🧠'
        )}
      </motion.button>
    </form>
  )
}
