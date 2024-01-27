// ==UserScript==
// @name     Lazero Merge Script
// @version  1
// @grant    none
// @run-at   document-start
// ==/UserScript==

// everytime having a different value.
// create a cronjob then.
// on copy command, you get the idea of it.
// or register a service.
//  so this time we only use clipboard, or something alike?
// what do you expect? on_clipboard_change?
// uuid can be used here.
// might be useful.
// some pages such as extension config are not accessiblt.
// yes you can monitor it by yourself.
// but anyway, it is getting close to the truth.
// wait till fully loaded?
console.log("LAZERO MERGE SCRIPT\n    -\n   |               ___  __  __\n  / \\  |    /|  /  ___ |   |  |\n \\  _\\ |__ / | /__ ___ |   |__|\n\nTo make everything\nexecutable, analyzable, controllable.");
// back again. doing random stuff here.
// not too goddamn bad?
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}// fucking absent.
function deselect() {
    if (window.getSelection) { window.getSelection().removeAllRanges(); }
    else if (document.selection) { document.selection.empty(); }
}
// even set imagedata?
// better get a inputbox.
// not called inside a event handler.
// which is weird.
// so we will do this when the document is ready!
// or not?
// do it in another platform.
// maybe?
const copyToClipboard = str => {
    const el = document.createElement('textarea');  // Create a <textarea> element
    el.value = str;                                 // Set its value to the string that you want copied
    el.setAttribute('readonly', '');                // Make it readonly to be tamper-proof
    el.style.position = 'absolute';
    el.style.left = '-9999px';                      // Move outside the screen to make it invisible
    document.body.appendChild(el);
    // Append the <textarea> element to the HTML document
    const selected =
        document.getSelection().rangeCount > 0        // Check if there is any content selected previously
            ? document.getSelection().getRangeAt(0)     // Store selection if found
            : false;                                    // Mark as false to know no selection existed before
    // do not check the selection.
    // do not store the fucking selection.
    // only if you want to.
    deselect();
    el.select();                                    // Select the <textarea> content
    document.execCommand('copy');                   // Copy - only works as a result of a user action (e.g. click events)
    document.body.removeChild(el);                  // Remove the <textarea> element
    if (selected) {                                 // If a selection existed before copying
        document.getSelection().removeAllRanges();    // Unselect everything on the HTML document
        document.getSelection().addRange(selected);   // Restore the original selection
    }
};
var uuid = null;
const Http = new XMLHttpRequest();
const url = 'http://localhost:7000';
Http.open("GET", url);
Http.send();

// making it portable?
Http.onreadystatechange = (e) => {
    var xk = Http.responseText;
    // doing it twice?
    if (!uuid) {
        if (xk) {
            console.log("Session UUID: " + xk);
            uuid = xk;
            var command = null;
            async function Tutor() {
                // console.log("posting document data");
                // whatever. it is great.
                await sleep(2000);
                var d = document.all;
                var ki = d.length;
                var json = [{ "LAZERO_HELPER_PROGRAM": uuid }];
                for (var i = 0; i < ki; i++) {
                    var p = d[i];
                    var j = { "innerHtml": p.innerHTML, "outerHTML": p.outerHTML };
                    json.push(j);
                }
                //d=JSON.stringify(d);
                copyToClipboard(JSON.stringify(json));
                // and that is really fast.
                // must use a strong clipboard manager.
                // either as a server or as system service.
                while (true) {
                    await sleep(1000);
                    const Httpx = new XMLHttpRequest();
                    const urlx = 'http://localhost:7001';
                    Httpx.open("GET", urlx);
                    Httpx.send();
                    Httpx.onreadystatechange = (f) => {
                        var kx = Httpx.responseText;
                        if (kx) {
                            // console.log("here");
                            if (!(command == kx)) {
                                // console.log(kx);
                                // console.log("there");
                                // no fucking command.
                                command = kx
                                // then consider run the command.
                                // is that stucked?
                                // just use the buffer program or something?
                                try {
                                    const json_eval = JSON.parse(kx);
                                    const cmd = json_eval["command"];
                                    const uid = json_eval["uuid"];
                                    if (uid == uuid) {
                                        const std = eval(cmd);
                                        var repo = [{ "LAZERO_EVAL_PROGRAM": uuid, "command": cmd }];
                                        const report = { "toString": std.toString(), "toSource": std.toSource(), "typeof": typeof (std) };
                                        repo.push(report);
                                        const cpy = JSON.stringify(repo);
                                        // console.log(cpy);
                                        copyToClipboard(cpy);
                                        console.log("new request completed: " + Date.now());
                                    }

                                } catch (err) { console.error(err); }

                            }
                        }
                        // console.log("testing connection: "+Date.now());
                    }
                }
                // do it later?
                // or do it again?
                // not fucking working.
                // GM.setClipboard(JSON.stringify(json));
            };
            Tutor();
        }
    }
}
// what is that anyway?
// if request failed?
// without network card?
// that implementation is about the ADD-ON.
// AGAIN. DEVELOPING EXTENSIONS.

// you can simply post the first one please???
// don't be silly.
// we shall also have access to the clipboard somehow.
// check notation?
// get uuid?