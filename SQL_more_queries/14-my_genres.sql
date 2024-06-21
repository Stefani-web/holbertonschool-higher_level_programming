-- Selecting genre names for the show 'Dexter'
-- Joining with the tv_show_genres table to get the genre matches
-- Joining with the tv_shows table to target the show 'Dexter'
-- Condition to select only the show 'Dexter'
-- Sorting the results by genre name in ascending order

SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
