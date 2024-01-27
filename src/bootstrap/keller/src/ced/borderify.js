/*
Just draw a border round the document.body.
*/

// yes. man. ahead of shit.
// console.log("");
// add all fucking permissions here!
// this shit is executable somehow?
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

/**
 * inits a websocket by a given url, returned promise resolves with initialized websocket, rejects after failure/timeout.
 *
 * @param url the websocket url to init
 * @param existingWebsocket if passed and this passed websocket is already open, this existingWebsocket is resolved, no additional websocket is opened
 * @param timeoutMs the timeout in milliseconds for opening the websocket
 * @param numberOfRetries the number of times initializing the socket should be retried, if not specified or 0, no retries are made
 *        and a failure/timeout causes rejection of the returned promise
 * @return {Promise}
 */
function initWebsocket(url, existingWebsocket, timeoutMs, numberOfRetries) {
    timeoutMs = timeoutMs ? timeoutMs : 1500;
    numberOfRetries = numberOfRetries ? numberOfRetries : 0;
    var hasReturned = false;
    var promise = new Promise((resolve, reject) => {
        setTimeout(function () {
            if(!hasReturned) {
                console.info('opening websocket timed out: ' + url);
                rejectInternal();
            }
        }, timeoutMs);
        if (!existingWebsocket || existingWebsocket.readyState != existingWebsocket.OPEN) {
            if (existingWebsocket) {
                existingWebsocket.close();
            }
            var websocket = new WebSocket(url);
            websocket.onopen = function () {
                if(hasReturned) {
                    websocket.close();
                } else {
                    console.info('websocket to opened! url: ' + url);
                    resolve(websocket);
                }
            };
            websocket.onclose = function () {
                console.info('websocket closed! url: ' + url);
                rejectInternal();
            };
            websocket.onerror = function () {
                console.info('websocket error! url: ' + url);
                rejectInternal();
            };
        } else {
            resolve(existingWebsocket);
        }

        function rejectInternal() {
            if(numberOfRetries <= 0) {
                reject();
            } else if(!hasReturned) {
                hasReturned = true;
                console.info('retrying connection to websocket! url: ' + url + ', remaining retries: ' + (numberOfRetries-1));
                initWebsocket(url, null, timeoutMs, numberOfRetries-1).then(resolve, reject);
            }
        }
    });
    promise.then(function () {hasReturned = true;}, function () {hasReturned = true;});
    return promise;
};
// do not do it twice.
async function dfunc() {
    while (true) {
        await sleep(500);
        // no fucking border.
        try { document.body.style.border = "5px solid red"; break }
        catch (e) { console.log(e); }
    }
}

console.log("LAZERO PLUGIN\n    -\n   |               ___  __  __\n  / \\  |    /|  /  ___ |   |  |\n \\  _\\ |__ / | /__ ___ |   |__|\n\nTo make everything\nexecutable, analyzable, controllable.");
dfunc();
// it is async.
async function func() {
    while (true) {
        await sleep(1000);
        // no fucking border.
        try { fetch("https://localhost:5000/nothing",{credentials:'include'}).then(function(response){console.log(response)}).catch(function(ex){console.log("Exception: ",ex)}) }
        catch (e) { console.log(e); }
    }
}
func();
var socket_0;
async function sfunc(init){
	await sleep(init);
while (true){
	try{
		//socket = new WebSocket("wss://localhost:5000/random");
initWebsocket("wss://localhost:5000/random",null,3000,0).then(function (socket){
socket_0=socket;
var timerId = 0;
	console.log("ws init succeed");
function keepAlive(webSocket) {
 var timeout = 15000;
 if (webSocket.readyState == webSocket.OPEN) {
  webSocket.send('');
 }
 timerId = setTimeout(keepAlive(webSocket), timeout);
}
function cancelKeepAlive() {
 if (timerId) {
  cancelTimeout(timerId);
 }
}
socket.onopen = function(e) {
	keepAlive(socket_0);
  console.log("[open] Connection established");
  console.log("Sending to server");
  socket.send("My name is John");
};
// what is this anyway?
socket.onmessage = function(event) {
	var edata = event.data;
  console.log(`[message] Data received from server: `)
	  console.log(edata,typeof(edata),edata.includes("baidu"));
	if (typeof(edata)===typeof("string")){
		if (edata.includes("https://")){
			var random="fetch failed";
			fetch(edata,{method:"GET",credentials:"include"}).then(function(resp){
				console.log("CONTENT: ",resp);
//				console.log("CONTENT: ",e.body);
				//	it is not with cookies.
//				const ebody=e.body.getReader();
				//get your fuck binary.
//				const ebody=resp.blob();
				resp.text().then(function(txt){try{
					console.log("CTEXT: ",txt.length);
				socket.send(txt);
				}catch(err){console.log("EMPTY RESPONSE:",err);
		socket.send(random);
					}},function(err){console.log("ERR PROMISE:",err);
		socket.send(random);
					})
				// what is that thing?
				// get the content please?
			}).catch(function(e){
				console.log("ERROR: ",e);
				socket.send(random);
			})
		}else{
  socket.send("NOT BAIDU URL");
  console.log("NOT BAIDU URL");
		}
	}else{
  socket.send("NOT STRING");
  console.log("NOT STRING");
	}
	// what data?
};

socket.onclose = function(event) {
	sfunc(3000);
  if (event.wasClean) {
    console.log(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
  } else {
    // e.g. server process killed or network down
    // event.code is usually 1006 in this case
	  // get uuid from elsewhere? check it logically.
    console.log('[close] Connection died');
  }
	cancelKeepAlive();
	// keep calling.
};

socket.onerror = function(error) {
	sfunc(3000);
  console.log(`[error] ${error.message}`);

}},function(){
sfunc(3000);
	console.log("ws init failed");
})
		// not usable? do it some time later?
await sleep(3000);
	break;		// wss://
	}catch(e){console.log(e);}
}
}
sfunc(0);
// how to dump the full shit?
// so there are three states.
// switch (document.readyState) {
//     case "loading":
//       // The document is still loading.
//       break;
//     case "interactive":
//       // The document has finished loading. We can now access the DOM elements.
//       // But sub-resources such as images, stylesheets and frames are still loading.
//       var span = document.createElement("span");
//       span.textContent = "A <span> element.";
//       document.body.appendChild(span);
//       break;
//     case "complete":
//       // The page is fully loaded.
//       console.log("The first CSS rule is: " + document.styleSheets[0].cssRules[0].cssText);
//       break;
//   }
// onreadystatechange, readystate.
// crap man.
// do the chrome extension? get out and see?
// configure the run-time.
// hey! we do not have the same font.
// // is it HTML?
// "*://*",
// "http://*",
// "https://*",
// "ws://*",
// "wss://*",
// "ftp://*",
// "ftps://*",
// "data://*",
// "file://*",
// must either: must either [must either [be one of ["clipboardRead", "clipboardWrite", "geolocation", "idle", "notifications"], be one of ["bookmarks"], be one of ["find"], be one of ["history"], be one of ["menus.overrideContext"], be one of ["search"], be one of ["activeTab", "tabs", "tabHide"], be one of ["browserSettings"], be one of ["cookies"], be one of ["downloads", "downloads.open"], be one of ["topSites"], be one of ["webNavigation"], or be one of ["webRequest", "webRequestBlocking"]], be one of ["alarms", "mozillaAddons", "storage", "unlimitedStorage"], be one of ["browsingData"], be one of ["captivePortal"], be one of ["devtools"], be one of ["identity"], be one of ["menus", "contextMenus"], be one of ["pkcs11"], be one of ["geckoProfiler"], be one of ["sessions"], be one of ["contextualIdentities"], be one of ["dns"], be one of ["management"], be one of ["privacy"], be one of ["proxy"], be one of ["nativeMessaging"], be one of ["telemetry"], be one of ["theme"], or match the pattern /^experiments(\.\w+)+$/], or must either [be one of ["<all_urls>"], must either [match the pattern /^(https?|wss?|file|ftp|\*):\/\/(\*|\*\.[^*/]+|[^*/]+)\/.*$/, or match the pattern /^file:\/\/\/.*$/], or match the pattern /^resource:\/\/(\*|\*\.[^*/]+|[^*/]+)\/.*$|^about:/]
// this is specific to FIREFOX.
