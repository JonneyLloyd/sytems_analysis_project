# This is a sample test. Create tests in separate files
# Run all tests with:  nosetests -v ./tests

# Notice: Class name and method name must start with Test and test_ in order to be picked up by nose

class TestSample:
    @classmethod
    def setup_class(cls):
        # Example: Load dummy sqlite DB
        print ("Runs before any methods in this class")

    @classmethod
    def teardown_class(cls):
        # Example: Clear dummy DB
        print ("Runs after all methods in this class")

    def setup(self):
        # Example: Set default values in the DB?
        print ("Runs before each test method")

    def teardown(self):
        # Example: Rollback before the next test
        print ("Runs after each test method")

    def test_good(self):
        # An actual test
        # import modules/classes/functions and give sample input with expected output
        assert True == True

    def test_stupid(self):
        # Another test
        assert True == False  # Fails as you imagine
