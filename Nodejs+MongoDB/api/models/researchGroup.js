'use strict';
var mongoose = require('mongoose');
var schema = mongoose.Schema;

var researchGroupSchema = new schema ({
    name: {
        type: String,
        required: true,
        unique: true,
        dropDups: true
    },
    description: {
        type: String
    },
    founder: {
        type: schema.Types.ObjectId,
        ref: 'Professor'
    }
});

module.exports = mongoose.model('ResearchGroup', researchGroupSchema);