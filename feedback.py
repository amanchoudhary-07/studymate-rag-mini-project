import json
from datetime import datetime

def collect_feedback(question, answer, rating):
    record = {
        "timestamp": str(datetime.now()),
        "question": question,
        "answer": answer,
        "rating": rating
    }

    with open("feedback_store.json", "a") as f:
        f.write(json.dumps(record) + "\n")
