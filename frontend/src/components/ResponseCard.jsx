// ResponseCard — displays model answer with variant styling (base/finetuned)
import { motion } from 'framer-motion'

export default function ResponseCard({ title, answer, variant }) {
  return (
    <motion.div
      className={`response-card response-card--${variant}`}
      initial={{ opacity: 0, y: 24 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.45 }}
    >
      <div className="response-card__header">
        <span className="response-card__badge">{variant === 'base' ? '🤖' : '✨'}</span>
        <h3 className="response-card__title">{title}</h3>
      </div>
      <p className="response-card__body">{answer}</p>
    </motion.div>
  )
}
