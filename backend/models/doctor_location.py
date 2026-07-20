from database import db


class DoctorLocation(db.Model):
    __tablename__ = "doctor_locations"

    doctor_id = db.Column(
        db.Integer,
        db.ForeignKey("doctors.id"),
        primary_key=True
    )

    location_id = db.Column(
        db.Integer,
        db.ForeignKey("locations.id"),
        primary_key=True
    )

    doctor = db.relationship(
        "Doctor",
        back_populates="locations"
    )

    location = db.relationship(
    "Location",
    back_populates="doctors"
    )