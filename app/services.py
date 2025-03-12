import sqlite3

DB_FILE = "medical_devices.db"


def get_grouped_by_classification():
    """Groups medical devices by classification code."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT classification_code, GROUP_CONCAT(device_name, ', ') AS devices
        FROM classifications
        GROUP BY classification_code
    """)

    grouped_data = cursor.fetchall()
    conn.close()

    return grouped_data


def find_similar_devices(product_code):
    """Finds similar devices based on classification criteria."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Get the device's classification info
    cursor.execute("""
        SELECT classification_code, medical_specialty
        FROM classifications
        WHERE product_code = ?
    """, (product_code,))

    device = cursor.fetchone()

    if not device:
        conn.close()
        return {"error": "Device not found"}

    classification_code, medical_specialty = device

    # Find other devices with the same classification code (Strong match)
    cursor.execute("""
        SELECT product_code, device_name
        FROM classifications
        WHERE classification_code = ? AND product_code != ?
    """, (classification_code, product_code))

    strong_matches = cursor.fetchall()

    # Find other devices in the same medical specialty (Potential alternative)
    cursor.execute("""
        SELECT product_code, device_name
        FROM classifications
        WHERE medical_specialty = ? AND classification_code != ?
    """, (medical_specialty, classification_code))

    potential_matches = cursor.fetchall()

    conn.close()

    return {
        "strong_matches": strong_matches,
        "potential_alternatives": potential_matches
    }
