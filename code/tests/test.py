# This is a sample test. Create tests in separate files
# Run all tests with:  nosetests -v ./tests

# Notice: Class name and method name must start with Test and test_ in order to be picked up by nose

from app.app_factory import AppFactory
from app.extensions import db
from config import TestConfig


class BaseDatabaseTest(object):
    '''
    Base class for testing with a dummy database.
    '''
    @classmethod
    def setup_class(cls):
        # Example: Load dummy sqlite DB
        print ("Runs before any methods in this class")
        cls.app = AppFactory.create_app(TestConfig)
        # db.init_app(cls.app)

        with cls.app.app_context():
            db.create_all()
            # populate here or in sub class

    @classmethod
    def teardown_class(cls):
        # Example: Clear dummy DB
        print ("Runs after all methods in this class")
        with cls.app.app_context():
            db.drop_all()

    def setup(self):
        # Example: Set default values in the DB? Set up transaction?
        print ("Runs before each test method")

    def teardown(self):
        # Example: Rollback before the next test
        print ("Runs after each test method")


class TestCase(BaseDatabaseTest):
    def test_good(self):
        # An actual test
        # import modules/classes/functions and give sample input with expected output
        assert True == True
