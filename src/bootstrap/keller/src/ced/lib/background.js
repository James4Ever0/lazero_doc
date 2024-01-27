function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
async function asf() {
    while (true) {
        await sleep(1000);
        // console.log("happy newYear");
        // sending things.
        // what the heck?
        // chrome.runtime.sendMessage({
        //     msg: "something_completed",
        //     data: {
        //         subject: "Loading",
        //         content: "Just completed!"
        //     }
        // });
        // the same. so chrome is ahead of everything??
        console.log("this is background page.");
        var tb=chrome.tabs;
        console.log(tb);
        // chrome.runtime.sendMessage({data:"something"},function(response){});
    }
}
asf();
// do it now.
/*
var getting = chrome.cookies.getAll()
console.log(getting)*/
// halt this.
// structure matters. sequence matters.
// does this matters? when switching instances. -> maybe.
// can you do some extra things? copy things into the clipboard?
