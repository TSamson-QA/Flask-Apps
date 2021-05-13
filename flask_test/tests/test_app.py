# Import the necessary modules
from flask import url_for
from flask_testing import TestCase

# import the app's classes and objects
from app import app, db, Register

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@34.105.221.153:3306/flask_instance",
        SECRET_KEY='TEST_SECRET_KEY', debug=True, WTF_CSRF_ENABLED=False)
        return app

    def setUp(self):

        db.create_all()
        sample1 = Register(name="MissWoman")

        db.session.add(sample1)
        db.session.commit()

def tearDown(self):

    db.session.remove()
    db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'MissWoman', response.data)

class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for('home'),
            data = dict(name="MrMan"),
            follow_redirects=True
        )
        self.assertIn(b'MrMan',response.data)