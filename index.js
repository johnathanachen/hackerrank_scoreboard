var express = require('express');
var path = require('path');
var bodyParser = require('body-parser');
var app = express();
var mongoose = require('mongoose');
var exphbs = require('express-handlebars');

app.use(express.static(__dirname + '/public'));
app.engine('handlebars', exphbs({defaultLayout: 'main'}));
app.set('view engine', 'handlebars');

mongoose.connect('mongodb://localhost/scoreboard');

var rank = mongoose.model('rank',{
	usr_name: String,
	points: { type: Number, index: true },
	date_added:  { type: Date, default: Date.now }
});

app.get('/',function (req, res) {
   	res.render('scoreboard');
});

/* IF the rank is greather than the other ranks calculate the diffrence between the points and move in the y direction that many spaces
 *
 */

app.listen(3000);
