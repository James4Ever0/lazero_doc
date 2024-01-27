// run this under electron prefix?
console.log("from electron");
// it is running just fine. but how to hide it?
const { app,BrowserWindow } = require("electron");
function createWindow(){
const win = new BrowserWindow({ width: 800, height: 1500 ,show:true})
//const win = new BrowserWindow({ width: 800, height: 1500 ,show:false})
win.loadURL('https://github.com')

const contents = win.webContents
console.log(contents)
}
app.on('ready', createWindow);
// can we use nightmare here?
// can we import other packages?
// app is launched, but headless. great. Now check modules.
