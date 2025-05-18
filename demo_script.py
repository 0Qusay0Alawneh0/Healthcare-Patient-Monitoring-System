# Demo Script: Demonstrate All DB Accesses (pseudo-code style)

# MongoDB (patient data)
# Example: Insert and find patient data
# db.patients.insertOne({"patient_id": "P001", "name": "John Doe", "age": 45, "gender": "Male", "medical_history": ["diabetes"]})
# db.patients.find({})

# InfluxDB (time-series data)
# Example: Write patient vitals
# curl -i -XPOST http://localhost:8086/write?db=health --data-binary "vitals,patient_id=P001 heartbeat=80,blood_pressure=120"

# Cassandra (analytics)
# Example: Insert patient risk analytics
# INSERT INTO patient_analytics (patient_id, timestamp, risk_score) VALUES ('P001', toTimestamp(now()), 0.7);

# Neo4j (relationships)
# Example: Query doctor-patient relationships
# MATCH (p:Patient)-[:TREATED_BY]->(d:Doctor) RETURN p, d;

# Redis (alerts)
# Example: Set and get patient alerts
# SET patient:alerts:P001 "Abnormal heartbeat at 10:01AM"
# GET patient:alerts:P001
