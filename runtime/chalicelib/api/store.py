import logging


from chalice import Blueprint, BadRequestError, UnauthorizedError

from ..constants import *
from ..models.store import StoreStatus, StoreBusinessHours, StoreTimeZone, Store
from ..models.report import ReportResults, ReportStatus
from ..services.report_generation import generate_report

store_routes = Blueprint('store')
logger = logging.getLogger(__name__)


@store_routes.route('/dummy', methods=['POST'], cors=True)
def dummy():
    stores = StoreTimeZone.all()
    for store in stores:
        try:
            Store.create(store_id=store.store_id)
        except Exception as e:
            continue


@store_routes.route('/trigger_report', methods=['POST'], cors=True)
def trigger_report():
    print("triggered report generation")
    report_status = ReportStatus.create(status=0)

    # I will be doing report generation in a separate thread
    # for deployment we could have used a sqs queue here
    # as this is a long running task
    generate_report(report_status.id)

    report_status.update(status=1)
    return {
        "report_id" : report_status.id
    }


@store_routes.route('/get_report/{id}', methods=['GET'], cors=True)
def get_report(id):
    report = ReportStatus.find_or_fail(id)
    if not report.status:
        return "Running"
    report_results = ReportResults.where(report_id=id).all()


    pass

