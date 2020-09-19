'use strict'

var mongoose = require('mongoose');
mongoose.set('useFindAndModify', false);
var professorModel = mongoose.model('Professor');
var researchGroupModel = mongoose.model('ResearchGroup');

exports.list_all_professors = function (req, res){
    const keys = Object.keys(req.query);
    const values = Object.values(req.query);
    var designations = ['Professor','Associate Professor','Assistant Professor'];
    var profs = [];
    if (keys[0] == 'designation') {
        if (designations.includes(values[0])){
            professorModel.find({designation: values[0]}, function(err, professors){
                if (err) {
                    res.status(404).json({message: 'Invalid professor\'s designation'});
                }
                for (var prof in professors) {
                    profs.push({name: professors[prof]['name'],email: professors[prof]['email']});
                }
                res.status(200).json(profs);
            });
        } else {
            res.status(200).json({message: 'No professors with such designation.'});
        }
    }
    else if (keys[0] == 'groupName'){
        researchGroupModel.find({name: values[0]}, function (err, groups){
            if (err) {
                res.status(404).json({message: 'Invalid group\'s name'});
            }
            if (Object.keys(groups).length != 0){
                var group_id = groups[0]['_id']
                professorModel.find({researchGroups: group_id}, function (err, professors){
                    if (err) {
                        res.status(404).json({message: 'Invalid group\'s ID'});
                    }
                    for (var prof in professors) {
                        profs.push({name: professors[prof]['name'],email: professors[prof]['email'],designation: professors[prof]['designation']});
                    }
                    res.status(200).json(profs);
                });
            }else {
                res.status(200).json({message: 'No groups with such name.'}); 
            }
            
        });
    }
    else {
        professorModel.find({}, function(err, professors) {
            if (err) {
                res.status(404).send(err);
            }
            for (var prof in professors) {
                profs.push({name: professors[prof]['name'],email: professors[prof]['email'],designation: professors[prof]['designation']});
            }
            res.status(200).json(profs);
        });
    }
};

exports.add_professor = function (req, res){
    var new_prof = new professorModel(req.body);
    new_prof.save(
        function(err, professor) {
            if (err) {
                res.status(404).send(err);
            }
            else {
                res.status(201).json({message: 'Professor successfully created', id: professor['_id']});
            }
        });
};

exports.read_a_professor = function (req, res){
    professorModel.findById(req.params.professorID, function (err, professor){
        if (err) {
            res.status(404).json({message: 'Invalid professor\'s ID'});
        }
        res.status(200).json({name: professor['name'],email: professor['email'],designation: professor['designation'],interests: professor['interests']});
    });
};


exports.update_a_professor = function (req, res) {
    professorModel.findOneAndUpdate({_id: req.params.professorID}, req.body, {new: true}, function (err, professor){
        if (err) {
            res.status(404).json({message: 'Invalid professor\'s ID'});
        }
        res.status(200).json({message: 'Professor successfully updated',id: professor['_id']});
    });
};

exports.delete_a_professor = function (req, res) {
    professorModel.findOneAndRemove({_id: req.params.professorID}, function (err, professor){
        if (err){
            res.status(404).json({message: 'Invalid professor\'s ID'});
        }
        researchGroupModel.remove({founder: req.params.professorID}).exec();
        res.status(200).json({message: 'Professor successfully deleted',id: req.params.professorID});
    });
};

