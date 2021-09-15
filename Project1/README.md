<h1>Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.<h1>
Ans:Saprkify is a online song streaming service. Users connect to the app and listen to songs based on there preferences. Sparkify woudl like to know/ analyse details around what songs are ruling the charts i.e what songs are heard more and what songs are heard less. Overall they need to know the anlytics around what are user preferences for the songs/ music on there application.


Q: State and justify your database schema design and ETL pipeline.
Ans: We have 3 Master/ dimension tables and 1 transaction table.
a) Master tables:- Tables that hold the master data for 
    1) Songs: Woudl hold the data for all the songs avaialble on the application with song and artist details
    2) Users: Would have details around Users names etc
    3) Artists: Would have details around the Artists who have sung the songs.
    4) Time: Its a date dimension table, that has the dates broken down for easy access

b) Transaction Table:
    1) SongPlay: This table woudl bring evrything together and would have details for songs, its artist users who browsed that song and time when it was heard .


Having master table allows us reduce data redundacy, the Songs users and artist that form the core of transactions on this application would not need to be repeated multiple times and only keys from individual tables would be reffered in the transaction table. 
a) If some details for registered usr changes then only the user table would need to change providing for decopling from rest of tables.
b) Similarly if some details of song ex: Song title, duration needs to change only the song table would be imapacted.




[Optional] Provide example queries and results for song play analysis.

Use Case:
a) Find the charbusters for each day
       
        Select s.title, CAST(sp.start_time)  as Day,count(1) as SongCount  
        FROM songplay sp LEFT JOIN songs s ON s.song_id = sp.song_id
        group by s.title, cast(sp.start_time as date)
        order by count(1) desc
        
b) Find the top artist heard each day

        Select CAST(sp.start_time)  as Day, a.name as artistName, ,count(1) as SongCount  
        FROM songplay sp LEFT JOIN artists a ON a.artist_id = sp.artist_id
        group by s.title, cast(sp.start_time as date) having count(1)>1
        order by count(1) desc
        
