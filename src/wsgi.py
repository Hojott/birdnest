#!/usr/bin/env python
from flask import Flask, render_template

from drones import breaching_drones
from pilots import get_contacts

app = Flask(__name__)

@app.route("/birdnest")
def webpage():
    """ Webpage that has contact info of pilots in breach
    """

    bad_drones = breaching_drones()
    breaches = get_contacts(bad_drones)

    return render_template("index.html", breaches=breaches)