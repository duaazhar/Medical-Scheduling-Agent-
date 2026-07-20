from database import db


class BodyPart(db.Model):
    __tablename__ = "body_parts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"<BodyPart {self.name}>"