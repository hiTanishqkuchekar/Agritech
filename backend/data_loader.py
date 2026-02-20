import pandas as pd

df = pd.read_csv("synthetic_farmers_final.csv")

def get_farmer_by_id(farmer_id: int):
    farmer = df[df["farmer_id"] == farmer_id]
    if farmer.empty:
        return None

    row = farmer.iloc[0]

    # backend-friendly format
    return {
        "farmer_id": int(row["farmer_id"]),
        "land_size": float(row["land_holding_acres"]),
        "income": int(row["annual_income"]),
        "state": row["state"],
        "district": row["district"],
        "crop": row["crop"],
        "farmer_category": row["farmer_category"],
        # assume basic documents for demo
        "documents": ["aadhaar", "land_record", "bank_account"]
    }
