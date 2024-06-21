-- Selecting comedy show titles
-- Joining with tv_show_genres table to get genre matches
-- Joining with tv_genres table to target the 'Comedy' genre
-- Sorting results by show title in ascending order

SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
