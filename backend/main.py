from fastapi import FastAPI, HTTPException
from agent import ai_agent_decision
from location_validator import validate_location

app = FastAPI(title="Agritech AI Agent")

@app.post("/recommend")
def recommend_scheme(farmer: dict):

    required_fields = ["land_size", "income", "village", "district", "documents"]
    for field in required_fields:
        if field not in farmer:
            raise HTTPException(status_code=400, detail=f"{field} is required")

    # location validation using dataset
    if not validate_location(farmer["district"], farmer["village"]):
        raise HTTPException(
            status_code=400,
            detail="Invalid village–district combination"
        )

    return ai_agent_decision(farmer)
@app.get("/")
def root():
    return {"message": "Agritech AI Agent is running"}
