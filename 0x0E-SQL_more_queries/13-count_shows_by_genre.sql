-- Lists all genres from hbtn_0d_tvshows alngside number of shows
SELECT tv_genres.name as genre, COUNT(tv_shows.id) as number_of_shows
    FROM tv_shows
        INNER JOIN tv_show_genres
            ON tv_shows.id = tv_show_genres.show_id
        INNER JOIN tv_genres
            ON tv_genres.id = tv_show_genres.genre_id
    GROUP BY tv_genres.name
    ORDER BY number_of_shows DESC;