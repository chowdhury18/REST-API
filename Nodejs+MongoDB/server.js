var express = require('express');
var app = express();
var port = process.env.PORT || 3000;
var mongoose = require('mongoose');
var professorModel = require('./api/models/professor');
var groupModel = require('./api/models/researchGroup'); 
var studentModel = require('./api/models/student');
var bodyParser = require('body-parser');

var connURL = "mongodb://localhost/db";
//var connURL = "mongodb://mongo:27017/mongo-db";
const options = {
    useNewUrlParser: true, 
    useUnifiedTopology: true, 
    useCreateIndex: true
};

const connectWithRetry = () => {
    console.log('MongoDB connection with retry')
    mongoose.connect(connURL, options).then(()=>{
      console.log('MongoDB is connected')
    }).catch(err=>{
      console.log('MongoDB connection unsuccessful, retry after 5 seconds.');
      setTimeout(connectWithRetry, 3000);
    });
}

connectWithRetry();
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
mongoose.Promise = global.Promise;
//mongoose.connect('mongodb://mongo:27017/db',{useNewUrlParser: true, useUnifiedTopology: true, 'useCreateIndex': true});

app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

var professorRoutes = require('./api/routes/professorRoutes');
var groupRoutes = require('./api/routes/researchGroupRoutes');
var studentRoutes = require('./api/routes/studentRoutes');
professorRoutes(app);
groupRoutes(app);
studentRoutes(app);

app.listen(port);

console.log('APP started... on port: ' + port);