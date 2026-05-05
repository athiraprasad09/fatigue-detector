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
        text_content = data.get('text', "").lower()
        
        # Code Detection: Keywords that signal professional work
        code_keywords = ['const', 'def', 'import', 'function', 'return', 'if', 'else', '{', '}', '=>', 'print']
        is_code = any(keyword in text_content for keyword in code_keywords)
        
        if not is_code and len(text_content) > 15:
            return jsonify({
                "status": "INPUT ERROR", 
                "suggestion": "Analysis invalid. Please input computer code (Python, JS, C++, etc.) to measure engineering flow."
            })

        if len(intervals) < 12:
            return jsonify({"status": "COLLECTING DATA", "suggestion": "Continue typing code to calibrate sensors..."})

        avg_speed = statistics.mean(intervals)
        variation = statistics.stdev(intervals) # Jitter detection

        # Logic for Fatigue Levels
        if backspaces > (len(intervals) * 0.25): # High error rate
            status = "CRITICAL STRESS"
            suggestion = "System Overload. Try Box Breathing (4s inhale, 4s hold, 4s exhale) immediately."
        elif avg_speed > 350 or variation > 150: # Slow or jittery typing
            status = "COGNITIVE FATIGUE"
            suggestion = "Focus is drifting. Apply the 20-20-20 rule: look 20ft away for 20s."
        elif avg_speed < 180: # Fast, consistent typing
            status = "OPTIMAL FLOW"
            suggestion = "Peak performance detected. Stay hydrated and maintain this rhythm."
        else:
            status = "STABLE / NORMAL"
            suggestion = "Steady progress. Consider a short stretch in 15 minutes."

        return jsonify({
            "fatigue_score": int((variation / avg_speed) * 100) if avg_speed > 0 else 0,
            "status": status,
            "suggestion": suggestion
        })
    except Exception:
        return jsonify({"error": "Internal Sensor Error"}), 500

if __name__ == '__main__':
    app.run(debug=False)
