import requests
from lxml import etree, objectify

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

    for appt, e, i in root.getchildren():
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

if __name__ == "__main__":
    print(get_drones())