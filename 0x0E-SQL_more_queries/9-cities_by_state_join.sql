-- script that lists all cities contained in the database hbtn_0d_usa
SELECT id, name, name
  FROM cities INNER JOIN
       states
    ON states.id = cities.id
 ORDER BY cities.id ASC;
