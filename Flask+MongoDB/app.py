 
from flask import Flask, jsonify, request, Response
from database.db import initialize_db
from database.models import Professor, ResearchGroup, Student
import json
from bson.objectid import ObjectId
import os

app = Flask(__name__)

# database config
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/flask-db'
    # 'host':'mongodb://mongo:27017/flask-db' # when the app is run as a service using docker-compose
}
db = initialize_db(app)


# get all professors
@app.route('/listProfessors', methods=['GET'])
def get_all_professors():
    keys = [key for key in request.args.keys()]
    if keys:
        if keys[0] == 'designation':
            value = request.args.get(keys[0])
            if value:
                professors = Professor.objects(designation=value).to_json()
                all_prof = json.loads(professors)
                if all_prof:
                    output = [{'name': str(p['name']), 'email': str(p['email']), 'designation': str(p['designation'])} for p in all_prof]
                    return jsonify(output), 200
                else:
                    output = {'message': 'Invalid designation'}
                    return output, 200
            else:
                output = {'message': 'Params value empty'}
                return output, 200

        elif keys[0] == 'groupName':
            value = request.args.get(keys[0])
            if value:
                groups = ResearchGroup.objects(name=value)
                if groups:
                    group_id = [group.id for group in groups]
                    professors = Professor.objects(researchGroups=group_id[0]).to_json()
                    all_prof = json.loads(professors)
                    output = [{'name': str(p['name']), 'email': str(p['email']), 'designation': str(p['designation'])} for p in all_prof]
                    return jsonify(output), 200
                else:
                    output = {'message': 'Invalid groupName'}
                    return output, 200
            else:
                output = {'message': 'Params value empty'}
                return output, 200
        else:
            output = {'message': 'Incorrect search key'}
            return output, 200
    else:
        professors = Professor.objects().to_json()
        all_prof = json.loads(professors)
        output = [{'name': str(p['name']), 'email': str(p['email']), 'designation': str(p['designation'])} for p in all_prof]
        return jsonify(output), 200


# get, update and delete professor by ID
@app.route('/listProfessor/<prof_id>', methods=['GET','PUT','DELETE'])
def get_professor_by_id(prof_id):
    if request.method == "GET":
        professor = json.loads(Professor.objects().get_or_404(id=prof_id).to_json())
        output = {'name': str(professor['name']), 'email': str(professor['email']), 'designation': str(professor['designation']), 'interests': professor['interests']}
        return jsonify(output), 200
    elif request.method == "PUT":
        body = request.get_json()
        keys = body.keys()
        if body and keys:
            if 'researchGroups' in keys:
                for group_id in body['researchGroups']:
                    Professor.objects(id=prof_id).update(push__researchGroups=ObjectId((group_id)))
            if 'name' in keys:
                Professor.objects(id=prof_id).update(set__name=body['name'])
            if 'designation' in keys:
                Professor.objects(id=prof_id).update(set__designation=body['designation'])
            if 'email' in keys:
                Professor.objects(id=prof_id).update(set__email=body['email'])
            if 'interests' in keys:
                for interest in body['interests']:
                    Professor.objects(id=prof_id).update(push__interests=interest)
            output = {'message': 'Professor successfully updated', 'id': str(prof_id)}
        else:
            output = {'message': 'Message body is empty'}
        return output, 200
    
    elif request.method == "DELETE":
        Professor.objects().get(id=prof_id).delete()
        groups = ResearchGroup.objects(founder=prof_id)
        if groups:
            group_ids = [group.id for group in groups]
            ResearchGroup.objects(founder=prof_id).delete()
            for gid in group_ids:
                Professor.objects(researchGroups=ObjectId(gid)).update(pull__researchGroups=ObjectId(gid))            
        output = {'message': 'Professor successfully deleted', 'id': str(prof_id)}
        return output, 200


# post professor
@app.route('/listProfessor', methods=['POST'])
def add_professor():
    body = request.get_json()
    professor = Professor(**body).save()
    prof_id = professor.id
    output = {'message': 'Professor successfully created', 'id': str(prof_id)}
    return output, 201


# get, update and delete group by ID
@app.route('/listGroup/<group_id>', methods=['GET','PUT','DELETE'])
def get_group_by_id(group_id):
    if request.method == "GET":
        group = json.loads(ResearchGroup.objects(id=group_id).get_or_404().to_json())
        output = {'id': str(group_id), 'name': str(group['name']), 'founder': str(group['founder']['$oid'])}
        return jsonify(output), 200
    elif request.method == "PUT":
        body = request.get_json()
        keys = body.keys()
        if body and keys:
            if 'name' in keys:
                ResearchGroup.objects(id=group_id).update(set__name=body['name'])
            if 'founder' in keys:
                prof_ids = [prof.id for prof in Professor.objects()]
                if ObjectId(body['founder']) in prof_ids:
                    ResearchGroup.objects(id=group_id).update(set__founder=ObjectId(body['founder']))
                    Professor.objects(id=body['founder']).update(push__researchGroups=ObjectId(group_id))
                else:
                    output = {'message':'Invalid founder ID'}
                    return output, 404
            if 'description' in keys:
                ResearchGroup.objects(id=group_id).update(set__description=body['description'])
            output = {'message': 'Group successfully updated', 'id': str(group_id)}
        else:
            output = {'message': 'Message body is empty'}
        return output, 200
    elif request.method == "DELETE":
        ResearchGroup.objects().get(id=group_id).delete()
        founder = Professor.objects(researchGroups=group_id)
        if founder:
            Professor.objects(researchGroups=group_id).update(pull__researchGroups=ObjectId(group_id))
        student = Student.objects(researchGroups=group_id)
        if student:
            Student.objects(researchGroups=group_id).update(pull__researchGroups=ObjectId(group_id))
        output = {'message': 'Group successfully deleted', 'id': str(group_id)}
        return output, 200

# post researchGroup
@app.route('/listGroup', methods=['POST'])
def add_group():
    body = request.get_json()
    founder = body['founder']
    group = ResearchGroup(**body).save()
    group_id = group.id
    Professor.objects(id=founder).update_one(push__researchGroups=group_id)
    output = {'message': 'Group successfully created', 'id': str(group_id)}
    return output, 201

# get all students
@app.route('/listStudents', methods=['GET'])
def get_all_student():
    keys = [key for key in request.args.keys()]
    if keys:
        if keys[0] == 'groupName':
            value = request.args.get(keys[0])
            if value:
                groups = ResearchGroup.objects(name=value)
                if groups:
                    group_id = [group.id for group in groups]
                    students = Student.objects(researchGroups=group_id[0]).to_json()
                    all_students = json.loads(students)
                    output = [{'name': str(p['name']), 'studentNumber': str(p['studentNumber'])} for p in all_students]
                    return jsonify(output), 200
                else:
                    output = {'message': 'Invalid groupName'}
                    return output, 200
            else:
                output = {'message': 'Params value empty'}
                return output, 200
        else:
            output = {'message': 'Incorrect search key'}
            return output, 200

# get, update and delete students
@app.route('/listStudent/<student_id>', methods=['GET','PUT','DELETE'])
def get_student_by_id(student_id):
    if request.method == "GET":
        student = json.loads(Student.objects().get_or_404(id=student_id).to_json())
        if student:
            group_ids = [group['$oid'] for group in student['researchGroups']]
            output = {'name': str(student['name']), 'studentNumber': str(student['studentNumber']), 'researchGroups': str(group_ids)}
        else:
            output = {'message': 'Invalid student ID'}
        return output, 200
    elif request.method == "PUT":
        body = request.get_json()
        keys = body.keys()
        if body and keys:
            if 'name' in keys:
                Student.objects(id=student_id).update(set__name=body['name'])
            if 'studentNumber' in keys:
                Student.objects(id=student_id).update(set__studentNumber=body['studentNumber'])
            if 'researchGroups' in keys:
                for group_id in body['researchGroups']:
                    Student.objects(id=student_id).update(push__researchGroups=ObjectId(group_id))
            output = {'message': 'Student successfully updated', 'id': str(student_id)}
        else:
            output = {'message': 'Message body empty'}
        return output, 200
    elif request.method == "DELETE":
        Student.objects.get_or_404(id=student_id).delete()
        output = {'message': 'Student successfully deleted', 'id': str(student_id)}
        return output, 200

# post student
@app.route('/listStudent', methods=['POST'])
def add_student():
    body = request.get_json()
    student = Student(**body).save()
    student_id = student.id
    output = {'message': 'Student successfully created', 'id': str(student_id)}
    return output, 201

#app.run() # FLASK_APP=app.py FLASK_ENV=development flask run