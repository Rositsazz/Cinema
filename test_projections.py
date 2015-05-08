import unittest
import sqlite3
from projections import Projections


class TestProjections(unittest.TestCase):

    def setUp(self):
        self.p = Projections()
        self.conn = sqlite3.connect('movie.db')
    
    def test_bla(self):
      print(Projections.show_projections(self.conn))


if __name__ == '__main__':
    unittest.main()