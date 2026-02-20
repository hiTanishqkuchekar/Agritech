def check_eligibility(farmer, scheme):
    reasons = []
    eligible = True

    if farmer["land_size"] > scheme["max_land"]:
        eligible = False
        reasons.append("Land size exceeds scheme limit")

    if farmer["income"] > scheme["max_income"]:
        eligible = False
        reasons.append("Income exceeds scheme limit")

    missing = set(scheme["required_documents"]) - set(farmer["documents"])
    if missing:
        reasons.append("Missing documents: " + ", ".join(missing))

    return eligible, reasons
