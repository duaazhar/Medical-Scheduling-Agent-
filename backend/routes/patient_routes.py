from flask import Blueprint
from flask import jsonify
from flask import request

from services.patient_service import (
    get_all_patients,
    get_patient_by_phone,
    create_patient, 
    get_or_create_patient
)


patient_bp = Blueprint(
    "patients",
    __name__
)

@patient_bp.route(
    "/patients",
    methods=["GET"]
)
def get_patients():

    patients = get_all_patients()

    results = []

    for patient in patients:

        results.append({

            "id": patient.id,

            "first_name": patient.first_name,

            "last_name": patient.last_name,

            "phone_number": patient.phone_number

        })

    return jsonify(results)

@patient_bp.route(
    "/patients/<phone_number>",
    methods=["GET"]
)
def get_patient(phone_number):

    patient = get_patient_by_phone(
        phone_number
    )

    if patient is None:

        return jsonify({
            "error": "Patient not found"
        }), 404

    return jsonify({

        "id": patient.id,

        "first_name": patient.first_name,

        "last_name": patient.last_name,

        "phone_number": patient.phone_number

    })

@patient_bp.route(
    "/patients",
    methods=["POST"]
)
def add_patient():

    data = request.get_json()

    patient = create_patient(

        first_name=data["first_name"],

        last_name=data["last_name"],

        phone_number=data["phone_number"],

        date_of_birth=data.get("date_of_birth")

    )

    return jsonify({

        "message": "Patient created",

        "id": patient.id

    }), 201