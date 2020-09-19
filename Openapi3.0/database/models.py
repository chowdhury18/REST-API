from .db import db
import datetime

class Course(db.Document):
    c_type = {
        'compulsory': 'compulsory',
        'optional': 'optional'
    }
    c_semester = {
        'autumn': 'autumn',
        'spring': 'spring'  
    }
    code = db.StringField(max_length=20,required=True, unique=True)
    name = db.StringField(max_length=30,required=True, unique=True)
    description = db.StringField(max_length=50)
    course_type = db.StringField(choices=c_type.keys(),default="compulsory",required=True)
    semester = db.StringField(choices=c_semester.keys(),default="autumn",required=True)
    starting_date = db.DateTimeField(required=True, default=datetime.datetime.utcnow)
    ending_date = db.DateTimeField(required=True, default=datetime.datetime.utcnow)


