from sqlalchemy import create_engine, select

class SQLEngine:
    def __init__(self):
        self.host = ""
        self.port = ""
        self.username = ""
        self.database = ""
        self.engine = None

    def create_engine(self):
        # Path to SQLite database file
        database = "data/form_d_database.db"
        path = "Users/tktakaro/PycharmProjects/primeAssessment/"
        # Establish connection to database and create engine
        connection_string = "'sqlite:////" + path + database
        self.engine = create_engine(connection_string)

        self.test_connection()

    def test_connection(self):
        # Check if sql engine is running
        if not self.engine:
            err = "SQL Engine has not started. Please create engine first."
            raise Exception(err)

        try:
            connection = self.engine.connect()
        except Exception as err:
            raise Exception(err)

    def get_data(self):
        return