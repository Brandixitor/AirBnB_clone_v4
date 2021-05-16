#!/usr/bin/python3
<<<<<<< HEAD
""" Starts a Flash Web Application """
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template
from uuid import uuid4
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
=======
""" Starts a Flask application related to HBNB. """

from os import getenv
from flask import Flask, render_template
from models import storage
from models import amenity
from models.state import State
from models.amenity import Amenity
from models.place import Place
from uuid import uuid4

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database session after each request."""
>>>>>>> cc2915ad9bec3ef385068c59ea0b45c2299ae4ba
    storage.close()


@app.route('/2-hbnb', strict_slashes=False)
def hbnb():
<<<<<<< HEAD
    """ HBNB is alive! """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    # Sort cities inside each states
    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

=======
    """
        Flask route at /hbnb.
        Fills the hbnb homepage.
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
>>>>>>> cc2915ad9bec3ef385068c59ea0b45c2299ae4ba
    values = {"states": states, "amenities": amenities,
              "places": places, "cache_id": uuid4()}
    return render_template('2-hbnb.html', **values)


<<<<<<< HEAD
if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
=======
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
>>>>>>> cc2915ad9bec3ef385068c59ea0b45c2299ae4ba
