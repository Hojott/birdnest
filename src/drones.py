import requests
from lxml import objectify
import math

class DroneCoords:
    """ Includes drone serial-number and coordinates
    """
    def __init__(self, serial_number, pos_y, pos_x):
        self.serial_number = serial_number
        self.pos_y = pos_y
        self.pos_x = pos_x

def parse_drones(xml):
    """ Parses drone XML-data into a list of Python objects
    """

    root = objectify.fromstring(xml)
    serial_numbers = []
    pos_ys = []
    pos_xs = []

    for appt in root.getchildren():
        for e in appt.getchildren():
            for i in e.getchildren():
                if i.tag == "serialNumber":
                    serial_numbers.append(i.text)
                if i.tag == "positionY":
                    pos_ys.append(i.text)
                if i.tag == "positionX":
                    pos_xs.append(i.text)
    
    drones = []
    for serial, y, x in zip(serial_numbers, pos_ys, pos_xs):
        drones.append(DroneCoords(serial, y, x))

    return drones

def get_drones():
    """ Returns drone data and coordinates as a list of Python objects
    """

    link = "https://assignments.reaktor.com/birdnest/drones"
    xml_data = requests.get(link).text
    xml_no_dec = xml_data.replace('<?xml version="1.0" encoding="UTF-8"?>','')
    obj_data = parse_drones(xml_no_dec)
    return obj_data

def breaching_drones():
    """ Returns list of drones that break NDZ and their distance
    """
    drones = get_drones()
    bad_drones = []
    for drone in drones:
        distance = math.hypot(float(drone.pos_y) - 250000.0, float(drone.pos_x) - 250000.0)
        distance = math.floor(distance/1000)
        if distance < 100:
            bad_drones.append([drone, distance])
    return bad_drones