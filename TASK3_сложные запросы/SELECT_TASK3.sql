select musical_genre_id, count(musician_performer_id)
from music_genre_performer mgp  
group by musical_genre_id
order by count(musician_performer_id) desc;

select year_of_issue, count(name_track) 
from track t
join album a on t.album_id = album_id
group by year_of_issue
having year_of_issue between  2019 and 2020;

select name_album, AVG(track_duration) 
from album a
join track t on t.album_id = album_id
group by name_album
order by AVG(track_duration);

select name_artist, year_of_issue 
from musician_performer mp 
join music_performer_album mpa on mp.id = mpa.musician_performer_id 
join album a on mpa.album_id = a.id 
group by name_artist, year_of_issue
having not year_of_issue = 2020;

select name_compilation, name_artist
from compilation c 
join track_compilation tc on c.id = tc.track_id 
join track t on tc.track_id = t.id 
join album a on t.album_id = a.id 
join music_performer_album mpa on a.id = mpa.musician_performer_id 
join musician_performer mp on mpa.musician_performer_id = mp.id
group by name_compilation, name_artist
having name_artist = 'Lara Fabian';

select name_album, name_artist, count(name_genre)
from album a 
join music_performer_album mpa on a.id = mpa.musician_performer_id 
join musician_performer mp on mpa.musician_performer_id = mp.id 
join music_genre_performer mgp on mp.id =mgp.musical_genre_id 
join musical_genre mg on mgp.musical_genre_id = mg.id 
group by name_album, name_artist
having count(name_genre) > 1;

select name_track 
from track t 
left join track_compilation tc ON t.id = tc.compilation_id 
where compilation_id is null;

select name_artist
from musician_performer mp 
join music_performer_album mpa on mp.id = mpa.album_id 
join album a on mpa.album_id = a.id
join track t on a.id = t.id 
where track_duration = 
(select min(track_duration) 
from musician_performer mp 
join music_performer_album mpa on mp.id = mpa.album_id 
join album a on mpa.album_id = a.id
join track t on a.id = t.id );

select name_album,count(t.album_id)
from album a 
join track t on a.id = t.album_id
group by name_album;






