'''
Script to initialize data in the PartTypes table

@author: iamdavehawkins
'''

from app import db
from app.models import *

PartType.query.delete()

bb = PartType(name="Bottom Bracket", min_per_bike=1, max_per_bike=1)
db.session.add(bb)

bars = PartType(name="Handlebars", min_per_bike=1, max_per_bike=1)
db.session.add(bars)



db.session.commit()
