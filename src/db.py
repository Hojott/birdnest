import apsw
import time

from pilots import get_contacts, PilotInfo

def create_database():
    """ Creates the database
    """

    conn = apsw.Connection("src/databases/pilots.sql")
    conn.execute(
        """CREATE TABLE pilot(
        name TEXT,
        email TEXT,
        phone TEXT,
        serial_number TEXT,
        distance INTEGER,
        time REAL
        )"""
    )

def try_database():
    """ Checks if database exists, creates it if doesn't, and returns connection to database
    """

    try:
        conn = apsw.Connection("src/databases/pilots.sql", flags=apsw.SQLITE_OPEN_READWRITE)
    except:
        create_database()   # Creates database in case apsw fails to find it
        conn = apsw.Connection("src/databases/pilots.sql")

    finally:
        return conn

def append_database(pilot):
    """ Adds pilot to database, or updating existing one, and deletes pilots over 10min old
    """
    
    conn = try_database()
    cur = conn.cursor()

    cur.execute("SELECT * FROM pilot WHERE serial_number = :serial_number", pilot.__dict__)
    exists = cur.fetchone()
    if exists:
        if int(exists[4]) > pilot.distance:
            cur.execute("UPDATE pilot SET distance = :distance, time = :time WHERE serial_number = :serial_number", pilot.__dict__)
        else:
            cur.execute("UPDATE pilot SET time = :time WHERE serial_number = :serial_number", pilot.__dict__)

    else:
        query = "INSERT INTO pilot VALUES(:name, :email, :phone, :serial_number, :distance, :time)"
        conn.execute(query, pilot.__dict__)

    cur.execute("DELETE FROM pilot WHERE time < ?", [time.time() - 600.0])

    conn.close()

def list_database():
    """ Returns pilots in database
    """
    
    conn = try_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM pilot")

    pilots = cur.fetchall()

    pilot_objects = []
    for pilot in pilots:
        pilot_object = PilotInfo(
            pilot[0],
            pilot[1],
            pilot[2],
            pilot[3],
            pilot[4],
        )
        pilot_objects.append(pilot_object)
    return pilot_objects

def control_database():
    """ Automatically adds new pilots into db
    """
    running = 1
    while running:
        time.sleep(2)
        contacts = get_contacts()

        for contact in contacts:
            append_database(contact)
