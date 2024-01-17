-- list_genres_not_linked_to_dexter.sql

USE hbtn_0d_tvshows;
SET @dexter_genre_ids = (SELECT GROUP_CONCAT(DISTINCT genre_id) FROM tv_show_genres WHERE show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter'));

-- List all genres not linked to Dexter
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id AND FIND_IN_SET(tv_genres.id, @dexter_genre_ids)
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_genres.name ASC;
