from database import db


class Doctor(db.Model):
    __tablename__ = "doctors"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    accepting_new_patients = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    # Relationships
    locations = db.relationship(
        "DoctorLocation",
        back_populates="doctor",
        cascade="all, delete-orphan"
    )

    capabilities = db.relationship(
        "DoctorCapability",
        back_populates="doctor",
        cascade="all, delete-orphan"
    )

    slots = db.relationship(
        "Slot",
        back_populates="doctor",
        cascade="all, delete-orphan"
    )

    appointments = db.relationship(
        "Appointment",
        back_populates="doctor"
    )

    def __repr__(self):
        return f"<Doctor {self.name}>"