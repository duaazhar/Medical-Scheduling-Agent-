from datetime import datetime

from database import db


class Patient(db.Model):
    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(
        db.String(50),
        nullable=False
    )

    last_name = db.Column(
        db.String(50),
        nullable=False
    )

    phone_number = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    date_of_birth = db.Column(
        db.Date,
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    # Relationships
    appointments = db.relationship(
        "Appointment",
        back_populates="patient",
        cascade="all, delete-orphan"
    )

    calls = db.relationship(
        "Call",
        back_populates="patient",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return (
            f"<Patient "
            f"{self.first_name} "
            f"{self.last_name}>"
        )