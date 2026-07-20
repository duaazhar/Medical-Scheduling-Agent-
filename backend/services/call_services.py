from datetime import datetime

from database import db
from models import Call


def create_call(
    patient,
    transcript="",
    status="Started"
):
    """
    Creates a new call record when the patient first
    contacts the scheduling system.
    """

    call = Call(
        patient_id=patient.id,
        caller_phone=patient.phone_number,
        transcript=transcript,
        status=status,
        started_at=datetime.utcnow()
    )

    db.session.add(call)
    db.session.commit()

    return call


def complete_call(
    call,
    appointment=None,
    transcript="",
    status="Scheduled"
):
    """
    Marks a call as successfully completed.
    """

    call.status = status
    call.transcript = transcript
    call.ended_at = datetime.utcnow()

    if appointment is not None:
        call.appointment_id = appointment.id

    db.session.commit()

    return call


def fail_call(
    call,
    transcript="",
    status="Failed"
):
    """
    Marks a call as failed.
    """

    call.status = status
    call.transcript = transcript
    call.ended_at = datetime.utcnow()

    db.session.commit()

    return call