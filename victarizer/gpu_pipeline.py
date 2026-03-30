import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import IsolationForest

# Step 1: Read logs
def read_logs(file):
    with open(file, "r") as f:
        return [line.strip() for line in f]

# Step 2: Process logs
def process_logs(logs):
    data = []

    for log in logs:
        # Extract FPS
        if "fps" in log:
            fps = int(log.split("=")[1])
        else:
            fps = None

        # Detect status
        if any(word in log.lower() for word in ["crash", "timeout", "tdr"]):
            status = "fail"
        else:
            status = "pass"

        data.append((log, fps, status))

    return data

# Step 3: Create DB
def create_db():
    conn = sqlite3.connect("gpu_logs.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        log TEXT,
        fps INTEGER,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()

# Step 4: Insert into DB
def insert_data(data):
    conn = sqlite3.connect("gpu_logs.db")
    cursor = conn.cursor()

    for row in data:
        cursor.execute(
            "INSERT INTO logs (log, fps, status) VALUES (?, ?, ?)",
            row
        )

    conn.commit()
    conn.close()

# Step 5: AI - TF-IDF + Isolation Forest
def detect_anomalies(logs):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(logs)

    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(X)

    preds = model.predict(X)

    anomalies = [log for log, p in zip(logs, preds) if p == -1]
    return anomalies

# Step 6: Analysis
def analyze_db():
    conn = sqlite3.connect("gpu_logs.db")
    cursor = conn.cursor()

    print("\n===== DATABASE ANALYSIS =====")

    cursor.execute("SELECT COUNT(*) FROM logs")
    print("Total Logs:", cursor.fetchone()[0])

    cursor.execute("SELECT COUNT(*) FROM logs WHERE status='fail'")
    print("Fail Logs:", cursor.fetchone()[0])

    cursor.execute("SELECT AVG(fps) FROM logs WHERE fps IS NOT NULL")
    print("Average FPS:", cursor.fetchone()[0])

    conn.close()

# Main
def main():
    file = "gpu.log"

    logs = read_logs(file)
    data = process_logs(logs)

    create_db()
    insert_data(data)

    anomalies = detect_anomalies(logs)

    analyze_db()

    print("\n===== AI DETECTED ANOMALIES =====")
    for log in anomalies[:10]:
        print(log)

if __name__ == "__main__":
    main()