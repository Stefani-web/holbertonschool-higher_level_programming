-- Selects genre name and sum of ratings
SELECT tv_genres.name, SUM(tv_genres.rating) AS rating_sum
FROM tv_genres
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
