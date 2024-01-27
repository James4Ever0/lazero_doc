// #!/usr/bin/nodejs
var http=require('http');
// var crypto = require('crypto');
// the heck.
// it would be hard if browsing the fucking thing.
// i mean PDF.
// and still don't know how to get it right.
// but we can do this, by remote access.
// the shell! yeah!
// var crypto = require('crypto'); 
// I HATE ALL FUCKING BROWSERS.
// check if there are multi-clipboard implementations on ANDROID, WINDOWS and LINUX.
// also the goddamn MACOS.
// time to do your own fucking browser, huh?
// able to operate on its own???
// huh?? -> window manager -> x server -> console automation
function uuidv4(){
    var dt = new Date().getTime();
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (dt + Math.random()*16)%16 | 0;
        dt = Math.floor(dt/16);
        return (c=='x' ? r :(r&0x3|0x8)).toString(16);
    });
    return uuid;
}
// function uuidv4() {
//     return ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, c =>
//         (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
//     );
// }
// man the heck is running.
// say either get it from clipboard or from web.
// return it via web or clipboard.
var server = http.createServer((function (request, response) {// never read the request?
    response.writeHead(200,
        { "Content-Type": "text/plain" });
    var k = uuidv4();
    // you should invoke another program.
    // maybe? maybe not.
    response.end(k);
}));
server.listen(7000);