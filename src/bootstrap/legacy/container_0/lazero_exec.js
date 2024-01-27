// ==UserScript==
// @name     Lazero Exec Demo
// @version  1
// @grant    none
// @run-at   document-start
// ==/UserScript==

// check on that require thing.
// does not share the same uuid.
// thus not official implementation.
// disable another script first.
// use that script instead?
// get the uuid somehow.
// it is gonna slow you down.
// do me a favor: online clipboard.
// please. this is for good.
// that function is not right.
// or not?
// do it in another platform.
// maybe?
// fucking absent.
// finally?
// whatever.
// do the clipboard manager then.
// try-catch in js?
function deselect() {
    if (window.getSelection) { window.getSelection().removeAllRanges(); }
    else if (document.selection) { document.selection.empty(); }
}
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
// not gonna restore the original state.
// so you'd better write a plugin instead.
// firefox and chrome.
// come on.
// you should clone the termux thing.
// do the terminal emulator thing!
// terminal emulator -> file expolrer -> browser ...
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// that sleep function is fucked.
// this is not really the case.
// also not good at all when doing this.


const Http = new XMLHttpRequest();
const url = 'http://localhost:7000';
Http.open("GET", url);
Http.send();

// making it portable?
// can't wait for the long duration.
// before the document is ready, that script won't run.
// you probably need to visit another site over and over again.
var uuid = null;
// eventually replace all kinds of shit.
Http.onreadystatechange = (e) => {
    var xk = Http.responseText;
    // just parse it.
    if (!uuid) {
        if (xk) {
            console.log("Session UUID: " + xk);
            uuid = xk;
            var command = null;
            async function Tutor() {
                // document.write('Hello Toturix');
                while (true) {
                    await sleep(1000);
                    const Httpx = new XMLHttpRequest();
                    const urlx = 'http://localhost:7001';
                    Httpx.open("GET", urlx);
                    Httpx.send();
                    Httpx.onreadystatechange = (f) => {
                        var kx = Httpx.responseText;
                        if (kx) {
                            if (!(command == kx)) {
                                // console.log(kx);
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
                    }
                }
            }
            Tutor();
            // do not execute the same shit again.
            // and you still want to broadcast it via clipboard?
            // with cp command there's no need for clipboard.
            // will it be problematic?
            // javascript does not have blocking issues?
            // the thing is not running at all.
            // THE THING IS NOR REALLY RUNNING!
            // while (true) {
                // can do solo scanning with that tool.
            //     // no there is error inside.
            //     sleep(2000).then(() => {
            //         var e = getClipboardContent();
            //         console.log("exec spliter");
            //         console.log(e);
            //     });
            // monitor, operate, and so on.
            // sleep(2000);
            // not working.
        }
    }
}
// the code to reply:
// .toString();
// .toSource();
// maybe some type???
// typeof(a);
// how do we get the automatic completion?
// so we complie pieces of code outside the project, seeing what will happen.