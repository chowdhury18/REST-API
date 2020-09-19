'use strict';
var mongoose = require('mongoose');
var schema = mongoose.Schema;

var professorSchema = new schema ({
    name: {
        type: String,
        required: true
    },
    designation: {
        type: String,
        enum: ['Professor','Associate Professor','Assistant Professor'],
        default: 'Professor',
        required: true
    },
    email: {
        type: String
    },
    interests: [{
        type: String
    }],
    researchGroups: [{
        type: schema.Types.ObjectId,
        ref: 'ResearchGroup'
    }]   
});

module.exports = mongoose.model('Professor', professorSchema);