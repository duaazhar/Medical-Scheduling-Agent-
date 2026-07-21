from database import db

from models import (
    Appointment,
    BodyPart,
    IssueType,
)

from services.routing_service import route_patient


def book_appointment(
    patient,
    body_part_name,
    issue_type_name,
    preferred_time="Earliest Available"
):
    """
    Routes the patient and books the earliest available appointment.

    Returns:
        {
            "success": True,
            "appointment": Appointment,
            "doctor": Doctor,
            "slot": Slot
        }

    or

        {
            "success": False,
            "reason": "<reason>"
        }
    """

    routing_result = route_patient(
        patient,
        body_part_name,
        issue_type_name,
        preferred_time
    )

    if not routing_result["success"]:
        return routing_result

    doctor = routing_result["doctor"]
    slot = routing_result["slot"]

    body_part = BodyPart.query.filter_by(
        name=body_part_name
    ).first()

    issue_type = IssueType.query.filter_by(
        name=issue_type_name
    ).first()

    if body_part is None or issue_type is None:
        return {
            "success": False,
            "reason": "Invalid body part or issue type."
        }
    
    if not slot.is_available:
        return {
            "success": False,
            "reason": "Selected appointment slot is no longer available."
        }

    slot.is_available = False

    appointment = Appointment(
        patient_id=patient.id,
        doctor_id=doctor.id,
        slot_id=slot.id,
        body_part_id=body_part.id,
        issue_type_id=issue_type.id,
        status="Scheduled"
    )

    db.session.add(appointment)

    db.session.commit()

    return {
        "success": True,
        "appointment": appointment,
        "doctor": doctor,
        "slot": slot
    }