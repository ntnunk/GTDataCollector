from stravalib.client import Client
from stravalib import unithelper

from Activity import Activity
from GTDataStore import GTDataStore

import xml.etree.ElementTree as et

import os
import string

class GTDataCollector(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

        self.strava_config = {}
        self.contact_list = []
        self.read_config()

    def read_config(self):
        """
        Read the configuration from the config.xml file.
        This should contain, at a minimum, the access token
        for the Strava API and the email address(es) to 
        send the export file to. It probably should contain
        the export file path as well.
        """
        config_path = '.'
        config_file = os.path.join(config_path, 'config.xml')
        config_tree = et.parse(config_file)

        strava_element = config_tree.find('strava')
        for el in strava_element:
            if el.tag == 'client':
                if 'id' in el.attrib:
                    self.strava_config['id'] = el.attrib['id']
                else:
                    self.strava_config['id'] = None

                if 'secret' in el.attrib:
                    self.strava_config['secret'] = el.attrib['secret']
                else:
                    self.strava_config['secret'] = None
                self.strava_config['access-token'] = el.attrib['access-token']
            elif el.tag == 'group':
                if 'name' in el.attrib:
                    self.strava_config['group-name'] = el.attrib['name']
                else:
                    self.strava_config['group-name'] = None
                self.strava_config['group-id'] = el.attrib['id']

        db_element = config_tree.find('database')
        db_name = None
        db_path = None
        for el in db_element:
            if el.tag == 'path':
                db_path = el.attrib['name']
            elif el.tag == 'file':
                db_name = el.attrib['name']

        if db_name is not None and db_path is not None:
            self.db_path = os.path.join(db_path, db_name)
        else:
            self.db_path = os.path.join('.', 'gtdc.db')

        contact_list_element = config_tree.find('contact-list')
        for el in contact_list_element:
            user = {}
            if el.tag == 'user':
                user['firstname'] = el.attrib['firstname']
                user['lastname'] = el.attrib['lastname']
                user['email'] = el.attrib['email']
            self.contact_list.append(user)

    def collect_ride_data(self):
        """
        Pull the latest ride data from Strava via the API
        """
        client = Client()
        client.access_token = self.strava_config['access-token']
        activities = client.get_club_activities(165009)

        act_list = []
        for activity in activities:
            if not activity.type == 'Ride' and not activity.type == 'VirtualRide':
                print 'Non-ride activity: %s, type: %s' % (activity.name, activity.type)
                continue
            act = Activity(activity.id)
            act.set_athlete(activity.athlete.id)
            act.set_name(activity.name)
            act.set_gmt_date(activity.start_date) # GMT Start date
            act.set_elapsed_time(activity.elapsed_time)
            act.set_distance(round(unithelper.kilometers(activity.distance).num, 2))
            act.set_elevation(unithelper.meters(activity.total_elevation_gain).num)
            act.set_ride_type(activity.type)
            act.set_trainer_ride(activity.trainer)
            act_list.append(act)
        db_store = GTDataStore(self.db_path, self.verbose)
        db_store.store_if_new(act_list)

    def generate_export_file(self, export_path):
        """
        Generate the CSV for export
        """
        pass

    def send_export_file(self, export_file):
        """
        Email the export file
        """
        pass

if __name__ == '__main__':
    gtdc = GTDataCollector(verbose=True)
    gtdc.collect_ride_data()
