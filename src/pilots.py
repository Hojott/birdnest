import requests
import json
import time

from drones import breaching_drones

class PilotInfo:
    """ Includes pilot name, contact info and drone serial-number
    """

    def __init__(self, name, email, phone, serial_number, distance):
        self.name = name
        self.email = email
        self.phone = phone
        self.serial_number = serial_number
        self.distance = distance
        self.time = time.time()

def get_contactinfo(drone, distance):
    """ Returns contact info from serial-number
    """

    link = "https://assignments.reaktor.com/birdnest/pilots/" + drone
    data = requests.get(link)
    json_data = json.loads(data.text)
    pilot_info = PilotInfo(
        json_data["firstName"] + " " + json_data["lastName"],
        json_data["email"],
        json_data["phoneNumber"],
        drone,
        distance
    )
    return pilot_info

def get_contacts():
    """ Returns list of contact info of breaching drones
        drones include both serialnumber and distance.
    """

    drones = breaching_drones()

    contact_list = []
    for drone in drones:
        contact_info = get_contactinfo(drone[0].serial_number, drone[1])
        contact_list.append(contact_info)
    return contact_list