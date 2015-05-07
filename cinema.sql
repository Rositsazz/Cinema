DROP TABLE IF EXISTS Movies;
CREATE TABLE Movies(
		id INTEGER PRIMARY KEY,
		name VARCHAR(150),
		rating DECIMAL(2,1)
);


DROP TABLE IF EXISTS Reservations;
CREATE TABLE Reservations(
	id integer primary key,
	username VARCHAR(60),
	projection_id	INTEGER,
	row	INTEGER,
	col INTEGER,
	FOREIGN KEY (projection_id) REFERENCES Projections(id)
)


DROP TABLE IF EXISTS Projections;
CREATE TABLE Projections(
	id INTEGER PRIMARY KEY,
	movie_id INTEGER,
	type VARCHAR(10),
	date DATE,
	time DATETIME,
	FOREIGN KEY(movie_id) REFERENCES Movies(id)
);

INSERT INTO Movies(name, rating)
VALUES("F&F", 10);

INSERT INTO Projections(movie_id, type, date, time)
VALUES(1, "3D", "2014-04-01", "20:00");

INSERT INTO Reservations(username, projection_id, row, col)
VALUES("Aldi", 1 ,10, 9);