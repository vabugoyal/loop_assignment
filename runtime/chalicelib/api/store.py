import logging


from chalice import Blueprint, BadRequestError, UnauthorizedError

from ..constants import *
from ..models.store import StoreStatus, StoreBusinessHours, StoreTimeZone
from ..services.store import generate_report_last_n_days, generate_report_last_hour

store_routes = Blueprint('store')
logger = logging.getLogger(__name__)


@store_routes.route('/{id}/report', methods=['POST'], cors=True)
def generate_report(id):
    """Given a store id generate a report of the store for last week."""
    """
    Fetch all the polls of this store done in last week.
    """
    last_hour_report = generate_report_last_hour(id)
    return last_hour_report


@store_routes.route('/trigger_report', methods=['POST'], cors=True)
def generate_report():

    pass


@store_routes.route('/get_report', methods=['GET'], cors=True)
def generate_report(id):

    pass