from app import db

class Bike(db.Model):

    __tablename__ = 'bikes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    weight = db.Column(db.Float)

    def __repr__(self):
        return '<Bike {}>'.format(self.name)