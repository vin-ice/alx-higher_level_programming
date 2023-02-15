-- Lists all genres of the show Dexter
SELECT tv_genres
    FROM tv_shows
        INNER JOIN tv_show_genres
            ON tv_shows.id = tv_show_genres.show_id
        INNER JOIN tv_shows
            ON tv_shows.id = 