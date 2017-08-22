## MyFitnessPal Grand Tour Challenge Data Collection Tool

### Project Summary
A simple tool to assist with data collection for the Grant Tour Challenges hosted on the
MyFitnessPal community. 

This tool's purpose is to automate the collection of bicycle ride data from specifc groups on
Strava then collate and arrange the data into desired import formats for other tools used in the
challenges.

### Configuration
Configuration is controlled via XML files. First is a "common" configuration file that contains
Strava API information. This file should be be named "config.xml" and should be located in the
same folder as the executable script. It should be set up per-user (user being a challenge
administrator that's collecting data for a given challenge.) and contains the following format:

```xml
<gtdata>
    <strava>
        <!-- Client ID and Client Secret Probably aren't needed -->
        <client id="your-client-id"
            secret="your-client-secret"
            access-token="your-access-token">
        </client>
    </strava>

    <!--
    The local folder the challenge configuration files are located in.
    The script will collect and process data for all challenge config
    files found in this folder.
    -->
    <challenge config-folder="."/>
</gtdata>
```
Upon execution, the script will read and parse any XML files found in the challenge config folder
defined in the common confuration file. Any valid challange configuration files that are found in
the folder will be processed.

Challenge configuration files contain the information for a given challenge. A single user
(challenge administrator) could have multiple configuration files in the event that there are
multiple challenges running simultaneuously. The challenge configuration file is as follows:

```xml
<challenge>
    <!-- 
    Common parameters, including challenge name and whether or not to allow virtual
    rides (Zwift, et al) and/or indoor trainer rides. These values both default to true
    -->
    <common name="Challenge Name" allow-virtual="true|false" allow-trainer="true|false">

    <!-- The Strava group the ride data is collected from -->
    <group id="strava-group-id"
        name="strava-group-name">
    </group>

    <!-- The local database the ride data is saved into -->
    <database path="/database/path" file="database_file.db">
    </database>

    <!-- The export file definition -->
    <export path="./challenges"
        file="file-prefix"
        type="csv"
        append-date="true">
    </export>

    <!-- The contact list data export files are sent to -->
    <contact-list>
        <!-- As many users as desired can be configured -->
        <user firstname="First"
            lastname="Last"
            email="email@address.com">
        </user>
        <user firstname="Second"
            lastname="Contact"
            email="secondguy@address.com">
        </user>
    </contact-list>
</challenge>
```
### Status
This script is very early pre-alpha. Some work to be done to finish core functionality, more work to
be done for error checking, data validation, etc.

