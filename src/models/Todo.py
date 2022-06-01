from . import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(255))
    done = db.Column(db.Boolean)

    def __init__(self, title, description, done):
        self.title = title
        self.description = description
        self.done = done

    def __repr__(self):
        return '<Todo %r>' % self.title
print(db)
    