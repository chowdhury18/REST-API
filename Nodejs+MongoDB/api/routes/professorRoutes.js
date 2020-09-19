'use strict';
var professorQuery = function(app) {
    var professorController = require('../controllers/professorController');
    
    app.route('/listProfessors')
        .get(professorController.list_all_professors)

    app.route('/listProfessor')
        .post(professorController.add_professor);

    app.route('/listProfessor/:professorID')
        .get(professorController.read_a_professor)
        .put(professorController.update_a_professor)
        .delete(professorController.delete_a_professor);
};

module.exports = professorQuery;