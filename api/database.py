'''
Dev Jeison Maigual
Script description: weather station DataBase
Engine:SQLite3
Date 09/09/2024
'''

#Import engine database pakage

import sqlite3

#Create weather station database connection

con = sqlite3.connect('weather_station.db')

#create cursor
cur = con.cursor()

#Create model User

users_model='''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT not null,
        password text not null,
        role text not null,
        status boolean default null,
        create_at timestamp default(datetime('now','localtime')),
        update_at timestamp default(datetime('now','localtime')),
        delete_at null
    )
'''

#execute query
cur.execute(users_model)

#close connection
con.close()