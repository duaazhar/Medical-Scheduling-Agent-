from app import app

from models import Patient

from services.booking_service import book_appointment


with app.app_context():

    patient = Patient.query.first()

    result = book_appointment(
        patient,
        "Knee",
        "Fracture"
    )

    if result["success"]:

        print("\nBOOKING SUCCESS\n")

        print("Doctor:")
        print(result["doctor"].name)

        print()

        print("Appointment ID:")
        print(result["appointment"].id)

        print()

        print("Slot:")
        print(result["slot"].start_time)

    else:

        print(result["reason"])