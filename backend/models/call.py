from datetime import datetime

from database import db


class Call(db.Model):
    __tablename__ = "calls"

    id = db.Column(db.Integer, primary_key=True)

    patient_id = db.Column(
        db.Integer,
        db.ForeignKey("patients.id"),
        nullable=False
    )

    appointment_id = db.Column(
        db.Integer,
        db.ForeignKey("appointments.id"),
        nullable=True
    )

    caller_phone = db.Column(
        db.String(20),
        nullable=False
    )

    status = db.Column(
        db.String(20),
        nullable=False
    )

    transcript = db.Column(
        db.Text,
        nullable=True
    )

    started_at = db.Column(
        db.DateTime,
        nullable=False
    )

    ended_at = db.Column(
        db.DateTime,
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    # Relationships
    patient = db.relationship(
        "Patient",
        back_populates="calls"
    )

    appointment = db.relationship(
        "Appointment",
        back_populates="calls"
    )

    def __repr__(self):
        return (
            f"<Call {self.id} "
            f"Status={self.status}>"
        )