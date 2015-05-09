INSERT INTO Movies(name, rating)
VALUES ('The Hunger Games: Catching Fire', 7.9);

INSERT INTO Movies(name, rating)
VALUES ('Wreck-It Ralph', 7.8);

INSERT INTO Movies(name, rating)
VALUES ('Her', 8.3);

INSERT INTO Projections(movie_id, type, date, time)
VALUES (1, '3D', '2014-04-01', '19:10');

INSERT INTO Projections(movie_id, type, date, time)
VALUES (1, '2D', '2014-04-01', '19:00');

INSERT INTO Projections(movie_id, type, date, time)
VALUES (1, '4DX', '2014-04-02', '21:00');

INSERT INTO Projections(movie_id, type, date, time)
VALUES (3, '2D', '2014-04-05', '20:20');

INSERT INTO Projections(movie_id, type, date, time)
VALUES (2, '3D', '2014-04-02', '22:00');

INSERT INTO Projections(movie_id, type, date, time)
VALUES (2, '2D', '2014-04-02', '19:30');

INSERT INTO Reservations(username, projection_id, row, col)
VALUES ('RadoRado', 1, 2, 1);

INSERT INTO Reservations(username, projection_id, row, col)
VALUES ('RadoRado', 1, 3, 5);

INSERT INTO Reservations(username, projection_id, row, col)
VALUES ('RadoRado', 1, 7, 8);

INSERT INTO Reservations(username, projection_id, row, col)
VALUES ('Ivo', 3, 1, 1);

INSERT INTO Reservations(username, projection_id, row, col)
VALUES ('Ivo', 3, 1, 2);

INSERT INTO Reservations(username, projection_id, row, col)
VALUES ('Mysterious', 5, 2, 3);

INSERT INTO Reservations(username, projection_id, row, col)
VALUES ('Mysterious', 5, 2, 4);
