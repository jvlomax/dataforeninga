import unittest
from main import db, app, Members
from flask.ext.testing import TestCase
import configs
class DatabaseTest(TestCase):

    def create_app(self):
        app.config.from_object(configs.TestConfig)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_insert_member(self):
        member = Members(first_name="Bjarne", last_name="betjent", position="Leader", phone="666", mail="bjarne@betjent.com")
        db.session.add(member)
        db.session.commit()

    def test_select_member(self):
        self.test_insert_member()
        bjarne = Members.query.filter_by(first_name="Bjarne").first()
        assert bjarne is not None
        assert bjarne.phone == "666"


if __name__ == "__main__":
    unittest.main()