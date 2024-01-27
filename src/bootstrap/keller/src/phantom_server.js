var page = require('webpage').create();
  //viewportSize being the actual size of the headless browser
  page.viewportSize = { width: 1024, height: 768 };
  //the clipRect is the portion of the page you are taking a screenshot of
  page.clipRect = { top: 0, left: 0, width: 1024, height: 768 };
  //the rest of the code is the same as the previous example
  page.open('https://www.baidu.com/', function() {
//    page.render('github.png')
var base64 = page.renderBase64('PNG');
	  // full of error.
  console.log(base64);
var http = new XMLHttpRequest();
	  http.open("POST", "http://localhost:7777/phantom_render", true);
//	  http.setRequestHeader("Content-type","application/png");
	  http.send(base64);
	  //  string. can be other things. make a post request. fetch.
	  /*var data= new FormData();
	  data.append("screenshot",data)*/
	  /*fetch("http://localhost:7777/phantom_render",{
		  method:"POST",
		  body:base64
	  });*/
	  // send it into other things.
//    phantom.exit();
	  //    don't you quit.
  });
// this one is called the webkit.
// no websecurity.
