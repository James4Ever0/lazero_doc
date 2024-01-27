const jsdom = require ("jsdom");
const html = `<!doctype html>
  <html>
    <head>
      <link rel="stylesheet" href="xterm.css" />
    </head>
    <body>
      <div id="terminal" width="500px" height="500px"></div>
    </body>
  </html>`;
const { JSDOM } = jsdom;
const dom = new JSDOM (html,{runScripts:"dangerously",resources:"usable"});
window = dom.window;
window.matchMedia=window.matchMedia || function (){
	return {
		matches:false,
		addListener :function (){},
		removeListener : function (){}
	};
};
if (!window.requestAnimationFrame){
	let targetTime =0;
	window.requestAnimationFrame = function(c){
		const currentTime= +new Date();
		const timeoutCb= function(){c(+new Date())}
		return window.setTimeout(timeoutCb,Math.max(targetTime +16, currentTime) - currentTime)
	}
}
requestAnimationFrame = window.requestAnimationFrame;
document = window.document;
//document.outerHTML=html;
/* Keep source code the same */
var xterm = require("xterm");
var term = new xterm.Terminal({
	convertEol:true,
	fontFamily:`'Droid Sans Mono', monospace`,
	fontSize:15,
	rendererType:'dom',
});
//term.open(document.getElementById('terminal'));
//var elem=document.getElementById('terminal');
//console.log(elem);
term.open(document.getElementById('terminal'));
//console.log(term.element);
//console.log(term.element.parentElement);
//term.fit();
term.write('Hello from \x1B[1;3;31mxterm.js\x1B[0m $ ');
//DOES THIS WORKS?
console.log(term.element.innerHTML);
