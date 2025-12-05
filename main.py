import random
from faker import Faker 
import mysql.connector 

fake =Faker("en_IN")


db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Venkii_11M",
        database="SmartGarbage"
    )

cur = db.cursor()

for i in range(15):
    tid = i + 1
    userId = random.randint(1, 10)
    collectorId = random.randint(1, 5)

    description = random.choice([
        "Pickup required",
        "Garbage overflowing",
        "Collection request",
        "Wet waste ready",
        "Dry waste pickup"
    ])

    status = random.choice(["pending", "assigned", "collected"])
    priority = random.choice(["low", "medium", "high"])

    # Bengaluru-like GPS coordinates
    lat = round(random.uniform(12.90, 13.05), 6)
    lng = round(random.uniform(77.50, 77.70), 6)

    location_json = f'{{"lat": {lat}, "lng": {lng}}}'

    sql = """
    INSERT INTO report (id, userId, collectorId, description, photoUrl, status, priority, location, createdAt)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, NOW())
    """

    val = (tid, userId, collectorId, description, "/uploads/default.jpg", status, priority, location_json)
    cur.execute(sql, val)

db.commit()
print("Inserted 15 Indian tasks!")

