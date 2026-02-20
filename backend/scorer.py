def calculate_score(farmer, scheme):
    score = 0

    if farmer["land_size"] <= scheme["max_land"]:
        score += 40

    if farmer["income"] <= scheme["max_income"]:
        score += 30

    matched = set(farmer["documents"]) & set(scheme["required_documents"])
    score += int((len(matched) / len(scheme["required_documents"])) * 30)

    return score
