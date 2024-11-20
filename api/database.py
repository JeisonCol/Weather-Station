'''
Dev Jeison Maigual
Script description: weather station DataBase
Engine:SQLite3
Date 09/09/2024
'''

# Import engine database package
import sqlite3

# Create weather station database connection
con = sqlite3.connect('weather_station.db')

# Create cursor
cur = con.cursor()

# Create model User
users_model = '''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL, 
        status BOOLEAN DEFAULT NULL,
        create_at TIMESTAMP DEFAULT(datetime('now', 'localtime')),
        update_at TIMESTAMP DEFAULT(datetime('now', 'localtime')),
        delete_at NULL
    )
'''

# Create model Sensores
sensores_model = '''
    CREATE TABLE IF NOT EXISTS sensores(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        temperature FLOAT NOT NULL,
        humidity FLOAT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
'''

# Execute queries
cur.execute(users_model)
cur.execute(sensores_model)

# Commit and close connection
con.commit()
con.close()

print("Database and tables created successfully.")
