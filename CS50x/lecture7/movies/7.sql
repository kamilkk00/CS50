SELECT rating, title FROM ratings JOIN movies on ratings.movie_id = movies.id WHERE movies.year = 2010 ORDER BY rating DESC, title ASC;
