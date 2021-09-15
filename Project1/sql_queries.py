# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users "
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE songplays (songplay_id serial primary key, start_time TIMESTAMP NOT NULL, user_id INT NOT NULL , 
                                level TEXT, song_id TEXT, artist_id TEXT, session_id TEXT, location TEXT, user_agent TEXT)
                        """)
user_table_create = ("""CREATE TABLE users 
                        (
                            user_id INT primary key, first_name TEXT, last_name TEXT, gender TEXT, level TEXT
                        )
                    """)
song_table_create = ("""CREATE TABLE songs 
                        (
                            song_id TEXT primary key, title TEXT, artist_id TEXT, year TEXT, duration TEXT
                        )
                    """)
artist_table_create = ("""CREATE TABLE artists
                          (
                            artist_id TEXT primary key, name TEXT, location TEXT, latitude FLOAT, longitude FLOAT
                           )
                       """)
time_table_create = ("""CREATE TABLE  time 
                        (
                            start_time timestamp primary key, hour INT, day INT, week TEXT, month TEXT, year INT, weekday INT
                        )
                    """)

# INSERT RECORDS
songplay_table_insert = ("""INSERT INTO songplays
                            (
                                start_time, user_id, level, song_id,artist_id,session_id,location,user_agent
                            ) 
                                VALUES ( %s, %s, %s, %s,%s,%s,%s,%s)""")
user_table_insert = ("""INSERT INTO users
                        (
                            user_id, first_name, last_name, gender, level) 
                            VALUES (%s, %s, %s, %s, %s)
                            ON CONFLICT(user_id) DO UPDATE SET level = excluded.level;""")
song_table_insert =  ("""INSERT INTO songs
                         (
                            song_id, title, artist_id, year, duration
                          ) 
                            VALUES (%s, %s, %s, %s, %s)
                            ON CONFLICT (song_id) DO NOTHING;""")
artist_table_insert = ("""INSERT INTO artists
                          (
                            artist_id, name, location , latitude, longitude
                          )  
                            VALUES (%s, %s, %s, %s, %s)
                            ON CONFLICT (artist_id) DO NOTHING;""")
time_table_insert = ("""INSERT INTO time
                        (
                            start_time, hour, day , week, month,year,weekday
                        )  
                        VALUES 
                        (%s, %s, %s, %s, %s,%s,%s)
                        ON CONFLICT (start_time) DO NOTHING;""")

# FIND SONGS

song_select = (""" select s.song_id,a.artist_id from songs s inner join artists a on a.artist_id= s.artist_id 
                    WHERE lower(s.title)=lower(%s) AND lower(trim(a.name))= lower(trim(%s)) and cast(s.duration as float)=%s 
             """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
#create_table_queries = [song_table_create,artist_table_create]
