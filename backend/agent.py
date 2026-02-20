import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SCHEME_PATH = os.path.join(BASE_DIR, "schemes", "schemes.json")

def load_schemes():
    with open(SCHEME_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def ai_agent_decision(farmer):
    schemes = load_schemes()
    results = []

    for scheme in schemes:
        eligible, reasons = check_eligibility(farmer, scheme)
        score = calculate_score(farmer, scheme)

        status = "Eligible" if eligible else "Not Eligible"

        results.append({
            "scheme_id": scheme["scheme_id"],
            "scheme_name": scheme["name"],
            "status": status,
            "readiness_score": score,
            "reasons": reasons,
            "benefit": scheme["benefit"],
            "apply_mode": scheme["apply_mode"],
            "next_steps": scheme["apply_steps"],
            "deadline": scheme["deadline"]
        })

    return {
        "farmer_profile": {
            "district": farmer["district"],
            "village": farmer["village"]
        },
        "recommendations": results
    }
