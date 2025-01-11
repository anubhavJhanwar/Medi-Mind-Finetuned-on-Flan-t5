// Animated loading indicator shown during model inference
import { motion } from 'framer-motion'

export default function Loader() {
  return (
    <div className="loader-container">
      <div className="loader-dots">
        {[0, 1, 2].map((i) => (
          <motion.span
            key={i}
            className="loader-dot"
            animate={{ y: [0, -12, 0] }}
            transition={{ duration: 0.6, repeat: Infinity, delay: i * 0.15 }}
          />
        ))}
      </div>
      <p className="loader-text">MediMind is thinking...</p>
    </div>
  )
}
