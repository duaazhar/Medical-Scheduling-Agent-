from flask import Blueprint
from flask import jsonify
from flask import render_template

from models import (
    Patient,
    Appointment,
    Call,
    Slot
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