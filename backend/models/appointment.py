from datetime import datetime

from database import db


class Appointment(db.Model):
    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key=True)

    patient_id = db.Column(
        db.Integer,
        db.ForeignKey("patients.id"),
        nullable=False
    )

    doctor_id = db.Column(
        db.Integer,
        db.ForeignKey("doctors.id"),
        nullable=False
    )

    slot_id = db.Column(
        db.Integer,
        db.ForeignKey("slots.id"),
        nullable=False,
        unique=True
    )

    status = db.Column(
        db.String(20),
        nullable=False,
        default="Scheduled"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    body_part_id = db.Column(
        db.Integer,
        db.ForeignKey("body_parts.id"),
        nullable=False
    )

    issue_type_id = db.Column(
        db.Integer,
        db.ForeignKey("issue_types.id"),
        nullable=False
    )

    # Relationships
    patient = db.relationship(
        "Patient",
        back_populates="appointments"
    )

    doctor = db.relationship(
        "Doctor",
        back_populates="appointments"
    )

    slot = db.relationship(
        "Slot",
        back_populates="appointment"
    )

    calls = db.relationship(
        "Call",
        back_populates="appointment"
    )

    body_part = db.relationship(
    "BodyPart"
    )   

    issue_type = db.relationship(
        "IssueType"
    )


    def __repr__(self):
        return (
            f"<Appointment("
            f"Patient={self.patient.first_name} {self.patient.last_name}, "
            f"Doctor={self.doctor.name}, "
            f"BodyPart={self.body_part.name}, "
            f"Issue={self.issue_type.name})>"
        )