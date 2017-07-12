class Activity(object):
    def __init__(self, strava_id, athlete=None, name=None, distance=None, 
                 elevation=None, gmt_date=None, elapsed_time=None, ride_type=None, trainer=None):
        self.strava_id = strava_id
        self.athlete = athlete
        self.name = name
        self.distance = distance
        self.elevation = elevation
        self.gmt_date = gmt_date
        self.elapsed_time = elapsed_time
        self.ride_type = ride_type
        self.trainer = trainer

    def set_strava_id(self, strava_id):
        """ The Strava ride ID """
        self.strava_id = strava_id

    def get_strava_id(self):
        """ 
        The Strava ride ID. Currently a real/float.
        Integer possible in Python SQLite? Also, Enforce here?
        """
        return self.strava_id

    def set_athlete(self, athlete):
        self.athlete = athlete

    def get_athlete(self):
        """ Strava Athlete ID """
        return self.athlete

    def set_name(self, name):
        """ Strava Ride Name """
        self.name = name

    def get_name(self):
        """ Strava Ride Name """
        return self.name

    def set_distance(self, distance):
        """ 
        Distance should be km, 2 decimals
        Should this be done/enforced here?
        """
        self.distance = distance

    def get_distance(self):
        """
        Distance should be km, 2 decimals
        should this be done/enforced here?
        """
        return self.distance

    def set_elevation(self, elevation):
        """ Total elevation in meters """
        self.elevation = elevation

    def get_elevation(self):
        """ Total elevation in meters """
        return self.elevation

    def set_gmt_date(self, gmt_date):
        """
        Defaults to DateTime.DateTime. Need to add ability to set
        as either DateTime object or string.
        """
        self.gmt_date = gmt_date

    def get_gmt_date(self, as_string=True):
        if as_string:
            return self.gmt_date.strftime("%Y-%m-%d %H:%M:%S.%f") # String for sqlite
        else:
            return self.gmt_date # as DateTime.DateTime object

    def set_elapsed_time(self, elapsed_time):
        """
        Defaults to DateTime.TimeDelta object. Need to add
        ability to set as either TimeDelta object or string.
        """
        self.elapsed_time = elapsed_time

    def get_elapsed_time(self, as_string=True):
        if as_string:
            return str(self.elapsed_time) # String for sqlite
        else:
            return self.elapsed_time # As DateTime.TimeDelta object

    def set_ride_type(self, ride_type):
        self.ride_type = ride_type

    def get_ride_type(self):
        return self.ride_type

    def set_trainer_ride(self, trainer):
        self.trainer = trainer

    def get_trainer_ride(self):
        return self.trainer

