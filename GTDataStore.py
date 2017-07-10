from Activity import Activity

import sqlite3

class GTDataStore(object):
    def __init__(self):
        self.connection = None
        self.db = None

    def set_db(self, db_path):
        self.db = db_path

    def get_db(self):
        return self.db

    def create_db(db_name):
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        # Create the users table
        sql = """CREATE TABLE users (id integer, name text, race_num integer)"""
        c.execute(sql)

        # Create the ride data table
        sql = """
            CREATE TABLE rides 
                (activity integer, rider integer, name text, date text, ride_time text, distance
                integer, elevation integer)
            """
        c.execute(sql)
        conn.commit()
        conn.close()

    def create_connection(self):
        self.connection = sqlite3.connect(self.db)

    def get_db_cursor(self):
        return self.connection.cursor()

    def commit_and_close(self):
        self.conection.commit()
        self.connection.close()

    def store_if_new(act_list):
        """
        check if the activity is already in the DB, store if not.
        Select by Activity ID, if no record returned then store
        """
        self.create_connection()
        c = self.get_db_cursor()
        for act in act_list:
            ride_id = (act.get_strava_id(),)
            sql = 'SELECT * FROM rides WHERE activity=?'
            c.execute(sql, ride_id)
            if c.fetchone() is None:
                ride_data = (act.get_strava_id(), act.get_athlete(), act.get_name(),
                             act.get_gmt_date(), act.get_elapsed_time(), act.get_distance(),
                             act.get_elevation())
                sql = 'INSERT INTO rides VALUES (?, ?, ?, ?, ?, ?, ?)'
                c.execute(sql, ride_data)
        self.commit_and_close()

