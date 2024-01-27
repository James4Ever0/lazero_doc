// ==UserScript==
// @name     Lazero Merge Script
// @version  1
// @grant    none
// @run-at   document-start
// ==/UserScript==

// what is the so-called format anyway?
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
// don't be a dick. if want to use mass scan, you shall get a bigger drive, or do it elsewhere.
console.log("LAZERO MERGE SCRIPT\n    -\n   |               ___  __  __\n  / \\  |    /|  /  ___ |   |  |\n \\  _\\ |__ / | /__ ___ |   |__|\n\nTo make everything\nexecutable, analyzable, controllable.");
// back again. doing random stuff here.
// not too goddamn bad?
// <heartbeat package>
// do it in WEBSOCKET.
// or other implementations. if found by anyone.
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
// no <body>. cannot copy.
// NO BODY! CANNOT COPY!
// consider using plugin or something else.
// either use document.write
// the HECK!
// advice: do it in extension, not a fucking script.
// google has asked me to pay the fucking bill.
// cannot run.
const copyToClipboard = str => {
    try {
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
    }
    catch (error) { console.log(error); }
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
            // not even running?
            async function Tutor() {
                // console.log("posting document data");
                // whatever. it is great.
                // broadcast first?
// do it when you hit the enter?
// use system level supervise.
                var json = [{ "LAZERO_HELPER_PROGRAM": uuid }];
                try { copyToClipboard(JSON.stringify(json)); } catch (e) { console.log(e); }
                // wrong at this place.
                var i0 = 0;
                var i1 = false
                for (i0 = 0; i0 < 3; i0++) {
                    try {
                        await sleep(2000);
                        var d = document.all;
                        var ki = d.length;
                        for (var i = 0; i < ki; i++) {
                            var p = d[i];
                            var j = { "innerHtml": p.innerHTML, "outerHTML": p.outerHTML };
                            json.push(j);
                            // should you try to test it?
                        }
                        //d=JSON.stringify(d);
                        copyToClipboard(JSON.stringify(json));
                        i1 = true;
                        break;
                    } catch (err) { console.log(err); json = [{ "LAZERO_HELPER_PROGRAM": uuid }]; }
                }
                if (!i1) {
                    json.push({ "err": "timeout" })
                    copyToClipboard(JSON.stringify(json));
                }
                // do it later?
                // or do it again?
                // not fucking working.
                // GM.setClipboard(JSON.stringify(json));
            };
            async function Functor() {
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
                                        const report = { "toString": std.toString(), "toSource": std.toSource(), "typeof": typeof(std) };
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
            };
            Tutor();
            Functor();
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
<<<<<<< HEAD
// never ever see clock ticking? huh?
// it is amazing that there is no intermediate process when the browser does that fucking selection.
// no wonder browser is another beast.
// WEB IDE... File Explorer...
=======
>>>>>>> b22c4b69b54236744c2e24f54e1ba97cfa2de9bb
