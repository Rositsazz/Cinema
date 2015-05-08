from movies import Movies


class Reservations:

    INSERT_USERNAME = """
        INSERT INTO Reservations(username)
        VALUES(?)
    """
    SEARCH_FOR_USERNAME = """
        SELECT username
        FROM Reservations
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
        for row in result:
            if row[0] != username:
                cursor.execute(cls.INSERT_USERNAME, (username,))
        conn.commit()

    @classmethod
    def choose_movie(cls, conn, movie_id):
        pass
