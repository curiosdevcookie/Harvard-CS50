SELECT people.name FROM people WHERE people.id IN (SELECT stars.person_id FROM stars WHERE stars.movie_id IN (SELECT movies.id FROM movies WHERE movies.title IN (SELECT movies.title FROM movies WHERE movies.id IN (SELECT stars.movie_id FROM stars WHERE stars.person_id IN (SELECT people.id FROM people WHERE people.name = 'Kevin Bacon' AND people.birth = '1958'))))) 
AND people.id != (
  SELECT id 
  FROM people 
  WHERE name = 'Kevin Bacon'
);
