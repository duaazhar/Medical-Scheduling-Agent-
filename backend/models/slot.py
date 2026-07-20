from datetime import datetime

from database import db


class Slot(db.Model):
    __tablename__ = "slots"

    id = db.Column(db.Integer, primary_key=True)

    doctor_id = db.Column(
        db.Integer,
        db.ForeignKey("doctors.id"),
        nullable=False
    )

    location_id = db.Column(
        db.Integer,
        db.ForeignKey("locations.id"),
        nullable=False
    )

    start_time = db.Column(
        db.DateTime,
        nullable=False
    )

    end_time = db.Column(
        db.DateTime,
        nullable=False
    )

    is_available = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    # Relationships
    doctor = db.relationship(
        "Doctor",
        back_populates="slots"
    )

    location = db.relationship(
        "Location",
        back_populates="slots"
    )

    appointment = db.relationship(
        "Appointment",
        back_populates="slot",
        uselist=False
    )

    def __repr__(self):
        return (
            f"<Slot "
            f"{self.start_time} "
            f"Doctor={self.doctor_id}>"
        )