import sqlite3
import sys

from movies import Movies


if len(sys.argv) <= 1:
    print("Provide database file")
    print("python3.4 magic_reservation_system.py movie.db")
    sys.exit(1)

db = sys.argv[1]

conn = sqlite3.connect(db)
conn.row_factory = sqlite3.Row

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



# print(commands)
# Movies.show_current_movies(conn)

