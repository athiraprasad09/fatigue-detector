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
        
        if len(intervals) < 10:
            return jsonify({"fatigue_score": 0, "status": "Need more data"})

        # Logic for Software Engineer Fatigue:
        # We look at 'Consistency'. Tired engineers have 'jittery' typing.
        avg_speed = statistics.mean(intervals)
        variation = statistics.stdev(intervals)
        
        # Calculate a score out of 100
        # A high variation (jitter) + slow speed = High Fatigue
        raw_score = (variation / avg_speed) * 100
        fatigue_score = min(100, int(raw_score * 2))

        # Determine professional status
        if fatigue_score > 75:
            status = "Burnout Warning: Take a Break"
        elif fatigue_score > 45:
            status = "Moderate Fatigue: Consider Coffee"
        else:
            status = "Optimal Flow: Focused"

        return jsonify({
            "fatigue_score": fatigue_score,
            "status": status
        })
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=False)
