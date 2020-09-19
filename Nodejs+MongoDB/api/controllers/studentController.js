'use strict'

var mongoose = require('mongoose');
mongoose.set('useFindAndModify', false);
var professorModel = mongoose.model('Professor');
var researchGroupModel = mongoose.model('ResearchGroup');
var studentModel = mongoose.model('Student');

exports.list_all_students = function (req, res){
    const keys = Object.keys(req.query);
    const values = Object.values(req.query);
    var stds = [];
    if (keys[0] == 'groupName'){
        researchGroupModel.find({name: values[0]}, function (err, groups){
            if (err) {
                res.status(404).json({message: 'Invalid group\'s name'});
            }
            if (Object.keys(groups).length != 0){
                var group_id = groups[0]['_id']
                studentModel.find({researchGroups: group_id}, function(err, students){
                    if (err) {
                        res.status(404).json({message: 'Invalid group\'s ID'});
                    }
                    for (var std in students) {
                        stds.push({name: students[std]['name'],studentNumber: students[std]['studentNumber']});
                    }
                    res.status(200).json(stds);
                });
            }else {
                res.status(200).json({message: 'No groups with such name.'}); 
            }
            
        });
    } else {
        studentModel.find({}, function(err, students) {
            if (err) {
                res.send(err);
            }
            if (students) {
                for (var std in students) {
                    stds.push({name: students[std]['name'],studentNumber: students[std]['studentNumber']});
                }
                if (stds.length == 0){
                    res.status(200).json({message: "No student enrolled"});
                }
                res.status(200).json(stds);
            }
        });
    }
};

exports.add_student = function (req, res){
    var new_student = new studentModel(req.body);
    new_student.save(
        function(err, student) {
            if (err) {
                res.status(404).send(err);
            }
            res.status(201).json({message: 'Student successfully created', id: student['_id']});
        });
};

exports.read_a_student = function (req, res){
    studentModel.findById(req.params.studentID, function (err, student){
        if (err) {
            res.status(404).json({message: 'Invalid student\'s ID'});
        }
        res.status(200).json({name: student['name'],studentNumber: student['studentNumber'],researchGroups: student['researchGroups']});
    });
};

exports.update_a_student = function (req, res) {
    studentModel.findOneAndUpdate({_id: req.params.studentID}, req.body, {new: true}, function (err, student){
        if (err) {
            res.status(404).json({message: 'Invalid student\'s ID'});
        }
        res.status(200).json({message: 'Student successfully updated',id: student['_id']});
    });
};

exports.delete_a_student = function (req, res) {
    studentModel.findOneAndRemove({_id: req.params.studentID}, function (err, student){
        if (err){
            res.status(404).json({message: 'Invalid student\'s ID'});
        }
        res.status(200).json({message: 'Student successfully deleted',id: req.params.studentID});
    });
};

