class Activity(object):
    def __init__(self, strava_id, athlete=None, name=None, distance=None, elevation=None, gmt_date=None, elapsed_time=None):
        self.strava_id = strava_id
        self.athlete = athlete
        self.name = name
        self.distance = distance
        self.elevation = elevation
        self.gmt_date = gmt_date
        self.elapsed_time = elapsed_time

    def set_strava_id(self, strava_id):
        self.strava_id = strava_id

    def get_strava_id(self):
        return self.strava_id

    def set_athlete(self, athlete):
        self.athlete = athlete

    def get_athlete(self):
        return self.athlete

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

    def set_elevation(self, elevation):
        self.elevation = elevation

    def get_elevation(self):
        return self.elevation

    def set_gmt_date(self, gmt_date):
        self.gmt_date = gmt_date

    def get_gmt_date(self):
        return self.gmt_date.strftime("%Y-%m-%d %H:%M:%S.%f")

    def set_elapsed_time(self, elapsed_time):
        self.elapsed_time = elapsed_time

    def get_elapsed_time(self):
        return str(self.elapsed_time)

