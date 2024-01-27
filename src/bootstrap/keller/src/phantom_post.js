const base64="hello world";
var http = new XMLHttpRequest();
http.open("POST", "http://localhost:7777/phantom_render", true);
//	  http.setRequestHeader("Content-type","application/png");
http.send(base64);
// can you get return value? we need the return.
	  //  string. can be other things. make a post request. fetch.
	  /*var data= new FormData();
	  data.append("screenshot",data)*/
	  /*fetch("http://localhost:7777/phantom_render",{
		  method:"POST",
		  body:base64
	  });*/
	  // send it into other things.
// this one is called the webkit.
// no websecurity.
var spawn = require("child_process").spawn
var execFile = require("child_process").execFile
// not getting shit from this.

var child = spawn("curl", ["http://localhost:7777/random"])

child.stdout.on("data", function (data) {
  console.log("spawnSTDOUT: ");
	console.log(data);
	// no multi-arg log support.
})

child.stderr.on("data", function (data) {
  console.log("spawnSTDERR: ");
	console.log(data);
})

child.on("exit", function (code) {
  console.log("spawnEXIT: ")
	console.log(code);
})
// but no returning.
//child.kill("SIGKILL")
// all fucked up.
/*execFile("curl", ["-v","http://localhost:7777/phantomjs"], null, function (err, stdout, stderr) {
  console.log("execFileSTDOUT:");
	console.log(typeof(stdout));
  console.log("execFileSTDERR:");
		console.log(typeof(stderr));
})*/
/*
setTimeout(function () {
  phantom.exit(0)
}, 2000)*/
