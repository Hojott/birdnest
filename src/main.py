#!/usr/bin/env python
#
# main.py is used as a command line tool.
# The website uses wsgi.py, and should be
# run with ´flask run´ in src/
#

from drones import breaching_drones
from pilots import get_contacts

def cmd_tool():
    """ Command line tool for displaying breaches
    """

    bad_drones = breaching_drones()
    pilot_contacts = get_contacts(bad_drones)

    print("Pilots in breach of NDZ:")
    if len(pilot_contacts) == 0:
        print(" None")
    else:
        for pilot in pilot_contacts:
            print(f" - {pilot.name}\n   - {pilot.email}\n   - {pilot.phone}")

if __name__ == "__main__":
    cmd_tool()