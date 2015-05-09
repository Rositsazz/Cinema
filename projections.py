import sqlite3
from movies import Movies


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

    GET_CURRENT_MOVIE = """
        SELECT name
        FROM Movies
        WHERE id = ?
    """

    GET_AVAILABLE_SEATS_BY_ID = """
        SELECT available_seats
        FROM Projections
        WHERE id = ?
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

        return result.fetchall()


    @classmethod
    def show_projections(cls, conn, movie_id=None, date=None):
        cursor = conn.cursor()


        projections = cls.get_projections(conn, movie_id, date)

        if not(movie_id is None) and date is None:
            current_movie = cursor.execute(cls.GET_CURRENT_MOVIE, (movie_id, ))
            name_curr_movie = current_movie.fetchone()[0]
            print('Projections for movie ' + name_curr_movie + ':')

            for projection in projections:
                pr_id = projection[0]
                type_movie = projection[2]
                date = projection[3]
                time = projection[4]
                print('[{}] - {} {} ({})'.format(pr_id, date, time, type_movie))

        elif not(movie_id is None) and not(date is None):
            current_movie = cursor.execute(cls.GET_CURRENT_MOVIE, (movie_id, ))
            name_curr_movie = current_movie.fetchone()[0]
            print("Projections for movie {} on date {}:".format(name_curr_movie, date))

            for projection in projections:
                pr_id = projection[0]
                type_movie = projection[2]
                time = projection[4]
                print('[{}] - {} ({})'.format(pr_id, time, type_movie))
        else:
            print('All projections:')

            for projection in projections:
                pr_id = projection[0]
                id_movie = projection[1]
                type_movie = projection[2]
                date = projection[3]
                time = projection[4]
                current_movie = cursor.execute(cls.GET_CURRENT_MOVIE, (id_movie, ))
                name_curr_movie = current_movie.fetchone()[0]

                print('[{}] - {} on {} at {} ({})'.format(pr_id, name_curr_movie, date, time, type_movie))

        # return name_curr_movie


    @classmethod
    def get_available_seats_by_id(cls, conn, projection_id):
        cursor = conn.cursor()
        result = cursor.execute(cls.GET_AVAILABLE_SEATS_BY_ID, (projection_id, ))
        return result.fetchone()[0]

    @classmethod
    def delete_projections(cla, conn):
        pass
