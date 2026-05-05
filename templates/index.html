<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cognitive Fatigue Detector | Engineer Edition</title>
    <style>
        :root { --purple: #6c5ce7; --bg: #7f7fd5; --text-main: #2d3436; }
        body { 
            font-family: 'Inter', system-ui, -apple-system, sans-serif; 
            background: linear-gradient(135deg, var(--bg), #86a8e7, #91eae4); 
            height: 100vh; margin: 0; display: flex; justify-content: center; align-items: center; 
        }
        .card { 
            background: white; padding: 2.5rem; border-radius: 24px; 
            box-shadow: 0 20px 40px rgba(0,0,0,0.15); width: 95%; max-width: 650px; 
        }
        .header { display: flex; align-items: center; gap: 12px; margin-bottom: 5px; }
        h1 { margin: 0; font-size: 1.8rem; color: var(--text-main); letter-spacing: -0.5px; }
        .sub-status { color: #00b894; font-size: 0.85rem; margin-bottom: 25px; display: flex; align-items: center; gap: 6px; font-weight: 500; }
        .dot { height: 8px; width: 8px; background-color: #00b894; border-radius: 50%; display: inline-block; animation: blink 1.5s infinite; }
        @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }

        .stats-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-bottom: 25px; }
        .stat-box { background: #f8f9fc; padding: 15px; border-radius: 14px; border: 1px solid #edf2f7; text-align: center; transition: 0.3s; }
        .stat-val { display: block; font-size: 1.3rem; font-weight: 800; color: var(--purple); }
        .stat-label { font-size: 0.65rem; text-transform: uppercase; color: #a0aec0; letter-spacing: 1px; font-weight: 700; margin-top: 4px; }

        textarea { 
            width: 100%; height: 180px; border: 2px solid #edf2f7; border-radius: 16px; 
            padding: 18px; font-size: 1rem; resize: none; box-sizing: border-box; 
            transition: all 0.3s ease; font-family: 'Fira Code', monospace; line-height: 1.6;
        }
        textarea:focus { outline: none; border-color: var(--purple); box-shadow: 0 0 0 4px rgba(108, 92, 231, 0.1); }
        
        .btn { 
            background: linear-gradient(90deg, #6c5ce7, #a29bfe); color: white; border: none; 
            padding: 16px; border-radius: 14px; width: 100%; font-size: 1rem; font-weight: 700; 
            cursor: pointer; margin-top: 20px; transition: 0.3s; box-shadow: 0 4px 15px rgba(108, 92, 231, 0.3);
        }
        .btn:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(108, 92, 231, 0.4); }
        
        #result-container { margin-top: 25px; padding: 20px; border-radius: 14px; display: none; text-align: center; }
        .status-title { font-size: 1.4rem; margin-bottom: 8px; }
        .suggestion-text { font-size: 0.95rem; color: #4a5568; line-height: 1.5; }
    </style>
</head>
<body>

    <div class="card">
        <div class="header">
            <span style="font-size: 2rem;">🧠</span>
            <h1>Cognitive Fatigue Detector</h1>
        </div>
        <div class="sub-status"><span class="dot"></span> Real-time typing pattern analysis</div>
        
        <!-- Dashboard Stats -->
        <div class="stats-grid">
            <div class="stat-box">
                <span class="stat-val" id="keystrokes">0</span>
                <span class="stat-label">Keystrokes</span>
            </div>
            <div class="stat-box">
                <span class="stat-val" id="avg-speed">-</span>
                <span class="stat-label">Avg Speed (ms)</span>
            </div>
            <div class="stat-box">
                <span class="stat-val" id="timer">0s</span>
                <span class="stat-label">Session Time</span>
            </div>
        </div>

        <textarea id="typingArea" placeholder="Start typing your code or thoughts here... The system monitors speed and errors to detect fatigue."></textarea>
        
        <button class="btn" onclick="analyzeFatigue()">🔍 Analyze Fatigue Level</button>
        
        <div id="result-container">
            <div id="status-display" class="status-title"></div>
            <div id="suggestion-display" class="suggestion-text"></div>
        </div>
    </div>

    <script>
        let lastKeyTime;
        let intervals = [];
        let backspaceCount = 0;
        let startTime = Date.now();
        let keystrokeCount = 0;

        // Session Timer
        setInterval(() => {
            const seconds = Math.floor((Date.now() - startTime) / 1000);
            document.getElementById('timer').innerText = seconds + "s";
        }, 1000);

        const area = document.getElementById('typingArea');
        area.addEventListener('keydown', (e) => {
            const now = Date.now();
            keystrokeCount++;
            document.getElementById('keystrokes').innerText = keystrokeCount;

            if (e.key === 'Backspace') {
                backspaceCount++;
            }

            if (lastKeyTime) {
                const interval = now - lastKeyTime;
                // Ignore long pauses (over 2 seconds) to keep data clean
                if (interval < 2000) {
                    intervals.push(interval);
                    const avg = Math.round(intervals.reduce((a, b) => a + b) / intervals.length);
                    document.getElementById('avg-speed').innerText = avg;
                }
            }
            lastKeyTime = now;
        });

        async function analyzeFatigue() {
            if (intervals.length < 10) {
                alert("Please type a bit more (at least 10 keystrokes) for an accurate reading!");
                return;
            }

            const res = await fetch('/analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 
                    intervals: intervals,
                    backspaces: backspaceCount 
                })
            });
            
            const data = await res.json();
            const container = document.getElementById('result-container');
            const statusDiv = document.getElementById('status-display');
            const suggestDiv = document.getElementById('suggestion-display');

            container.style.display = "block";
            statusDiv.innerText = "Status: " + data.status;
            suggestDiv.innerText = "💡 " + data.suggestion;

            // Dynamic Styling based on status
            if (data.status.includes("Energetic")) {
                container.style.background = "#f0fff4";
                statusDiv.style.color = "#38a169";
            } else if (data.status.includes("Stressed")) {
                container.style.background = "#fff5f5";
                statusDiv.style.color = "#e53e3e";
            } else {
                container.style.background = "#fffaf0";
                statusDiv.style.color = "#dd6b20";
            }
        }
    </script>
</body>
</html>
