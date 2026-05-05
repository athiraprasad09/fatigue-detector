from flask import Flask, render_template, request, jsonify
import statistics

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        intervals = data.get('intervals', [])
        backspaces = data.get('backspaces', 0)
        
        if len(intervals) < 10:
            return jsonify({"status": "Keep typing...", "suggestion": "Need more data."})

        avg_speed = statistics.mean(intervals)
        
        # 1. Stress Detection (High Backspaces/Corrections)
        if backspaces > (len(intervals) * 0.3):
            status = "Highly Stressed"
            suggestion = "Try the 4-7-8 Breathing Technique: Inhale for 4s, hold for 7s, exhale for 8s."
        
        # 2. Fatigue Detection (Slow typing > 300ms per key)
        elif avg_speed > 300:
            status = "Tired / Fatigued"
            suggestion = "20-20-20 Rule: Every 20 mins, look at something 20 feet away for 20 seconds."
            
        # 3. Energetic (Fast typing < 150ms per key)
        else:
            status = "Energetic / In Flow"
            suggestion = "You're in the zone! Keep going, but remember to hydrate."

        return jsonify({
            "fatigue_score": int(avg_speed / 10),
            "status": status,
            "suggestion": suggestion
        })
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500
