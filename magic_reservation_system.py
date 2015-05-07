import sqlite3
import sys

if len(sys.argv) <= 1:
    print("Provide database file")
    print("python3.4 magic_reservation_system.py movie.db")
    sys.exit(1)

db = sys.argv[1]

conn = sqlite3.connect(db)
conn.row_factory = sqlite3.Row

