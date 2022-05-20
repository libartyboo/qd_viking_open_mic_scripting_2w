import sqlite3


class DatabaseConnSQLite:

    def __init__(self, **kwargs):
        self.dbname = kwargs.get("dbname", None)

    def __enter__(self):
        try:
            if not self.dbname:
                raise ValueError
            self.conn = sqlite3.connect(self.dbname)
            return self.conn
        except ValueError:
            print("Invalid connection data")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.commit()
            self.conn.close()
