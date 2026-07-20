from app import app
from database import db
from models import Appointment

with app.app_context():

    Appointment.query.delete()

    db.session.commit()

    print("Appointments cleared.")