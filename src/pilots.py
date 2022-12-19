#!/usr/bin/env python
import requests
import json

class PilotInfo:
    """ Includes pilot name, contact info and drone serial-number
    """

    def __init__(self, name, email, phone, serial_number):
        self.name = name
        self.email = email
        self.phone = phone
        self.serial_number = serial_number

def get_contactinfo(serial_number):
    """ Returns contact info from serial-number
    """

    link = "https://assignments.reaktor.com/birdnest/pilots/" + serial_number
    data = requests.get(link)
    json_data = json.loads(data.text)
    pilot_info = PilotInfo(
        json_data["firstName"] + " " + json_data["lastName"],
        json_data["email"],
        json_data["phoneNumber"],
        serial_number
    )
    return pilot_info

def get_contacts(drones):
    """ Returns list of contact info from list of drones
    """

    contact_list = []
    for drone in drones:
        contact_info = get_contactinfo(drone.serial_number)
        contact_list.append(contact_info)
    return contact_list