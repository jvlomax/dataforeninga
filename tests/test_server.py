import unittest
import os
import main
import tempfile

class MainTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, main.app.config["DATABASE"] = tempfile.mkstemp()

        self.app = main.app.test_client()
        #main.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(main.app.config["DATABASE"])

    def test_empty(self):
        rv = self.app.get("/")
        assert "Tromsøstudentenes dataforening" in rv.data.decode("utf-8")
        assert "default welcome page" not in rv.data.decode("utf-8")

if __name__ == "__main__":
    unittest.main()