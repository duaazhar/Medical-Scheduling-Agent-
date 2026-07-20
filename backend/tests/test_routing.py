from app import app
from services.routing_service import find_matching_doctors

with app.app_context():
    doctors = find_matching_doctors(
        "Knee",
        "Fracture"
    )

    for doctor in doctors:
        print(doctor.name)