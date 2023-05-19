import logging
import threading

from chalice import Blueprint, BadRequestError, UnauthorizedError, Response

from ..constants import *
from ..models.store import StoreTimeZone, Store
from ..models.report import ReportStatus
from ..services.report_generation import generate_report, generate_csv_report

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
    report_status = ReportStatus.create(status=0)

    # I will be doing report generation in a separate thread
    # for deployment we could have used a sqs queue here
    # as this is a long running task
    thread = threading.Thread(target=generate_report, args=[report_status.id])
    thread.start()
    # generate_report(report_status.id)

    return {
        "report_id" : report_status.id
    }


@store_routes.route('/get_report/{id}', methods=['GET'], cors=True)
def get_report(id):
    report = ReportStatus.find_or_fail(id)
    print(report.status)
    if not report.status:
        return "Running"

    file_name = "report.csv"
    file_path = file_name

    generate_csv_report(id, file_name)

    with open(file_path, 'rb') as f:
        contents = f.read()

    headers = {'Content-Type': 'application/octet-stream',
        'Content-Disposition': 'attachment; filename={}'.format(file_name),
        'Content-Length': str(os.path.getsize(file_path))
    }
    return Response(body=contents, headers=headers)

