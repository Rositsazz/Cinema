from reservations import Reservations


class AvailableSeats:

    GET_PROJECTION_ID = """
        SELECT id
        FROM Projections
        WHERE movie_id = ?
            AND date = ?
            AND time = ?
    """

    GET_SEATS_FOR_PROJECTIONS = """
        SELECT row, col
        FROM Reservations
        WHERE projection_id = ?
    """

    ALL_SEATS = [['.'] * 10] * 10

    @classmethod
    def get_projection_id(cls, conn, movie_id, date, time):
        cursor = conn.cursor()

        result = cursor.execute(cls.GET_PROJECTION_ID, (movie_id, date, time))

        return result.fetchone()

    @classmethod
    def available_seats(cls, conn, projection_id):
        cursor = conn.cursor()

        result = cursor.execute(cls.GET_SEATS_FOR_PROJECTIONS (projection_id, ))

        return result.fetchall()

    @classmethod
    def show_available_seats(cls, conn, movie_id, date, time):
        pr_id = cls.get_projection_id(conn, movie_id, date, time)
        av_seats = cls.available_seats(conn, pr_id)

        for seat in av_seats:
            x, y = seat
            ALL_SEATS[x][y] = 'X'
