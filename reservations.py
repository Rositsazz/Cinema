from movies import Movies
from projections import Projections
# from available_seats import AvailableSeats


class Reservations:

    INSERT_USERNAME = """
        INSERT INTO Reservations(username)
        VALUES(?)
    """
    SEARCH_FOR_USERNAME = """
        SELECT username
        FROM Reservations
    """
    CHOOSE_MOVIE_NAME = """
        SELECT name
        FROM Movies
        WHERE id = ?
        """

    AVAILABLE_SEATS = """
        SELECT available_seats
        FROM Projections
    """

    UPDATE_ROW_AND_COLUMN = """
        UPDATE Reservations
        SET row = ?, col = ?
        WHERE id = ?
    """

    SELECT_ROW_AND_COLUMN = """
        SELECT id
        FROM Reservations
        WHERE username = ? AND row=-1 AND col=-1
    """

    SELECT_ROW_AND_COLUMN_BY_ID = """
        SELECT row, col
        FROM Reservations
        WHERE id = ?
    """

    @classmethod
    def make_reservation(cls, conn, username):

        cursor = conn.cursor()

        cursor.execute(cls.INSERT_USERNAME, (username,))
        Movies.show_current_movies(conn)
        conn.commit()

    @classmethod
    def search_for_user(cls, conn, username):
        cursor = conn.cursor()

        cursor.execute(cls.SEARCH_FOR_USERNAME)
        conn.commit()

    @classmethod
    def choose_movie(cls, conn, movie_id):
        res = Projections.show_projections(conn, movie_id=movie_id)
        return res

    @classmethod
    def change_row_and_column(cls, conn, name, row, column):
        cursor = conn.cursor()
        null_values = cursor.execute(cls.SELECT_ROW_AND_COLUMN, (name, ))
        res_id = null_values.fetchone()[0]
        print(res_id)
        cursor.execute(cls.UPDATE_ROW_AND_COLUMN, (row, column, res_id))
        res = cursor.execute(cls.SELECT_ROW_AND_COLUMN_BY_ID, (res_id, ))
        print(res.fetchone())
        conn.commit()
