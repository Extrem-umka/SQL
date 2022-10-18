create table if not exists musical_genre(
id serial primary key,
name_genre VARCHAR(50) not null
);

create table if not exists musician_performer(
id serial primary key,
name_artist VARCHAR(70) not null
);


create table if not exists music_genre_performer(
musical_genre_id integer references musical_genre(id),
musician_performer_id integer references musician_performer(id),
constraint pk primary key(musical_genre_id, musician_performer_id)
);

create table if not exists album(
id serial primary key,
name_album VARCHAR(70) not null,
year_of_issue integer not null
);

create table if not exists music_performer_album(
album_id integer references album(id),
musician_performer_id integer references musician_performer(id),
primary key(album_id, musician_performer_id)
);

create table if not exists track(
id serial primary key,
name_track VARCHAR(70) not null,
track_duration integer not null,
album_id integer references album(id)
);

create table if not exists compilation(
id serial primary key,
name_compilation VARCHAR(70) not null,
year_of_issue integer not null
);


create table if not exists track_compilation(
track_id integer references track(id),
compilation_id integer references compilation(id),
primary key(track_id, compilation_id)
);




