from database import db


class TodoRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    status = db.Column(db.String(30))
    description = db.Column(db.String(1000))
    created = db.Column(db.DateTime)
    last_edited = db.Column(db.DateTime)
    due_to = db.Column(db.DateTime)