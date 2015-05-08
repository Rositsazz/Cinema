from movies import Movies
from projections import Projections


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

    @classmethod
    def make_reservation(cls, conn, username):

        cursor = conn.cursor()

        cursor.execute(cls.INSERT_USERNAME, (username,))
        Movies.show_current_movies(conn)
        conn.commit()

    @classmethod
    def search_for_user(cls, conn, username):
        cursor = conn.cursor()

        result = cursor.execute(cls.SEARCH_FOR_USERNAME)
        print(result.fetchall())
        conn.commit()

    @classmethod
    def choose_movie(cls, conn, movie_id):
        cursor = conn.cursor()
        movie_name = cursor.execute(cls.CHOOSE_MOVIE_NAME, (movie_id,))
        print("Projections for movie {}:".format(movie_name.fetchone()[0]))
        res = Projections.get_projections(conn, movie_id=movie_id)
# [5] - 2014-04-02 19:30 (2D) - 98 spots available
# [6] - 2014-04-02 22:00 (3D) - 100 spots availabe")
