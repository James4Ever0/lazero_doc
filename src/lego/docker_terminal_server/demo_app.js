// run this under electron prefix?
// will it continue to run?

// it is running just fine. but how to hide it?
// might be good representative for browser server.
const { app,BrowserWindow } = require("electron");
function createWindow(){
const win = new BrowserWindow({show:true})
//const win = new BrowserWindow({ width: 800, height: 1500 ,show:true})
//const win = new BrowserWindow({ width: 800, height: 1500 ,show:false})
win.loadURL('http://localhost:9997')
const contents = win.webContents
var http = require('http');
var url = require('url');
//logger=require('html-differ/lib/logger')
//this is too slow.
var prev=null
    var server = http.createServer ( function(request,response){

    response.writeHead(200,{"Content-Type":"text/plain"});
    if(request.method == "GET")
        {
		var resp = "";
		console.log(request.url);
		var u = url.parse(request.url,true);
 if (u.pathname=="/display"){

	 //var search = u.search;
	 //console.log(search);
	 contents.executeJavaScript('document.getElementsByTagName("html")[0].outerHTML', true)
  .then((result) => {
    resp+=result // Will be the JSON object from the fetch call
	  //  may cause connection close. how do you restart the whole thing?
	  //  refresh?
 response.writeHead(200, {'Content-Type': 'text/html'}) 
            response.end(resp)
  })
//	 resp+=win.webContents.innerHTML;
	 }else if(u.pathname=="/input") {
//		 console.log(u)
		 // execute the command here.
		 // no other commands?
		 var udtype = u.query.type
		 var ustype = u.query.b64type
		 var uktype = u.query.autoreturn
		 if( typeof(udtype) === "string" ){
//		 var utype = udtype.toUpperCase()
		 for (var i in udtype){contents.sendInputEvent({"type":"char","keyCode":udtype[i]})}
			 if (uktype == "true"){contents.sendInputEvent({"type":"char",keyCode:"\n"})}
			 contents.executeJavaScript('document.getElementsByTagName("html")[0].outerHTML', true)
  .then((result) => {
    resp+=result // Will be the JSON object from the fetch call
 response.writeHead(200, {'Content-Type': 'text/html'}) 
            response.end(resp)
  }) }else if (typeof(ustype) === "string" ){
let buff = Buffer.from(ustype,'base64')
	  let text = buff.toString("utf-8")
		 for (var i in text){contents.sendInputEvent({"type":"char","keyCode":text[i]})}
			 if (uktype == "true"){contents.sendInputEvent({"type":"char",keyCode:"\n"})}
			 contents.executeJavaScript('document.getElementsByTagName("html")[0].outerHTML', true)
  .then((result) => {
    resp+=result // Will be the JSON object from the fetch call
 response.writeHead(200, {'Content-Type': 'text/html'}) 
            response.end(resp)})
  } else {
			 contents.executeJavaScript('document.getElementsByTagName("html")[0].outerHTML', true)
  .then((result) => {
    resp+=result // Will be the JSON object from the fetch call
 response.writeHead(200, {'Content-Type': 'text/html'}) 
            response.end(resp)})
  }
	 }
		else{
			response.writeHead(200, {'Content-Type': 'text/html'}) 
            response.end(resp)
		}
	// Get the path
		// there's no option for restart.
		// no watchdog, neither superdog.
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
//contents.sendInputEvent(inputEvent)
/*
const contents = win.webContents
//console.log(console.dir(contents))
contents.executeJavaScript('document.getElementsByTagName("html")[0].outerHTML', true)
  .then((result) => {
    console.log(result) // Will be the JSON object from the fetch call
  })
  */
}
app.on('ready', createWindow);
// can we use nightmare here?
// can we import other packages?
// app is launched, but headless. great. Now check modules.
