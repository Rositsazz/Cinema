import sqlite3
import sys

from movies import Movies
from reservations import Reservations

if len(sys.argv) <= 1:
    print("Provide database file")
    print("python3.4 magic_reservation_system.py movie.db")
    sys.exit(1)

db = sys.argv[1]

conn = sqlite3.connect(db)
# conn.row_factory = sqlite3.Row

commands = ["show movies",
            "show_movie_projections <movie_id>",
            "show_movie_projections <movie_id> <date>",
            "make_reservation",
            "available seat for <movie_id> <date> <time>"]

print("""Dear, customer
        Please, choose between these commands:
        1) show movies,
        2) show_movie_projections <movie_id>,
        3) show_movie_projections <movie_id> <date>,
        4) make_reservation,
        5) available seat for <movie_id> <date> <time>

        FOR US!!!! """)

command = input(">")
if command == "1":
    Movies.show_current_movies(conn)
elif command == "4":
    username = input("Step 1 (User): Choose name>")
    Reservations.search_for_user(conn, username)
    tickets = input("Step 1 (User): Choose number of tickets>")
    Reservations.make_reservation(conn, username)
    movie_id = input("Step 2 (Movie): Choose a movie>")
    Reservations.choose_movie(conn, movie_id)
