import logging
import requests
import random
import string
import os
import binascii
import leangle
import bcrypt
import pandas as pd

from chalice import Blueprint, BadRequestError, UnauthorizedError

from ..constants import *

store_routes = Blueprint('store')
logger = logging.getLogger(__name__)


@store_routes.route('/dummy', methods=['GET'], cors=True)
def dummy():
    # read the csv and do the entries in the database
    print("This is working.")
    return {"status" : "working"}



