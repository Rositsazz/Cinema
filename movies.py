class Movies:

    GET_CURRENT_MOVIES = """
        SELECT id, name, rating
        FROM Movies
    """

    @classmethod
    def show_current_movies(cls, conn):
        try:
            cursor = conn.cursor()

            cursor.execute(cls.GET_CURRENT_MOVIES)
            print("Current movies:")
            for row in cursor:
                print("[{}] - {} with rating {}".format(row[0],
                                                        row[1],
                                                        row[2]))
            conn.commit()
        except:
            pass


