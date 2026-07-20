from app import app

from models import Patient
from database import db
from services.routing_service import route_patient

with app.app_context():

    patient = Patient.query.first()

    if patient is None:
        patient = Patient(
            first_name="John",
            last_name="Smith",
            phone_number="5551234567"
        )

        db.session.add(patient)
        db.session.commit()

    result = route_patient(
        patient,
        "Knee",
        "Fracture"
    )

    if result is None:
        print("No match found")
    else:
        print(result["doctor"].name)
        print(result["slot"].start_time)