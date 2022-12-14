import pyodbc

class ConnectionError(Exception):
    pass
class CredentialsError(Exception):
    pass
class SQLError(Exception):
    pass

class UseDatabase:

    def __init__(self, config: dict) -> None:
        self.configuration = config

    def __enter__(self) -> 'cursor':
        self.conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=%(server)s;DATABASE=%(database)s;\
            ENCRYPT=%(encrypt)s;UID=%(username)s;PWD=%(password)s' % self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

        

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is pyodbc.ProgrammingError:
            raise SQLError(exc_value)
        elif exc_type:
            raise exc_type(exc_value)        