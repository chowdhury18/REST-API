'use strict'

var mongoose = require('mongoose');
mongoose.set('useFindAndModify', false);
var professorModel = mongoose.model('Professor');
var researchGroupModel = mongoose.model('ResearchGroup');
var studentModel = mongoose.model('Student');

exports.list_all_groups = function (req, res){
    var grps = [];
    researchGroupModel.find({}, function(err, groups) {
        if (err) {
            res.status(404).send(err);
        }
        for (var grp in groups) {
            grps.push({name: groups[grp]['name'],founder: groups[grp]['founder']});
        }
        res.status(200).json(grps);
    });
};

exports.add_group = function (req, res){
    var new_group = new researchGroupModel({_id: new mongoose.Types.ObjectId(), name: req.body.name, description: req.body.description});
    var founderID = req.body.founder;
    professorModel.findOneAndUpdate(
        {_id: founderID},
        {$addToSet: {researchGroups: new_group._id}},
        function (err, professor){
            if (err) {
                res.status(404).json({message: 'Invalid professor\'s ID'});
            }
            else {
                new_group.founder = founderID;
                new_group.save(function( err, group){
                    if (err){
                        res.status(404).send(err);
                    }
                    res.status(201).json({message: 'Group successfully created',id: group['_id']});
                });
            }
        });
};

exports.read_a_group = function (req, res){
    researchGroupModel.findById(req.params.groupID, function (err, group){
        if (err) {
            res.status(404).json({message: 'Invalid group\'s ID'});
        }
        res.status(200).json({id: group._id,name: group.name,founder: group.founder});
    });
};

exports.update_a_group = function (req, res) {
    researchGroupModel.findOneAndUpdate({_id: req.params.groupID}, req.body, {new: true}, function (err, group){
        if (err) {
            res.status(404).json({message: 'Invalid group\'s ID'});
        }
        res.status(200).json({message: 'Group successfully updated',id: group['_id']});
    });
};

exports.delete_a_group = function (req, res) {
    researchGroupModel.findOneAndRemove({_id: req.params.groupID}, function (err, group){
        if (err){
            res.status(404).json({message: 'Invalid group\'s ID'});
        }
        var groupid = req.params.groupID;
        professorModel.updateMany(
            {researchGroups: groupid},
            {$pull: {researchGroups: groupid}}
        ).exec();
        studentModel.updateMany(
            {researchGroups: groupid},
            {$pull: {researchGroups: groupid}}
        ).exec();
        /*
        professorModel.find({researchGroups: groupid}, function (err, professors){
            if (err) {
                res.status(404).json({message: 'Invalid group\'s ID'});
            }
            if (professors){
                for (var prof in professors) {
                    professorModel.findOneAndUpdate(
                        {_id: professors[prof]['_id']},
                        {$pull: {'researchGroups': groupid}}
                    );
                }
            } else{
                res.status(404).json({message: 'No professors are in the group.'});
            }           
        });*/
        res.status(200).json({message: 'Group successfully deleted',id: req.params.groupID});
    });
};

