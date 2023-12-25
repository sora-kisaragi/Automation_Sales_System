import unittest
from sqlalchemy.orm import Session
from database import create_session

class TestDatabase(unittest.TestCase):
    def test_create_session(self):
        session = create_session()
        self.assertIsInstance(session, Session)

if __name__ == '__main__':
    unittest.main()