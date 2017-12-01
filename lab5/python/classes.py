import MySQLdb


class Connection:
    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    #! Открытие соединения
    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db
            )
            self._connection.set_character_set('utf8')

    #! Закрытие соединения
    def disconnect(self):
        if self._connection:
            self._connection.close()


class Film:

    def __init__(self, db_connection, name, description):
        self.db_connection = db_connection.connection
        self.name = name
        self.description = description

    def save(self):
        c = self.db_connection.cursor()
        c.execute("insert into  films(name, description) values(%s, %s);",
                  (self.name, self.description))
        self.db_connection.commit()
        c.close()

    def show(self):
        c = self.db_connection.cursor()
        c.execute("select * from films;")
        entries = c.fetchall()
        for e in entries:
            print(e)
        c.close()
conn = Connection("dbuser", "123", "first_db")



with conn:
    film = Film(conn, 'Матрица', "Добро пожаловать в реальный мир")
    film.show()