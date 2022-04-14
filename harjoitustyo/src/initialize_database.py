from database_connection import get_database_connection


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS players"
                   "(player_id INTEGER PRIMARY KEY,"
                   "playername TEXT)")

    cursor.execute("CREATE TABLE IF NOT EXISTS player_settings"
                   "(player_id INTEGER REFERENCES players,"
                   "apple INTEGER,"
                   "snake INTEGER,"
                   "background INTEGER,"
                   "difficulty INTEGER)")

    cursor.execute("CREATE TABLE IF NOT EXISTS games"
                   "(player_id INTEGER REFERENCES players,"
                   "points INTEGER,"
                   "time INTEGER,"
                   "difficulty INTEGER)")

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    create_tables(connection)
