import os
import psycopg2

conn = psycopg2.connect(
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS'),
    database="face_recognizer_db")

cur = conn.cursor()

cur.execute("""CREATE TABLE users (
            id serial PRIMARY KEY,
            username varchar (255),
            image_path text,
            created_at date DEFAULT CURRENT_TIMESTAMP);"""
            )
conn.commit()
cur.close()
conn.close()
