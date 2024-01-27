chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        if (request.msg === "something_completed") {
            //  To do something
            // document.write
            // not even conplete.
            // use the chrome.tabs -> firefox.tab?
            console.log(request.data.subject)
            console.log(request.data.content)
        }
    }
);