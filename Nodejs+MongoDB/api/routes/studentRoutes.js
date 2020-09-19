'use strict';
var studentQuery = function(app) {
    var studentController = require('../controllers/studentController');
    
    app.route('/listStudents')
        .get(studentController.list_all_students)

    app.route('/listStudent')
        .post(studentController.add_student);

    app.route('/listStudent/:studentID')
        .get(studentController.read_a_student)
        .put(studentController.update_a_student)
        .delete(studentController.delete_a_student);
};

module.exports = studentQuery;