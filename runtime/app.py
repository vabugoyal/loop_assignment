import logging 
import os
import sys
import json
import leangle
import pandas as pd

from chalice import Chalice, CORSConfig, Response
from dotenv import load_dotenv

load_dotenv()

from chalicelib.api.store import store_routes

app = Chalice(app_name='MyProject')
app.debug = True
app.log.setLevel(logging.DEBUG)
app.register_blueprint(store_routes, url_prefix='/store')


@app.route('/healthcheck', methods=['GET'], cors=True)
def index():
    return {'status': 'healthy'}







