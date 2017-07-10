from stravalib.client import Client
from stravalib import unithelper

from Activity import Activity
from GTDataStore import GTDataStore

import xml.etree.ElementTree as et

import os
import string

class GTDataCollector(object):
    def __init__(self):
        self.strava_config = {}
        self.contact_list = []
        self.read_config()

        print self.strava_config
        print self.contact_list

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
                self.strava_config['id'] = el.attrib['id']
                self.strava_config['secret'] = el.attrib['secret']
                self.strava_config['access-token'] = el.attrib['access-token']
            elif el.tag == 'group':
                self.strava_config['group-name'] = el.attrib['name']
                self.strava_config['group-id'] = el.attrib['id']

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
            if not activity.type == "Ride" or activity.trainer == True:
                # This is either not a bicycle ride or it's an indoor ride of some type. Disregard.
                continue
            act = Activity(activity.id)
            act.set_athlete(activity.athlete.id)
            act.set_name(activity.name)
            act.set_gmt_date(activity.start_date) # GMT Start date
            act.set_elapsed_time(activity.elapsed_time)
            act.set_distance(round(unithelper.kilometers(activity.distance).num, 2))
            act.set_elevation(unithelper.meters(activity.total_elevation_gain).num)
            act_list.append(act)
        db_store = GTDataStore()
        db_store.store_if_new(act_list)

    def store_ride_data(self, ride_data):
        """
        Store the collected ride data in the database table
        """
        pass

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
    gtdc = GTDataCollector()
    gtdc.collect_ride_data()
