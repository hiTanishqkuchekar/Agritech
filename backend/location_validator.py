import pandas as pd
import os

# project root path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# csv path
CSV_PATH = os.path.join(BASE_DIR, "data", "synthetic_farmers_final.csv")

df = pd.read_csv(CSV_PATH)

def validate_location(district, village):
    match = df[
        (df["district"].str.lower() == district.lower()) &
        (df["village"].str.lower() == village.lower())
    ]
    return not match.empty

