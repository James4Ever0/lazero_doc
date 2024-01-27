// #!/usr/bin/nodejs
// undefined
// var 
var http=require('http');
// var crypto = require('crypto');
// the heck.
// it would be hard if browsing the fucking thing.
// i mean PDF.
// cannot be done. document.body is null.
// skip all errors?
// and still don't know how to get it right.
// but we can do this, by remote access.
// the shell! yeah!
// var crypto = require('crypto'); 
// return it via web or clipboard.
// whatever.
var demo="7bba4519-f413-4975-b0b6-8ebf98b5ccdf";
// you can set the command, without using mouse at all.
// without taking risk there's no meaning at all.
var server = http.createServer((function (request, response) {// never read the request?
    response.writeHead(200,
        { "Content-Type": "text/plain" });
    // var k = uuidv4();
    var k = {"uuid":demo,"command":"document.all"};
    // you should invoke another program.
    // better print it out.
    // not responding.
    // what the heck?
    // or put it into the clipboard.
    // maybe? maybe not.
    response.end(JSON.stringify(k));
    // JSON.parse(k);
    // get it parsed, or report error.
}));
server.listen(7001);