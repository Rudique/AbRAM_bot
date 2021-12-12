import sqlite3


class Database:
    def __init__(self, path_to_db="data/main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, params: tuple = None, fetchone=False,
                fetchall=False, commit=False):
        if not params:
            params = tuple()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        cursor.execute(sql, params)
        data = None

        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users(
        id int NOT NULL,
        name varchar(255) NOT NULL,
        notification_time int,
        set_time varchar(255),
        PRIMARY KEY (id)     
        );       
        
        """
        self.execute(sql, commit=True)

    def add_user(self, id: int, name: str, notification_time=0, set_time=None):
        sql = "INSERT INTO Users(id, name, notification_time, set_time) VALUES(?, ?, ?, ?)"
        parameters = (id, name, notification_time, set_time, )
        self.execute(sql, params=parameters, commit=True)

    def select_all_users(self):
        sql = "SELECT * FROM users"
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, params: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in params
        ])
        return sql, tuple(params.values())

    def select_user(self, **kwargs):
        sql = "SELECT * FROM users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_notification(self, time, setting_time, id):
        sql = "UPDATE Users SET notification_time=?, set_time=? WHERE id=?"
        return self.execute(sql, params=(time, setting_time, id), commit=True)

    def delete_user(self):
        self.execute("DELETE FROM Users WHERE True")


def logger(statement):
    print(f"""
--------------------------------------------------------------------
Executing:
{statement}

____________________________________________________________________
""")
