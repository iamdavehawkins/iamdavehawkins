'''
Script to initialize data in the PartTypes table

@author: iamdavehawkins
'''

from app import db
from app.models import *

# delete all rows from the table and start the auto increment at 1
def pop_parttypes():
	PartType.query.delete()
	db.engine.execute("ALTER SEQUENCE parttypes_id_seq RESTART WITH 1;")

	bb = PartType(name="Bottom Bracket")
	db.session.add(bb)

	bars = PartType(name="Handlebars")
	db.session.add(bars)

	tape = PartType(name="Bar Tape")
	db.session.add(tape)

	brake_levers = PartType(name="Brake Levers", min_per_bike=0, max_per_bike=4)
	db.session.add(brake_levers)

	shifters = PartType(name="Shifters", min_per_bike=0, max_per_bike=2)
	db.session.add(shifters)

	brifters = PartType(name="Brifters", min_per_bike=0, max_per_bike=2)
	db.session.add(brifters)

	stem = PartType(name="Stem")
	db.session.add(stem)

	fork = PartType(name="Fork")
	db.session.add(fork)

	front_wheel = PartType(name="Front Wheel")
	db.session.add(front_wheel)

	rear_wheel = PartType(name="Rear Wheel")
	db.session.add(rear_wheel)

	seatpost = PartType(name="Seatpost")
	db.session.add(seatpost)

	saddle = PartType(name="Saddle")
	db.session.add(saddle)

	crankset = PartType(name="Crankset")
	db.session.add(crankset)

	pedals = PartType(name="Pedals", min_per_bike=2, max_per_bike=2)
	db.session.add(pedals)

	brakes = PartType(name="Brakes", min_per_bike=0, max_per_bike=2)
	db.session.add(brakes)

	chain = PartType(name="Chain")
	db.session.add(chain)

	front_derailleur = PartType(name="Front Derailleur", min_per_bike=0)
	db.session.add(front_derailleur)

	rear_derailleur = PartType(name="Rear Derailleur", min_per_bike=0)
	db.session.add(rear_derailleur)

	cassette = PartType(name="Cassette")
	db.session.add(cassette)

	db.session.commit()

if __name__ == "__main__":
	pop_parttypes()
