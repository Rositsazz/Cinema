import sqlite3


class Projections:

    INSERT_PROJECTION_SQL = """
        INSERT INTO Projections(movie_id, type, date, time)
        VALUES (?,?,?,?)
    """

    GET_PROJECTIONS_MOVIE_ID = """
        SELECT id, movie_id, type, date, time
        FROM Projections
        WHERE movie_id = ?
    """

    GET_PROJECTIONS_MOVIE_ID_AND_DATE = """
        SELECT id, movie_id, type, date, time
        FROM Projections
        WHERE movie_id = ?
            AND date = ?
    """

    GET_ALL_PROJECTIONS = """
        SELECT id, movie_id, type, date, time
        FROM Projections
    """

    @classmethod
    def add_projections(cls, conn, movie_id, type_movie, date, time):

        try:

            cursor = conn.cursor()

            cursor.execute(cls.INSERT_PROJECTION_SQL, (movie_id, type_movie,
                                                       date, time))

            conn.commit()

        except:
            pass

    @classmethod
    def get_projections(cls, conn, movie_id=None, date=None):
        cursor = conn.cursor()

        if not(movie_id is None) and date is None:
            result = cursor.execute(cls.GET_PROJECTIONS_MOVIE_ID, (movie_id, ))
        elif not(movie_id is None) and not(date is None):
            result = cursor.execute(cls.GET_PROJECTIONS_MOVIE_ID_AND_DATE, (movie_id, date))
        else:
            result = cursor.execute(cls.GET_ALL_PROJECTIONS)

        return result.fetchmany()


    @classmethod
    def show_projections(cls, conn):
        pass

    @classmethod
    def delete_projections(cla, conn):
        pass
