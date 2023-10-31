var http = require('http');

var userCount = 0;

var server = http.createServer(function (req, res) {

    userCount++;

    res.writeHead(200, { 'Content-Type': 'text/html' });

    res.write('<h1>Hello!</h1>\n');

    res.write('We have had ' + userCount + ' visits!\n');
    res.end();

 

});

server.listen(3000);

console.log('server running...')