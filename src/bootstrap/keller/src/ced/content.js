// // listen for checkForWord request, call getTags which includes callback to sendResponse.
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));}
console.log("LAZERO PLUGIN\n    -\n   |               ___  __  __\n  / \\  |    /|  /  ___ |   |  |\n \\  _\\ |__ / | /__ ___ |   |__|\n\nTo make everything\nexecutable, analyzable, controllable.");
// do not do it twice.
async function dfunc(){
while(true){await sleep(500);
try { document.body.style.border = "5px solid red"; break}
catch (e) { console.log(e); }}}
dfunc();
// chrome.runtime.onMessage.addListener(
//   function (request, sender, sendResponse) {
//     if (request.action === 'checkForWord') {
//       checkForWord(request, sender, sendResponse);
//       // this is required to use sendResponse asynchronously
//       return true;
//     }
//   }
// );
// think about it.
// not able to run on super slow websites.
// for unofficial chrome kernel, we can install with .crx
// // Returns the index of the first instance of the desired word on the page.
// // send what?
// // hardware-level -> bios-level -> system-level -> browser-level
// function checkForWord(request, sender, sendResponse) {
//   var scripts = document.getElementsByTagName('script');
//   for (var i = 0; i < scripts.length; i++) {
//     if (scripts[i].src.toLowerCase().indexOf('jquery') > -1) {
//       return sendResponse({ results: i + 1 });
//     }
//   }
//   return sendResponse({ results: 0 });
// }
// fucking hell. there's no need to see anyone.