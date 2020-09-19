'use strict';
var groupQuery = function(app) {
    var groupController = require('../controllers/researchGroupController');
    
    app.route('/listGroups')
        .get(groupController.list_all_groups)

    app.route('/listGroup')
        .post(groupController.add_group);

    app.route('/listGroup/:groupID')
        .get(groupController.read_a_group)
        .put(groupController.update_a_group)
        .delete(groupController.delete_a_group);
};

module.exports = groupQuery;