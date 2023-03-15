-- Lists all genres not linked to Dexter on hbtn_0d_tvshows
SELECT tv_genres.name as name
    FROM tv_genres
WHERE tv_genres.id NOT IN
    (
        SELECT genre_id
            FROM tv_show_genres
                INNER JOIN tv_shows
                    ON tv_show_genres.show_id = tv_shows.id
        WHERE tv_shows.title = 'Dexter'
    )
ORDER BY name ASC;
