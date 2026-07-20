from datetime import datetime, timedelta

from app import app
from database import db

from models import (
    BodyPart,
    IssueType,
    Location,
    Doctor,
    DoctorLocation,
    DoctorCapability,
    Slot
)

from seed.seed_data import (
    BODY_PARTS,
    ISSUE_TYPES,
    LOCATIONS,
    DOCTORS
)

print("Seed script started")

def seed_database():

    with app.app_context():

        db.drop_all()
        db.create_all()

        # Seed body parts
        for name in BODY_PARTS:
            db.session.add(
                BodyPart(name=name)
            )

        # Seed issue types
        for name in ISSUE_TYPES:
            db.session.add(
                IssueType(name=name)
            )

        # Seed locations
        for location in LOCATIONS:
            db.session.add(
                Location(
                    code=location["code"],
                    name=location["name"]
                )
            )

        db.session.commit()

        body_parts = {
            bp.name: bp
            for bp in BodyPart.query.all()
        }

        issue_types = {
            issue.name: issue
            for issue in IssueType.query.all()
        }

        locations = {
            location.code: location
            for location in Location.query.all()
        }
        
        for doctor_data in DOCTORS:
            doctor = Doctor(
                name=doctor_data["name"],
                accepting_new_patients=doctor_data["accepting_new"]
            )

            db.session.add(doctor)

            # Assign an ID immediately without committing
            db.session.flush()

            # Add doctor locations
            for location_code in doctor_data["locations"]:

                doctor_location = DoctorLocation(
                    doctor_id=doctor.id,
                    location_id=locations[location_code].id
                )

                db.session.add(doctor_location)
            
            # Add routing capabilities
            for body_part_name, issue_type_name in doctor_data["capabilities"]:

                capability = DoctorCapability(
                    doctor_id=doctor.id,
                    body_part_id=body_parts[body_part_name].id,
                    issue_type_id=issue_types[issue_type_name].id
                )

                db.session.add(capability)
            
            # Generate appointment slots
            start_date = datetime.now().replace(
                hour=9,
                minute=0,
                second=0,
                microsecond=0
            )

            # Doctor may work at multiple locations
            doctor_location_ids = [
                locations[code].id
                for code in doctor_data["locations"]
            ]

            slot_hours = [9, 10, 11, 13, 14]

            for day in range(5):

                for i, hour in enumerate(slot_hours):

                    start_time = (
                        start_date + timedelta(days=day)
                    ).replace(hour=hour)

                    end_time = start_time + timedelta(minutes=30)

                    # Alternate locations if doctor has more than one
                    location_id = doctor_location_ids[
                        i % len(doctor_location_ids)
                    ]

                    slot = Slot(
                        doctor_id=doctor.id,
                        location_id=location_id,
                        start_time=start_time,
                        end_time=end_time,
                        is_available=True
                    )

                    db.session.add(slot)
        db.session.commit()

        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()