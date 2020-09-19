from .db import db

class Professor(db.Document):
    role = {'Professor': 'Professor',
         'Assistant Professor': 'Assistant Professor',
         'Associate Professor': 'Associate Professor'
         }
    name = db.StringField(max_length=20,required=True, unique=True)
    designation = db.StringField(choices=role.keys(),default="Professor",required=True)
    email = db.StringField(max_length=30,unique=True)
    interests = db.ListField(db.StringField())
    researchGroups = db.ListField(db.ReferenceField('ResearchGroup'))

class ResearchGroup(db.Document):
    name = db.StringField(max_length=20,required=True, unique=True)
    founder = db.ReferenceField(Professor,required=True,dbref=False)
    description = db.StringField(max_length=100)

class Student(db.Document):
    name = db.StringField(max_length=20,required=True, unique=True)
    studentNumber = db.StringField(max_length=20,required=True, unique=True)
    researchGroups = db.ListField(db.ReferenceField(ResearchGroup))
