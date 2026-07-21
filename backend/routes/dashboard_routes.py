from flask import Blueprint
from flask import jsonify
from flask import render_template

from models import (
    Patient,
    Appointment,
    Call,
    Slot,
    Doctor 
)


dashboard_bp = Blueprint(
    "dashboard",
    __name__
)


@dashboard_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@dashboard_bp.route("/dashboard/stats")
def dashboard_stats():

    total_patients = Patient.query.count()

    total_appointments = Appointment.query.count()

    total_calls = Call.query.count()

    scheduled_calls = Call.query.filter_by(
        status="Scheduled"
    ).count()

    failed_calls = Call.query.filter_by(
        status="Failed"
    ).count()

    available_slots = Slot.query.filter_by(
        is_available=True
    ).count()

    booked_slots = Slot.query.filter_by(
        is_available=False
    ).count()

    return jsonify({

        "patients": total_patients,

        "appointments": total_appointments,

        "calls": total_calls,

        "scheduled_calls": scheduled_calls,

        "failed_calls": failed_calls,

        "available_slots": available_slots,

        "booked_slots": booked_slots

    })

@dashboard_bp.route("/dashboard/calls")
def dashboard_calls():

    calls = (
        Call.query
        .order_by(Call.started_at.desc())
        .all()
    )

    results = []

    for call in calls:

        appointment = call.appointment
        patient = call.patient

        doctor = None
        location = None

        if appointment:
            doctor = appointment.doctor.name
            location = appointment.slot.location.name

        results.append({

            "id": call.id,

            "patient": (
                f"{patient.first_name} {patient.last_name}"
            ),

            "phone_number": call.caller_phone,

            "status": call.status,

            "doctor": doctor,

            "location": location,

            "started_at": (
                call.started_at.strftime(
                    "%Y-%m-%d %H:%M"
                )
            ),

            "ended_at": (
                call.ended_at.strftime(
                    "%Y-%m-%d %H:%M"
                )
                if call.ended_at else ""
            ),

            "transcript": call.transcript or ""

        })

    return jsonify(results)

@dashboard_bp.route("/dashboard/doctors")
def dashboard_doctors():

    doctors = Doctor.query.order_by(Doctor.name).all()

    results = []

    for doctor in doctors:

        available_slots = (
            Slot.query.filter_by(
                doctor_id=doctor.id,
                is_available=True
            ).count()
        )

        # Remove duplicates
        body_parts = sorted({
            capability.body_part.name
            for capability in doctor.capabilities
        })

        issue_types = sorted({
            capability.issue_type.name
            for capability in doctor.capabilities
        })

        results.append({

            "doctor": doctor.name,

            "accepting_new_patients":
                doctor.accepting_new_patients,

            "available_slots": available_slots,

            "body_parts": body_parts,

            "issue_types": issue_types

        })

    return jsonify(results)

@dashboard_bp.route("/dashboard/appointments")
def dashboard_appointments():

    appointments = (
        Appointment.query
        .join(Slot)
        .order_by(Slot.start_time)
        .all()
    )

    results = []

    for appointment in appointments:

        patient = appointment.patient
        doctor = appointment.doctor
        slot = appointment.slot

        results.append({

            "appointment_id": appointment.id,

            "patient": (
                f"{patient.first_name} {patient.last_name}"
            ),

            "doctor": doctor.name,

            "location": slot.location.name,

            "body_part": appointment.body_part.name,

            "issue_type": appointment.issue_type.name,

            "date": slot.start_time.strftime("%Y-%m-%d"),

            "time": slot.start_time.strftime("%I:%M %p"),

            "status": appointment.status

        })

    return jsonify(results)