//use nodejs this time.
const Nightmare = require('nightmare')
//const nightmare = Nightmare({ show: true,switches:{'ignore-certificate-errors': true}})
// shit. nightmare won't run on linux.
// too few?
// must be string array.
const nightmare = Nightmare({cli_args:["--no-sandbox"],show:false});
//const nightmare = Nightmare({width:1000,height:1000,switches: {"sandbox":false},show:true});
// not running.
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

nightmare.goto('https://www.baidu.com').evaluate(() => {return document.title;}).end().then((title) => {console.log(title);})

async function santa(){await sleep(10);}
santa();
// all fucked up.
