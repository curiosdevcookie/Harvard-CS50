SELECT movies.title FROM movies
WHERE movies.id IN (
  SELECT stars.movie_id FROM stars
  WHERE stars.person_id IN (
    SELECT people.id FROM people WHERE people.name = 'Johnny Depp'
  )
) AND movies.id IN (
  SELECT stars.movie_id FROM stars
  WHERE stars.person_id IN (
    SELECT people.id FROM people WHERE people.name = 'Helena Bonham Carter'
  )
);


-- SELECT movies.title FROM movies

-- INNER JOIN stars AS stars1 ON movies.id = stars1.movie_id
-- INNER JOIN people AS people1 ON stars1.person_id = people1.id AND people1.name = 'Johnny Depp'

-- INNER JOIN stars AS stars2 ON movies.id = stars2.movie_id
-- INNER JOIN people AS people2 ON stars2.person_id = people2.id AND people2.name = 'Helena Bonham Carter';