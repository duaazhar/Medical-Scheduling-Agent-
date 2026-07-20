from flask import Blueprint
from flask import jsonify
from flask import request

from models import Call

call_bp = Blueprint(
    "calls",
    __name__
)

@call_bp.route("/calls", methods=["GET"])
def get_calls():

    calls = Call.query.all()

    results = []

    for call in calls:

        results.append({

            "id": call.id,

            "patient": (
                call.patient.first_name
                + " "
                + call.patient.last_name
            ),

            "status": call.status,

            "started_at": call.started_at.isoformat(),

            "ended_at": (
                call.ended_at.isoformat()
                if call.ended_at else None
            )

        })

    return jsonify(results)