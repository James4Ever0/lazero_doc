var http = require('http');
var url = require('url');
//logger=require('html-differ/lib/logger')
//this is too slow.
var prev=null
    var server = http.createServer ( function(request,response){

    response.writeHead(200,{"Content-Type":"text/plain"});
    if(request.method == "GET")
        {
		console.log(request.url);
		var u = url.parse(request.url,true);
 if (u.pathname=="/random"){var search = u.search;
	 console.log(search);}
	// Get the path
	/*var p = u.pathname;
		console.log(u);
		console.log(p);*/
		//what?
	/*var body=[]
		request.on('data', function(data) {
      body.push(data)
      console.log('GET Partial body: ' , data)
    })
    request.on('end', function() {
	    var concatBody=Buffer.concat(body)
	    var next=concatBody.toString('utf-8')
      console.log('GET Body End:',next.length)

      response.writeHead(200, {'Content-Type': 'text/html'})
 
            response.end("received GET request.")
    })*/
		//parse query string?
 response.writeHead(200, {'Content-Type': 'text/html'}) 
            response.end("received GET request.")
 
	}
    else if(request.method == "POST")
        {//console.log(request.data);
		var body=[]
		request.on('data', function(data) {
      body.push(data)
      console.log('Partial body: ' , data)
    })
    request.on('end', function() {
	    var concatBody=Buffer.concat(body)
	    var next=concatBody.toString('utf-8')
      console.log('Body End:',next.length)

      response.writeHead(200, {'Content-Type': 'text/html'})
      response.end('post received')
    })
        }
    else
        {
            response.end("Undefined request .");
        }
});
//arbitrary path.
server.listen(7777);
console.log("Server running on port 7777");
