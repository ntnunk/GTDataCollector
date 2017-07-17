from stravalib.client import Client
from stravalib import unithelper

from Activity import Activity
from GTDataStore import GTDataStore
from Challenge import Challenge

import xml.etree.ElementTree as et

import os
import glob
import string

class GTDataCollector(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

        self.strava_config = {}
        self.config_list = []
        self.challenge_list = []
        self.read_config()
        for challenge in self.challenge_list:
            self.collect_ride_data(challenge)
            self.generate_export_file(challenge)

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

        element = config_tree.find('strava')
        for el in element:
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
        element = config_tree.find('challenge')
        self.challenge_dir = element.attrib['config-folder']
        if not os.path.exists(self.challenge_dir):
            print "Challenge directory doesn't exist"
            return False
        for cconfig in glob.glob(os.path.join(self.challenge_dir, "*.xml")):
            print cconfig
            self.config_list.append(cconfig)

        self.read_challenge_configs(self.config_list)

    def read_challenge_configs(self, config_list):
        """
        Read and parse the challenge configuration file(s)
        """
        for config in config_list:
            tree = et.parse(config)
            root = tree.getroot()
            if not root.tag == 'challenge':
                print 'Invalid config found'
                continue
            c = Challenge()
            for el in root:
                if el.tag == 'common':
                    c.set_name(el.attrib['name'])
                    if el.attrib['allow-virtual'] == 'true':
                        c.set_allow_virtual(True)
                    else:
                        c.set_allow_virtual(False)

                    if el.attrib['allow-trainer'] == 'true':
                        c.set_allow_trainer(True)
                    else:
                        c.set_allow_trainer(False)
                elif el.tag == 'group':
                    c.set_group_id(el.attrib['id'])
                    c.set_group_name(el.attrib['name'])
                elif el.tag == 'database':
                    c.set_db_path(os.path.join(el.attrib['path'], el.attrib['file']))
                elif el.tag == 'export':
                    c.set_export_info(el.attrib['path'], el.attrib['file'], el.attrib['type'],
                                      el.attrib['append-date'])
                elif el.tag == 'contact-list':
                    for user in el.findall('user'):
                        c.add_contact(user.attrib['firstname'], user.attrib['lastname'],
                                      user.attrib['email'])
            self.challenge_list.append(c)
        print self.challenge_list

    def collect_ride_data(self, challenge):
        """
        Pull the latest ride data from Strava via the API
        """
        client = Client()
        client.access_token = self.strava_config['access-token']
        #activities = client.get_club_activities(165009)
        activities = client.get_club_activities(challenge.get_group_id())

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
        db_store = GTDataStore(challenge.get_db_path(), self.verbose)
        db_store.store_if_new(act_list)

    def generate_export_file(self, challenge):
        """
        Generate the CSV for export
        """
        db_store = GTDataStore(challenge.get_db_path(), self.verbose)
        db_store.get_challenge_records('2017-07-01', '2017-07-23')

    def send_export_file(self, export_file):
        """
        Email the export file
        """
        pass

if __name__ == '__main__':
    gtdc = GTDataCollector(verbose=True)
