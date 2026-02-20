import pandas as pd
import numpy as np

# load existing synthetic data
df = pd.read_csv("synthetic_farmers.csv")

# -----------------------------
# REGION-WISE DISTRICT → TALUKA → VILLAGES
# -----------------------------

location_map = {

    # 🔵 KONKAN
    "Raigad": {
        "Alibag": ["Varsoli", "Revdanda", "Chaul"],
        "Mahad": ["Dasgaon", "Birwadi", "Kamble"],
        "Panvel": ["Kalamboli", "Kamothe", "Karanjade"]
    },

    # 🔵 PUNE SIDE (Western MH)
    "Pune": {
        "Ambegaon": ["Manchar", "Ghodegaon", "Awasari"],
        "Junnar": ["Otur", "Alephata", "Narayangaon"],
        "Haveli": ["Wagholi", "Theur", "Uruli"]
    },

    "Satara": {
        "Karad": ["Umbraj", "Masur", "Malkapur"],
        "Phaltan": ["Lonand", "Sakharwadi", "Nimb"],
        "Wai": ["Dhom", "Kikali", "Bavdhan"]
    },

    # 🔵 MARATHWADA
    "Aurangabad": {
        "Paithan": ["Bidkin", "Waluj", "Patoda"],
        "Gangapur": ["Shendra", "Lasur", "Banewadi"],
        "Sillod": ["Ajanta", "Andhari", "Golegaon"]
    },

    "Nanded": {
        "Biloli": ["Kundalwadi", "Sawargaon", "Hadsani"],
        "Degloor": ["Mukramabad", "Kangti", "Gokunda"],
        "Mukhed": ["Pimpalgaon", "Honer", "Dapkarja"]
    },

    "Beed": {
        "Georai": ["Bansarola", "Kada", "Thakarwadi"],
        "Ashti": ["Kasewadi", "Pimpri", "Dhanora"],
        "Patoda": ["Chousala", "Jaulkhed", "Therla"]
    },

    # ✅ PARBHANI (ADDED)
    "Parbhani": {
        "Purna": ["Dhanora", "Saykheda", "Golegaon"],
        "Pathri": ["Takli", "Rampuri", "Babhulgaon"],
        "Gangakhed": ["Malewadi", "Kondhar", "Mardasgaon"]
    },

    # 🔵 VIDARBHA
    "Nagpur": {
        "Katol": ["Sawanga", "Metpanjara", "Dhapewada"],
        "Hingna": ["Wanadongri", "Raipur", "Takli"],
        "Kalmeshwar": ["Mohpa", "Kohali", "Gondkhairi"]
    },

    "Amravati": {
        "Achalpur": ["Paratwada", "Pathrot", "Dhamangaon"],
        "Daryapur": ["Anjangaon", "Mangrul", "Yeoda"],
        "Chandur": ["Kurha", "Nandgaon", "Rajura"]
    },

    "Solapur": {
        "Pandharpur": ["Bhalwani", "Kasegaon", "Mundhewadi"],
        "Barshi": ["Vairag", "Tadsoundane", "Sukewadi"],
        "Mohol": ["Shirapur", "Penur", "Kamti"]
    },
      
        
    "Kolhapur": {
        "Karvir": ["Uchgaon", "Kalamba", "Shiroli"],
        "Hatkanangale": ["Pethvadgaon", "Jaysingpur", "Hupari"],
        "Radhanagari": ["Kasba Radhanagari", "Dhamod", "Gargoti"]
    },

}

# -----------------------------
# ADD TALUKA & VILLAGE
# -----------------------------
def assign_taluka(district):
    if district in location_map:
        talukas = list(location_map[district].keys())
        return np.random.choice(talukas)
    else:
        return "Unknown"

def assign_village(district, taluka):
    if district in location_map and taluka in location_map[district]:
        villages = location_map[district][taluka]
        return np.random.choice(villages)
    else:
        return "Unknown"


df["taluka"] = df["district"].apply(assign_taluka)

df["village"] = df.apply(
    lambda r: assign_village(r["district"], r["taluka"]),
    axis=1
)

# save final dataset
df.to_csv("synthetic_farmers_final.csv", index=False)

print("✅ FINAL DATASET CREATED : synthetic_farmers_final.csv")
