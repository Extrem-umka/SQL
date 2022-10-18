insert into musical_genre(name_genre)
VALUES('popsa'),
	  ('rap'),
	  ('classic'),
	  ('jazz'),
	  ('guitar');
	 

	 
insert into musician_performer(name_artist)
VALUES('Lara Fabian'),
	  ('Adel'),
	  ('Joe Satriani'),
	  ('Steve Vai'),
	  ('S. Rahmaninov'),
	  ('2pac'),
	  ('Al Di Meola'),
	  ('Dr.Dre');
	

	 
insert into album (name_album, year_of_issue)
VALUES('Camouflage', 2017),
	  ('30', 2020),
	  ('Super Colossal', 2006),
	  ('Piano Reductions', 2018),
	  ('Symphony', 1940),
	  ('Still i Rise', 1999),
	  ('Elegant', 2018),
	  ('The Chronic', 1992),
	  ('My Story', 2015);
	 	 

insert into track (name_track, track_duration, album_id)
VALUES('fantasy_1', 195, 1),
	  ('fantasy_2', 255, 1),
	  ('fantasy_3', 270, 2),
	  ('fantasy_4', 240, 2),
	  ('fantasy_5', 220, 3),
	  ('fantasy_6', 181, 3),
	  ('fantasy_7', 220, 4),
	  ('fantasy_8', 224, 4),
	  ('fantasy_9', 236, 5),
	  ('fantasy_10', 305, 6),
	  ('fantasy_11', 362, 7),
	  ('fantasy_12', 355, 7),
	  ('fantasy_13', 185, 8),
	  ('fantasy_14', 235, 8),
	  ('Myname_15',  250, 9);
	 

	 
	 
insert into compilation (name_compilation, year_of_issue)
VALUES('Best of the Best 1', 2022),
	  ('Best of the Best 2', 2021),
	  ('Best of the Best 3', 2020),
	  ('Best of the Best 4', 2019),
	  ('Best of the Best 5', 2018),
	  ('Best of the Best 6', 2017),
	  ('Best of the Best 7', 2016),
	  ('Best of the Best 8', 2015);
	 




insert into music_genre_performer (musical_genre_id, musician_performer_id)
VALUES(1,1),
	  (1,2),
	  (2,8),
	  (2,6),
	  (3,6),
	  (4,7),
	  (5,3),
	  (5,4);
	 
	
	 
insert into music_performer_album (album_id, musician_performer_id)
VALUES(1,1),
	  (2,2),
	  (3,3),
	  (4,4),
	  (5,5),
	  (6,6),
	  (7,7),
	  (8,8),
	  (9,8);
	 
	 

	 
insert into track_compilation  (track_id, compilation_id)
VALUES(1,1),
	  (1,2),
	  (1,3),
	  (2,3),
	  (2,4),
      (2,5),
      (3,4),
      (3,5),
      (4,6),
      (4,7),
      (4,8),
      (5,6),
      (5,7),
      (5,8),
      (6,6),
      (6,1),
      (6,8),
      (7,1),
      (7,3),
      (7,4),
      (8,1),
      (9,3),
      (10,4),
      (11,5),
      (11,2),
      (12,4),
      (13,7),
      (14,8),
      (15,6),
      (15,5);


	 