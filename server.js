let PusherPlatform = require('./pusher-platform');
var express = require('express')
var app = express()
var fs = require('fs') // this engine requires the fs module

app.engine('ntl', function (filePath, options, callback) { // define the template engine
  fs.readFile(filePath, function (err, content) {
    if (err) return callback(err)
    // this is an extremely simple template engine
    var rendered = content.toString().replace('#title#', '<title>' + options.title + '</title>')
    .replace('#message#', '<h1>' + options.message + '</h1>')
    return callback(null, rendered)
  })
})
app.set('views', './views') // specify the views directory
app.set('view engine', 'ntl') // register the template engine

app.get('/', function (req, res) {
  let appID = new PusherPlatform.App({
    appId: '',
  });

  var myFeed = appID.feed('playground');

  // myFeed.append('Hello, world!')
  //   .then(response => console.log('Success:', response))
  //   .catch(err => console.error('Error:', err));

  // You’re not limited to appending string values;
  // you can also append objects, arrays and numbers.
  // myFeed.append({ yourKey: 'your value' })
  //   .then(response => console.log('Success:', response))
  //   .catch(err => console.error('Error:', err));

  res.render('index', { title: 'Hey', message: 'Hello there!' })
})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})
