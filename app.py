from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    intervals = data.get('intervals', [])
    
    if len(intervals) < 5:
        return jsonify({"status": "error", "message": "Need more data"})

    # DATA SCIENCE LOGIC
    # We use Coefficient of Variation (CV) = Standard Deviation / Mean
    # Higher CV indicates irregular typing rhythm, a strong sign of fatigue.
    mean_speed = np.mean(intervals)
    std_dev = np.std(intervals)
    
    # Calculate a fatigue percentage based on rhythm variance
    # A standard rhythm usually has a CV under 0.2 (20%). 
    # Anything above 0.35 (35%) is heavily fatigued.
    cv = std_dev / mean_speed
    fatigue_score = min(100, round(cv * 200, 1)) 
    
    is_fatigued = cv > 0.30

    return jsonify({
        "avg_speed": round(mean_speed, 2),
        "fatigue_score": fatigue_score,
        "is_fatigued": bool(is_fatigued),
        "message": "Fatigue Detected" if is_fatigued else "Focus is Stable"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
