## MyFitnessPal Grand Tour Challenge Data Collection Tool

### Project Summary
A simple tool to assist with data collection for the Grant Tour Challenges hosted on the
MyFitnessPal community. 

This tool's purpose is to automate the collection of bicycle ride data from specifc groups on
Strava, collates and arranges the data into desired import formats for other tools used in the
challenges.

### Configuration
Configuration is controlled via an XML file. The format of the file is as follows:

```xml
<gtdata>
    <strava>
        <!-- Client ID and Client Secret Probably aren't needed -->
        <client id="your-client-id"
            secret="your-client-secret"
            access-token="your-access-token">
        </client>
        <group id="strava-group-id"
            name="strava-group-name">
        </group>
    </strava>
    <database>
        <path name="/database/path"></path>
        <file name="database_file.db"></file>
    </database>
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
</gtdata>
```
### Status
This script is very early pre-alpha. Some work to be done to finish core functionality, more work to
be done for error checking, data validation, etc.

