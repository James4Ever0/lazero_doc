#!/usr/bin/env node
// it is linked here. so do another thing, magic patch.
var electron = require('./')

var proc = require('child_process')
var patch =  process.argv.slice(2)
patch.unshift("--no-sandbox");
//patch.prepend("--no-sandbox")
//console.log(patch,typeof(patch));
var child = proc.spawn(electron,patch, { stdio: 'inherit', windowsHide: false })
child.on('close', function (code, signal) {
  if (code === null) {
    console.error(electron, 'exited with signal', signal)
    process.exit(1)
  }
  process.exit(code)
})

const handleTerminationSignal = function (signal) {
  process.on(signal, function signalHandler () {
    if (!child.killed) {
      child.kill(signal)
    }
  })
}

handleTerminationSignal('SIGINT')
handleTerminationSignal('SIGTERM')
