CREATE KEYSPACE IF NOT EXISTS health WITH replication = {'class':'SimpleStrategy', 'replication_factor':1};
USE health;

CREATE TABLE IF NOT EXISTS patient_analytics (
  patient_id text,
  timestamp timestamp,
  risk_score float,
  PRIMARY KEY (patient_id, timestamp)
);

INSERT INTO patient_analytics (patient_id, timestamp, risk_score) VALUES ('P001', toTimestamp(now()), 0.3);
INSERT INTO patient_analytics (patient_id, timestamp, risk_score) VALUES ('P002', toTimestamp(now()), 0.5);
INSERT INTO patient_analytics (patient_id, timestamp, risk_score) VALUES ('P003', toTimestamp(now()), 0.7);
INSERT INTO patient_analytics (patient_id, timestamp, risk_score) VALUES ('P004', toTimestamp(now()), 0.2);
INSERT INTO patient_analytics (patient_id, timestamp, risk_score) VALUES ('P005', toTimestamp(now()), 0.9);
