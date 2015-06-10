from app import db

# use Flask-Uploads to return filename where uploaded images are stored

class Bike(db.Model):
	'''
	The bikes that I have or have had in time
	along with all the parts currently installed
	Also retired bikes can continue to show
	'''

	__tablename__ = 'bikes'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String())
	weight = db.Column(db.Float)
	img_path = db.Column(db.String())
	retired = db.Column(db.Integer)

	parts = db.relationship('MyPart')

	def __repr__(self):
		return '<Bike {}>'.format(self.name)


class PartType(db.Model):
	'''
	Defines a list of valid bike parts and the min/max that can go
	on one bike.
	'''

	__tablename__ = 'parttypes'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String())
	min_per_bike = db.Column(db.Integer)
	max_per_bike = db.Column(db.Integer)

	my_parts = db.relationship('MyPart')

	def __init__(self, name, min_per_bike=1, max_per_bike=1):
		self.name = name
		self.min_per_bike = min_per_bike
		self.max_per_bike = max_per_bike

	def __repr__(self):
		return '<PartType {}, Max: {}>'.format(self.name, self.max_per_bike)


class MyPart(db.Model):
	'''
	These are the parts that I actually have at home
	as well as which bike (or none) they are currently
	installed on.
	'''

	__tablename__ = 'myparts'
	id = db.Column(db.Integer, primary_key=True)
	brand = db.Column(db.String())
	name = db.Column(db.String())
	price = db.Column(db.Float)
	weight_g = db.Column(db.Float)
	color = db.Column(db.String())
	img_path = db.Column(db.String())
	retired = db.Column(db.Integer)

	bike_id = db.Column(db.Integer, db.ForeignKey('bikes.id'))
	parttype_id = db.Column(db.Integer, db.ForeignKey('parttypes.id'))

	def __repr__(self):
		return '<Part {} {} is a {} installed on {}>'.format(
			self.brand, self.name, self.parttype_id, self.bike_id)

def pop_parttypes():
	bb = PartType(name="Bottom Bracket", min_per_bike=1, max_per_bike=1)
	db.session.add(bb)
	db.session.commit()