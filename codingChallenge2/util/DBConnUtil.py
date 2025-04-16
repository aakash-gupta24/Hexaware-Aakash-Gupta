import pyodbc

class DBConnUtil:
    @staticmethod
    def get_connection(conn_str):
        try:
            conn = pyodbc.connect(conn_str)
            print("Connection established successfully.")
            return conn
        except Exception as e:
            print(f"Failed to connect to DB: {e}")
            return None
