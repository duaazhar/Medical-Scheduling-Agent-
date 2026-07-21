from services.patient_service import is_new_patient

from models import (
    Doctor,
    DoctorCapability,
    BodyPart,
    IssueType,
    Slot
)

def get_body_part(name):
    return BodyPart.query.filter_by(
        name=name
    ).first()

def get_issue_type(name):
    return IssueType.query.filter_by(
        name=name
    ).first()

def find_matching_doctors(body_part_name, issue_type_name):
    body_part = get_body_part(body_part_name)

    issue_type = get_issue_type(issue_type_name)

    if body_part is None or issue_type is None:
        return []

    capabilities = DoctorCapability.query.filter_by(body_part_id=body_part.id, issue_type_id=issue_type.id).all()
    
    return [
    capability.doctor
    for capability in capabilities
    ]   

def filter_new_patient_eligibility(
    doctors,
    is_new_patient
):
    if not is_new_patient:
        return doctors

    eligible_doctors = []

    for doctor in doctors:
        if doctor.accepting_new_patients:
            eligible_doctors.append(doctor)

    return eligible_doctors

def find_available_slots(doctor):
    slots = (
        Slot.query
        .filter_by(
            doctor_id=doctor.id,
            is_available=True
        )
        .order_by(
            Slot.start_time
        )
        .all()
    )

    return slots

def find_first_available_slot(
    doctors,
    preferred_time="Earliest Available"
):

    preferred_time = preferred_time.lower()

    for doctor in doctors:

        slots = (
            Slot.query
            .filter_by(
                doctor_id=doctor.id,
                is_available=True
            )
            .order_by(Slot.start_time)
            .all()
        )

        if not slots:
            continue

        # Earliest available
        if preferred_time == "earliest available":
            return slots[0]

        # Morning appointments
        if preferred_time == "morning":

            for slot in slots:
                if slot.start_time.hour < 12:
                    return slot

        # Afternoon appointments
        elif preferred_time == "afternoon":

            for slot in slots:
                if slot.start_time.hour >= 12:
                    return slot

        # If preference isn't recognized or no matching slot exists,
        # fall back to the earliest slot for this doctor.
        return slots[0]

    return None

def route_patient(
    patient,
    body_part_name,
    issue_type_name,
    preferred_time="Earliest Available"
):
    """
    Finds the best doctor and earliest available slot for a patient.

    Returns:
        {
            "success": True,
            "doctor": Doctor,
            "slot": Slot
        }

    or

        {
            "success": False,
            "reason": "<reason>"
        }
    """

    new_patient = is_new_patient(patient)

    doctors = find_matching_doctors(
        body_part_name,
        issue_type_name
    )

    if not doctors:
        return {
            "success": False,
            "reason": "No physicians treat this condition."
        }

    doctors = filter_new_patient_eligibility(
        doctors,
        new_patient
    )

    if not doctors:
        return {
            "success": False,
            "reason": "No physicians accepting new patients."
        }

    slot = find_first_available_slot(
    doctors,
    preferred_time
    )

    if slot is None:
        return {
            "success": False,
            "reason": "No available appointment slots."
        }

    return {
        "success": True,
        "doctor": slot.doctor,
        "slot": slot
    }