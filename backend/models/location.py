from database import db


class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)

    code = db.Column(db.String(10), unique=True, nullable=False)

    name = db.Column(db.String(100), nullable=False)

    doctors = db.relationship(
        "DoctorLocation",
        back_populates="location",
        cascade="all, delete-orphan"
    )

    slots = db.relationship(
        "Slot",
        back_populates="location"
    )

    def __repr__(self):
        return f"<Location {self.code}>"