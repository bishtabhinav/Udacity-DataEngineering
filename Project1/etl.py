import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
from create_tables import *

#Song file has 1 record each file so the values[0] is taken and expected to workfor inserting
def process_song_file(cur, filepath):
    """
        This procedure processes a song file whose filepath has been provided as an arugment.
        It extracts the song information in order to store it into the songs table.
        Then it extracts the artist information in order to store it into the artists table.

        :parameter:
        * cur the cursor variable
        * filepath the file path to the song file
    """
    # open song file
    df = pd.read_json(filepath, lines=True)
    # insert song record
    song_data = df[['song_id','title','artist_id','year','duration']].values[0].tolist()
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data =  df[['artist_id','artist_name','artist_location','artist_latitude','artist_longitude']].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
           This procedure processes a log file whose filepath has been provided as an arugment.
           It extracts the time information for creating and master table, creates a user table
           that maintiants the list of all users accessing the application and then creates a
           transaction table that has the reocrds for all users and there songs accessed, the
           songs have been looked up on the basis of song, artisid and duration of song

           :parameter:
           * cur the cursor variable
           * filepath the file path to the song file
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page'] == 'NextSong']

    # convert timestamp column to datetime
    t =  pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
    time_data = [t,t.dt.hour,t.dt.day,t.dt.week,t.dt.month,t.dt.year,t.dt.weekday]

    # Create Column lables
    column_labels =  ['timestamp','hour','day','week','month','year','weekday']
    time_df = pd.DataFrame.from_dict(pd.Series(time_data,index=column_labels).to_dict())

    # iterate through rows and insert into the tables
    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_list = ([df.loc[:]['userId'],df.loc[:]['firstName'],df.loc[:]['lastName'],df.loc[:]['gender'],df.loc[:]['level']])
    column_labels = ['userid','firstname','lastname','gender','level']
    user_df = pd.DataFrame.from_dict(pd.Series(user_list,index=column_labels).to_dict())

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data=(pd.to_datetime(row['ts'],unit='ms'),row['userId'],row['level'],songid,artistid,row['sessionId'],row['location'],row['userAgent'])

        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
               This procedure processes a log file whose filepath has been provided as an arugment.
               It extracts the time information for creating and master table, creates a user table
               that maintiants the list of all users accessing the application and then creates a
               transaction table that has the reocrds for all users and there songs accessed, the
               songs have been looked up on the basis of song, artisid and duration of song

               :parameter:
               * cur: the cursor variable
               * conn: connecation variable use to connect database
               * filepath: the file path to the song file
               * func: function to be called for triggering the flow.
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """
               This function is main contro flow from python

    """
    #conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    #cur = conn.cursor()
    cur,conn = create_database()
    create_tables(cur, conn)
    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()