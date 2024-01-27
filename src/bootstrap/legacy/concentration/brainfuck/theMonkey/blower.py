# import vboxapi
# you are fascinated with the ability to do fuck over computer.
import virtualbox
import time
# how to get a running console?
vbox = virtualbox.VirtualBox()
session=virtualbox.Session()
machine=vbox.find_machine("TinyPlus")
progress=machine.launch_vm_process(session,"gui","")
# not working.
# progress=machine.launch_vm_process(session,"console","")
progress.wait_for_completion()
# how to pass it around?
time.sleep(5)
# not receiving shit.
session.console.keyboard.put_keys("Hello, world!")
# how to get output?
# session.unlock_machine()
# we do this process over and over again.
# progress=machine.launch_vm_process(session,"gui","")
# fast like shit.
# without session?
# ['TinyPlus']
# print([m.name for m in vbox.machines])
# it is off.
# print
# what the heck? why not using ssh?
# we have getting used to it. but how to install on tinycore?