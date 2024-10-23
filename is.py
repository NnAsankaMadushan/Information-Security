import sqlite3
import hashlib

# Connect to the database (creates the file if it doesn't exist)
conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

# Create table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

# Sample user data with hashed passwords
username1, password1 = "asanka", hashlib.sha256("asapassword".encode()).hexdigest()
username2, password2 = "masha", hashlib.sha256("mashapassword".encode()).hexdigest()
username3, password3 = "abheetha", hashlib.sha256("abheethapassword".encode()).hexdigest()
username4, password4 = "nimna", hashlib.sha256("nimnapassword".encode()).hexdigest()

# Insert data into the table
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

print("Data inserted successfully!")
