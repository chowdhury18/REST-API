## https://dev.to/paurakhsharma/flask-rest-api-part-0-setup-basic-crud-api-4650
from flask import Flask, jsonify, request, Response
from database.db import initialize_db
from database.models import Course
import json
from bson.objectid import ObjectId
import os
from flask_cors import CORS
from mongoengine.errors import ValidationError, NotUniqueError
from datetime import datetime

app = Flask(__name__)
CORS(app)

# database config
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/openapi-db'
}
db = initialize_db(app)

# route
@app.route('/')
def get_route():
    output = jsonify({'message': 'It looks like you are trying to access FlaskAPP over HTTP on the native driver port.'})
    #output.headers.add('Access-Control-Allow-Origin', '*')
    return output, 200
    
@app.route('/course', methods=['POST'])
def add_course():
    status_code = None
    try:
        body = request.get_json()
        course = Course(**body).save()
        course_id = course.id
        course_code = course.code
        course_name = course.name
        course_type = course.course_type
        course_semester = course.semester
        output = {'message': 'Course successfully created', 'id': str(course_id)}
        #output = {'id': str(course_id), 'code': str(course_code), 'name': str(course_name), 'type': str(course_type), 'semester': str(course_semester)}
        status_code = 201
    except ValidationError as err:
        output = {"message": str(err)}
        status_code = 500
    except NotUniqueError as err:
        output = {"message": str(err)}
        status_code = 500
    return output, status_code


@app.route('/course/<course_id>', methods=['GET','PUT','DELETE'])
def get_course_by_id(course_id):
    status_code = None
    if request.method == 'GET':
        try:
            course = json.loads(Course.objects().get_or_404(id=course_id).to_json())
            output = {'id': str(course['_id']['$oid']),'code': str(course['code']),'name': str(course['name']),'course_type': str(course['course_type']),'semester': str(course['semester']),'starting_date': str(datetime.utcfromtimestamp(course['starting_date']['$date']/1000.0).strftime('%Y-%m-%d %H:%M:%S')), 'ending_date': str(datetime.utcfromtimestamp(course['ending_date']['$date']/1000.0).strftime('%Y-%m-%d %H:%M:%S'))}
            return output, 200
        except:
            output = {"message": "Invalid course ID."}
            return output, 404
    elif request.method == 'PUT':
        try:
            body = request.get_json()
            Course.objects(id=course_id).update(**body)
            course = json.loads(Course.objects().get_or_404(id=course_id).to_json())
            output = {'message': 'Course successfully updated', 'id': str(course_id)}
            status_code = 200
        except ValidationError as err:
            output = {"message": str(err)}
            status_code = 500
        except NotUniqueError as err:
            output = {"message": str(err)}
            status_code = 500
        return output, status_code
    elif request.method == 'DELETE':
        try:
            Course.objects(id=course_id).delete()
            output = {'message': 'Course successfully deleted', 'id': str(course_id)}
            status_code = 204
        except:
            output = {"message": "Invalid course ID."}
            status_code = 404
        return output, status_code

@app.route('/courses', methods=['GET'])
def get_courses_by_params():
    status_code = None
    keys = [key for key in request.args.keys()]
    if keys:
        if keys[0] == 'course_type':
            value = request.args.get(keys[0])
            if value:
                courses = json.loads(Course.objects(course_type=value).to_json())
                if courses:
                    output = jsonify([{'code': str(c['code']), 'name': str(c['name']), 'semester': str(c['semester']), 'starting_date': str(datetime.utcfromtimestamp(c['starting_date']['$date']/1000.0).strftime('%Y-%m-%d %H:%M:%S')), 'ending_date': str(datetime.utcfromtimestamp(c['ending_date']['$date']/1000.0).strftime('%Y-%m-%d %H:%M:%S'))} for c in courses])
                    status_code = 200
                else:
                    output = {'message': 'Invalid course type.'}
                    status_code = 404
            else:
                output = {'message': 'Params value empty.'}
                status_code = 404
        elif keys[0] == 'semester':
            value = request.args.get(keys[0])
            if value:
                courses = json.loads(Course.objects(semester=value).to_json())
                if courses:
                    output = jsonify([{'code': str(c['code']), 'name': str(c['name']), 'course_type': str(c['course_type']), 'starting_date': str(datetime.utcfromtimestamp(c['starting_date']['$date']/1000.0).strftime('%Y-%m-%d %H:%M:%S')), 'ending_date': str(datetime.utcfromtimestamp(c['ending_date']['$date']/1000.0).strftime('%Y-%m-%d %H:%M:%S'))} for c in courses])
                    status_code = 200
                else:
                    output = {'message': 'Invalid semester.'}
                    status_code = 404
            else:
                output = {'message': 'Params value empty.'}
                status_code = 404
        else:
            output = {'message': 'Incorrect search key'}
            status_code = 404
    else:
        output = {"message":"No params found."}
        status_code = 404

    return output, status_code