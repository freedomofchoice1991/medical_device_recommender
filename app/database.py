import sqlite3
import requests

# FDA API Endpoint for medical device classification
FDA_API_URL = "https://api.fda.gov/device/classification.json?limit=1000"

# SQLite Database File
DB_FILE = "medical_devices.db"


def create_database():
    """Creates the SQLite database and classification table if not exists."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Creating table to store classification data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS classifications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_code TEXT UNIQUE,
            device_name TEXT,
            medical_specialty TEXT,
            regulation_number TEXT,
            classification_name TEXT,
            classification_code TEXT
        )
    """)

    conn.commit()
    conn.close()


def fetch_fda_data():
    """Fetches medical device classification data from the FDA API."""
    response = requests.get(FDA_API_URL)

    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print("Error fetching data:", response.status_code)
        return []


def store_data(data):
    """Stores the fetched classification data into SQLite."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    for item in data:
        cursor.execute("""
            INSERT OR IGNORE INTO classifications (product_code, device_name, medical_specialty, regulation_number, classification_name, classification_code)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            item.get("product_code", ""),
            item.get("device_name", ""),
            item.get("medical_specialty_description", ""),
            item.get("regulation_number", ""),
            item.get("classification_name", ""),
            item.get("review_panel", "")  # Storing review panel as classification_code for grouping
        ))

    conn.commit()
    conn.close()


def initialize_db():
    """Runs database setup and fetches/stores FDA classification data."""
    create_database()
    data = fetch_fda_data()

    if data:
        store_data(data)
        print("✅ Data successfully stored in SQLite3!")
    else:
        print("⚠️ No data to store!")


# Run this only when executing the script directly
if __name__ == "__main__":
    initialize_db()