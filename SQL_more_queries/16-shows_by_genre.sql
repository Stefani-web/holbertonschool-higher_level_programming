-- Selecting show titles and associated genre names
-- Left join to include all shows, even those without genres
-- Left join with the tv_genres table to get the genre names
-- Sorting the results by show title and genre name in ascending order

SELECT tv_shows.title, COALESCE(tv_genres.name, 'NULL') AS genre_name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, genre_name;
