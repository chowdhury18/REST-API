'use strict';
var mongoose = require('mongoose');
var schema = mongoose.Schema;

var studentSchema = new schema({
    name: {
        type: String,
        required: true
    },
    studentNumber: {
        type: String,
        required: true
    },
    researchGroups: [{
        type: schema.Types.ObjectId,
        ref: 'ResearchGroup'
    }]
});

module.exports = mongoose.model('Student',studentSchema);