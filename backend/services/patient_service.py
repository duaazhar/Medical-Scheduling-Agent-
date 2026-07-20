from models import Patient
from database import db
from models import Appointment


def get_all_patients():
    return Patient.query.all()


def get_patient_by_phone(phone_number):
    return Patient.query.filter_by(
        phone_number=phone_number
    ).first()


def create_patient(
    first_name,
    last_name,
    phone_number,
    date_of_birth=None
):
    patient = Patient(
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        date_of_birth=date_of_birth
    )

    db.session.add(patient)
    db.session.commit()

    return patient

def is_new_patient(patient):
    appointment = Appointment.query.filter_by(
        patient_id=patient.id
    ).first()

    return appointment is None

def get_or_create_patient(
    first_name,
    last_name,
    phone_number,
    date_of_birth=None
):
    """
    Returns an existing patient if the phone number exists.
    Otherwise creates a new patient.
    """

    patient = get_patient_by_phone(phone_number)

    if patient is not None:
        return patient

    return create_patient(
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        date_of_birth=date_of_birth
    )