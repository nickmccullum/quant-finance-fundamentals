from database import CursorFromConnectionPool

class User:
    def __init__(self, email, first_name, last_name, id=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return "<User {}>".format(self.email)

    def save_to_db(self):
        # This is creating a new connection pool every time! Very expensive...
        with CursorFromConnectionPool() as cursor:
            cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)',
                            (self.email, self.first_name, self.last_name))

    @classmethod
    def load_from_db_by_email(cls, email):
        with CursorFromConnectionPool() as cursor:
            # Note the (email,) to make it a tuple!
            cursor.execute('SELECT * FROM users WHERE email=%s', (email,))
            user_data = cursor.fetchone()
            return cls(email=user_data[1], first_name=user_data[2], last_name=user_data[3], id=user_data[0])
