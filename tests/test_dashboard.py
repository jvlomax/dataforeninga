import unittest
import os
from main import app, db, Members, Servers
import configs
from flask.ext.testing import TestCase


class TestOverviewCase(TestCase):

    def create_app(self):
        app.config.from_object(configs.TestConfig)

        return app

    def setUp(self):
        db.create_all()
        member = Members(first_name="Bjarne", last_name="Betjent", position="member", phone="666", mail="bjarne@betjent.com")
        db.session.add(member)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_table(self):
        rv = self.client.get("/dashboard/overview.html")
        assert rv.status_code == 200


        resp = self.client.get("/dashboard/overview.html")
        assert "Bjarne" in resp.data.decode("utf-8")
        assert "Max" not in resp.data.decode("utf-8")

    def test_charts(self):
     pass


class TestMembersCase(TestCase):

    def create_app(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
        return app

    def setUp(self):
        db.create_all()
        member = Members(first_name="Bjarne",
                         last_name="Betjent",
                         position="member",
                         phone="666",
                         mail="bjarne@betjent.com")
        db.session.add(member)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def test_table(self):
        resp = self.client.get("dashboard/members.html")
        self.assertStatus(resp, 200)
        self.assertIn("Bjarne", resp.data.decode("utf-8"))

    def test_add_member(self):
        resp = self.client.get("dashboard/members.html")
        self.assertNotIn("Max@mekker", resp.data.decode("utf-8"))
        member = Members(first_name="Max",
                         last_name="Mekker",
                         position="Leader",
                         phone="333",
                         mail="max@mekker.no")
        db.session.add(member)
        db.session.commit()
        resp = self.client.get("dashboard/members.html")
        self.assertIn("Max", resp.data.decode("utf-8"))

    def test_remove_member(self):
        bjarne = Members.query.filter_by(first_name='Bjarne').first()
        db.session.delete(bjarne)
        db.session.commit()
        resp = self.client.get("dashboard/members.html")
        self.assertNotIn("Bjarne", resp.data.decode("utf-8"))

    def test_edit_member(self):
        bjarne = Members.query.filter_by(first_name="Bjarne").first()
        bjarne.mail = "ilovepenis@ss.no"
        db.session.commit()
        resp = self.client.get("dashboard/members.html")
        self.assertNotIn("bjarne@betjent.com", resp.data.decode("utf-8"))
        self.assertIn("ilovepenis@ss.no", resp.data.decode("utf-8"))

class TestServersCase(TestCase):
    def create_app(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
        return app

    def setUp(self):
        db.create_all()
        server = Servers(uid=8, server_name="creeper", ip_address="129.242.219.41")
        db.session.add(server)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_table(self):
        resp = self.client.get("dashboard/servers.html")
        self.assertStatus(resp, 200)
        self.assertIn("129.242.219.41", resp.data.decode("utf-8"))

    def test_add_server(self):
        pass

    def test_remove_server(self):
        pass

    def test_edit_server(self):
        pass


class TestExport(TestCase):
    def create_app(self):
        app.config["TESTING"]
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
        return app


    def test_export_csv(self):
        resp = self.client.get("dashboard/export.html")
        self.assertStatus(resp, 200)
if __name__ == "__main__":
    unittest.main()