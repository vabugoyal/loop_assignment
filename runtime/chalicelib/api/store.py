import logging


from chalice import Blueprint, BadRequestError, UnauthorizedError

from ..constants import *
from ..models.store import StoreStatus, StoreBusinessHours, StoreTimeZone
from ..services.store import generate_report_last_n_days

store_routes = Blueprint('store')
logger = logging.getLogger(__name__)


@store_routes.route('/dummy', methods=['GET'], cors=True)
def dummy():
    # read the csv and do the entries in the database
    print("This is working.")
    return {"status": "working"}


@store_routes.route('/{id}/report', methods=['POST'], cors=True)
def generate_report(id):
    """Given a store id generate a report of the store for last week."""
    """
    Fetch all the polls of this store done in last week.
    """
    last_week_report = generate_report_last_n_days(id, 7)
    last_day_report = generate_report_last_n_days(id, 1)
    return last_week_report, last_day_report
