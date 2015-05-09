import sqlite3
import sys

from movies import Movies
from projections import Projections
from reservations import Reservations
from available_seats import AvailableSeats


if len(sys.argv) <= 1:
    print("Provide database file")
    print("python3.4 magic_reservation_system.py movie.db")
    sys.exit(1)

db = sys.argv[1]

conn = sqlite3.connect(db)
# conn.row_factory = sqlite3.Row

commands = ["show_movies",
            "show_movie_projections <movie_id>",
            "show_movie_projections <movie_id> <date>",
            "make_reservation",
            "available seat for <movie_id> <date> <time>"]

INSERT_INTO_RESERRVATION = """
    INSERT INTO Reservations(username, projection_id, row, col)
    VALUES (?, ?, ?, ?)
"""
ROW = -1
COL = -1

print("""Dear, customer
        Please, choose between these commands:
        1) show_movies,
        2) show_movie_projections <movie_id>,
        3) show_movie_projections <movie_id> <date>,
        4) make_reservation,
        5) available seat for <movie_id> <date> <time>
        6) exit

        FOR US!!!! """)

while True:
    command = input("> ")

    commands = command.split(' ')

    if commands[0] == "1":
        Movies.show_current_movies(conn)

    elif commands[0] == "2":
        if len(commands) < 2:
            Projections.show_projections(conn)
        else:
            Projections.show_projections(conn, commands[1])
    elif commands[0] == "3":
        try:
            Projections.show_projections(conn, commands[1], commands[2])
        except:
            print("Wait for correct command :P")

    elif commands[0] == "4":
        username = input("Step 1 (User): Choose name> ")
        Reservations.search_for_user(conn, username)

        tickets = input("Step 1 (User): Choose number of tickets> ")
        Reservations.make_reservation(conn, username)

        movie_id = input("Step 2 (Movie): Choose a movie> ")
        Reservations.choose_movie(conn, movie_id)

        projection_id = input("Choose projection number> ")
        # seats = Projections.get_available_seats_by_id(conn, projection_id)
        # print("For this projection the available seats are {}".format(seats))

        AvailableSeats.show_available_seats(conn, movie_id, projection_id)

        for i in range(int(tickets)):
            cursor = conn.cursor()
            cursor.execute(INSERT_INTO_RESERRVATION, (username, projection_id, ROW, COL ))

        for i in range(int(tickets)):
            print("\nTicket {} :".format(i+1))
            ticket = input("row and column: ")
            row, column = ticket.split(" ")
            Reservations.change_row_and_column(conn, username, row, column)

        AvailableSeats.show_available_seats(conn, movie_id, projection_id)

        print("{}, You ordered your tickets for the movie".format(username))
        break


    elif commands[0] == "exit":
        break
