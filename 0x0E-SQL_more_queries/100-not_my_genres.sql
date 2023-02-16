-- Lists all genres not linked to Dexter on hbtn_0d_tvshows
SELECT tv_genres.name as genre
    FROM tv_genres
WHERE tv_genres.id NOT IN
    (
        SELECT genre_id
            FROM tv_show_genres
        WHERE show_id = 
            (
                SELECT id
                    FROM tv_shows
                WHERE title = 'Dexter'
            )
    )
ORDER BY genre ASC;
