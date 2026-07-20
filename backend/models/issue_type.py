from database import db


class IssueType(db.Model):
    __tablename__ = "issue_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"<IssueType {self.name}>"