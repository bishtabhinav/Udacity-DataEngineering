# DROP TABLES

songplay_table_drop = "DROP TABLE songplays"
user_table_drop = "DROP TABLE users "
song_table_drop = "DROP TABLE songs"
artist_table_drop = "DROP TABLE artists"
time_table_drop = "DROP TABLE time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id serial, start_time TIMESTAMP, user_id TEXT , level TEXT, song_id TEXT, artist_id TEXT, session_id TEXT, location TEXT, user_agent TEXT)""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id TEXT, first_name TEXT, last_name TEXT, gender TEXT, level TEXT)""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id TEXT, title TEXT, artist_id TEXT, year TEXT, duration TEXT)""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id TEXT, name TEXT, location TEXT, latitude FLOAT, longitude FLOAT)""")


time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time timestamp, hour INT, day INT, week TEXT, month TEXT, year INT, weekday INT)""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays ( start_time, user_id, level, song_id,artist_id,session_id,location,user_agent) VALUES ( %s, %s, %s, %s,%s,%s,%s,%s)""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s);""")

song_table_insert =  ("""INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s);""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location , latitude, longitude)  VALUES (%s, %s, %s, %s, %s);""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day , week, month,year,weekday)  VALUES (%s, %s, %s, %s, %s,%s,%s);""")

# FIND SONGS

song_select = (""" select s.song_id,a.artist_id from songs s inner join artists a on a.artist_id= s.artist_id WHERE lower(s.title)=lower(%s) AND lower(trim(a.name))= lower(trim(%s)) and cast(s.duration as float)=%s 
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
#create_table_queries = [song_table_create,artist_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]