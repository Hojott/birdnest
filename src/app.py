from flask import Flask, render_template
from time import sleep

from drones import breaching_drones
from pilots import get_contacts
from db import list_database

def flask_app():
    """ Runs the entire Flask application
    """

    app = Flask(__name__)

    @app.route("/")
    def wip():
        """ WIP Webpage
        """

        return render_template("wip.html")

    @app.route("/birdnest", methods=['GET', 'POST'])
    def webpage():
        """ Webpage that has contact info of pilots in breach
        """

        try:
            breaches = list_database()
        except:
            sleep(0.5)  # in case database is locked by control_database in other thread
            breaches = list_database()
        finally:
            return render_template("index.html", breaches=breaches)
    
    app.run(host="0.0.0.0")
