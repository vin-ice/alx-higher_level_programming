-- Lists all shows and all genres linked to that show from db
SELECT tv_shows.title AS title, tv_genres.name AS name
    FROM tv_shows
        LEFT OUTER JOIN
            (
                tv_show_genres INNER JOIN tv_genres
                ON tv_show_genres.genre_id = tv_genres.id
            )
        ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, name;
