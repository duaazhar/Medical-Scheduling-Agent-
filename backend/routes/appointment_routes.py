from flask import Blueprint, jsonify, request

from services.patient_service import get_or_create_patient
from services.booking_service import book_appointment
from services.call_services import (
    create_call,
    complete_call,
    fail_call
)
from models import Patient

appointment_bp = Blueprint(
    "appointments",
    __name__
)


@appointment_bp.route(
    "/appointments/book",
    methods=["POST"]
)

def book():

    data = request.get_json()

    # Support Vogent's function payload format
    if "params" in data and "args" in data["params"]:
        data = data["params"]["args"]

    # -----------------------------
    # Validate request body
    # -----------------------------
    required_fields = [
        "first_name",
        "last_name",
        "phone_number",
        "body_part",
        "issue_type"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "success": False,
                "reason": f"Missing required field: {field}"
            }), 400

    # -----------------------------
    # Extract request fields
    # -----------------------------
    first_name = data["first_name"]
    last_name = data["last_name"]
    phone_number = data["phone_number"]
    date_of_birth = data.get("date_of_birth")

    body_part = data["body_part"]
    issue_type = data["issue_type"]

    preferred_time = data.get(
    "preferred_time",
    "Earliest Available"
    )

    transcript = data.get("transcript", "")

    # -----------------------------
    # Find or create patient
    # -----------------------------
    patient = get_or_create_patient(
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        date_of_birth=date_of_birth
    )

    # -----------------------------
    # Start call log
    # -----------------------------
    call = create_call(
        patient=patient,
        transcript=transcript
    )

    # -----------------------------
    # Attempt booking
    # -----------------------------
    result = book_appointment(
        patient,
        body_part,
        issue_type,
        preferred_time
    )

    # -----------------------------
    # Booking failed
    # -----------------------------
    if not result["success"]:

        fail_call(
            call=call,
            transcript=transcript
        )

        return jsonify(result), 400

    # -----------------------------
    # Booking succeeded
    # -----------------------------
    appointment = result["appointment"]
    doctor = result["doctor"]
    slot = result["slot"]

    complete_call(
        call=call,
        appointment=appointment,
        transcript=transcript
    )

    return jsonify({
        "success": True,
        "appointment_id": appointment.id,
        "doctor": doctor.name,
        "location": slot.location.name,
        "start_time": slot.start_time.isoformat(),
        "end_time": slot.end_time.isoformat(),
        "status": appointment.status
    }), 201

@appointment_bp.route(
    "/appointments/patient",
    methods=["POST"]
)
def get_patient_appointments():

    data = request.get_json()

    # Support Vogent function payload
    if "params" in data and "args" in data["params"]:
        data = data["params"]["args"]

    phone_number = str(data.get("phone_number", "")).strip()

    if not phone_number:
        return jsonify({
            "success": False,
            "reason": "Missing phone number"
        }), 400

    patient = Patient.query.filter_by(
        phone_number=phone_number
    ).first()

    if patient is None:
        return jsonify({
            "success": True,
            "appointments": []
        }), 200

    appointments = []

    for appointment in patient.appointments:

        slot = appointment.slot
        doctor = appointment.doctor

        appointments.append({

            "appointment_id": appointment.id,

            "doctor": doctor.name,

            "location": slot.location.name,

            "start_time": slot.start_time.isoformat(),

            "end_time": slot.end_time.isoformat(),

            "status": appointment.status

        })

    return jsonify({

        "success": True,

        "patient": (
            f"{patient.first_name} {patient.last_name}"
        ),

        "appointments": appointments

    }), 200