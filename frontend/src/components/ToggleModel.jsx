// ToggleModel — switch between side-by-side, base-only, finetuned-only views
export default function ToggleModel({ active, onChange }) {
  return (
    <div className="toggle-model">
      <button
        className={`toggle-btn ${active === 'both' ? 'toggle-btn--active' : ''}`}
        onClick={() => onChange('both')}
      >
        Side by Side
      </button>
      <button
        className={`toggle-btn ${active === 'base' ? 'toggle-btn--active' : ''}`}
        onClick={() => onChange('base')}
      >
        Base Only
      </button>
      <button
        className={`toggle-btn ${active === 'finetuned' ? 'toggle-btn--active' : ''}`}
        onClick={() => onChange('finetuned')}
      >
        Fine-Tuned Only
      </button>
    </div>
  )
}
