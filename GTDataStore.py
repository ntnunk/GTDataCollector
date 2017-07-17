from Activity import Activity

import os
import sqlite3

class GTDataStore(object):
    def __init__(self, db_path, verbose=False):
        self.verbose = verbose
        self.connection = None
        self.db = db_path
        if not os.path.exists(db_path):
            self.create_db(db_path)

    def set_db(self, db_path):
        self.db = db_path

    def get_db(self):
        return self.db

    def create_db(self, db_name):
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        # Create the users table
        sql = """CREATE TABLE users (id integer primary key, name text, race_num integer)"""
        c.execute(sql)

        # Create the ride data table
        sql = """
            CREATE TABLE rides 
                (activity int primary key, rider integer, name text, date text, ride_time text, distance
                integer, elevation integer, ride_type text, trainer integer)
            """
        c.execute(sql)
        conn.commit()
        conn.close()

    def create_connection(self):
        self.connection = sqlite3.connect(self.db)

    def get_db_cursor(self):
        return self.connection.cursor()

    def commit_and_close(self):
        self.connection.commit()
        self.connection.close()

    def store_if_new(self, act_list):
        """
        check if the activity is already in the DB, store if not.
        Select by Activity ID, if no record returned then store
        """
        self.create_connection()
        c = self.get_db_cursor()
        for act in act_list:
            strava_id = str(act.get_strava_id())
            ride_id = (strava_id,)
            sql = "SELECT date FROM rides WHERE activity=?"
            c.execute(sql, ride_id)
            if c.fetchone() is not None:
                continue
            if self.verbose:
                print 'New ride found: %s' % act.get_name()
            ride_data = (act.get_strava_id(), act.get_athlete(), act.get_name(),
                            act.get_gmt_date(), act.get_elapsed_time(), act.get_distance(),
                            act.get_elevation(), act.get_ride_type(), act.get_trainer_ride())
            sql = 'INSERT INTO rides VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
            c.execute(sql, ride_data)
        self.commit_and_close()

    def get_challenge_records(self, start_date, end_date):
        sql = "SELECT rider, date, distance, ride_time, elevation FROM rides "
        sql += "WHERE (date BETWEEN ? AND ?) AND ride_type='Ride' AND trainer=0 "
        sql += "ORDER BY date;"
        print sql
        self.create_connection()
        c = self.get_db_cursor()
        for row in c.execute(sql, (start_date, end_date)):
            print row
