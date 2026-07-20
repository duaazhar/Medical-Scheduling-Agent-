from database import db


class DoctorCapability(db.Model):
    __tablename__ = "doctor_capabilities"

    id = db.Column(db.Integer, primary_key=True)

    doctor_id = db.Column(
        db.Integer,
        db.ForeignKey("doctors.id"),
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
    doctor = db.relationship(
        "Doctor",
        back_populates="capabilities"
    )

    body_part = db.relationship(
        "BodyPart"
    )

    issue_type = db.relationship(
        "IssueType"
    )

    # Prevent duplicate routing rules
    __table_args__ = (
        db.UniqueConstraint(
            "doctor_id",
            "body_part_id",
            "issue_type_id",
            name="unique_doctor_capability"
        ),
    )

    def __repr__(self):
        return (
            f"<DoctorCapability("
            f"{self.doctor.name}, "
            f"{self.body_part.name}, "
            f"{self.issue_type.name})>"
        )