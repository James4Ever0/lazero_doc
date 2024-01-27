var Highlight = require('highlighter')();
// var marked = require('marked');//just test.
// no module.
// var style =
// it even got brainfuck.
// it does have the output. but never render it to image. or you have to use chrome.
var fs = require('fs');
// //does this work?
// did not applied the style.
// it is getting altered by cnpm.
// var html = require('highlight-xml');
// var js = require('highlight-javascript');
// it is always about the <pre></pre>
// i can do it. i can let my computer to shredder.
var data = fs.readFileSync('scipy.html', 'utf8'); // it works.
// var data = fs.readFileSync('./fix_x_torch.py', 'utf8');
var a = Highlight(data, "html");// does this work?
console.log('<html><head><link rel="stylesheet" type="text/css" href="androidstudio.css" ></head><body><pre><code>' + a + "</code></pre></body></html>");
// it got shit for every shit.
// what about other languages?
// var highlight = new Highlight()
//   .use(html)
//   .use(js);
// html=data
// // var el = document.querySelector('.code-sample');
// // highlight.element(el);
// highlight.all();
// console.log(html);
// this is not a package.
// i have to admit javascript has some advantages here.
// and it just fucking works.
// we always got a lot of fucks.
// broken code, and more.
// the guesslang might be good but we need to have conda or something that can switch to cuda.
// nvm. move forward.
// is my disk getting slow? that could be serious problem.
// chrome is not working.
// fuck it. it sucks.