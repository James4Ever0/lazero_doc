import virtualbox
import time
vbox = virtualbox.VirtualBox()
session = virtualbox.Session()
# session.console.keyboard.put_keys("Hello, world!")
# these keys are slow.
# print(dir(session))
# session.unlock_machine()
# fucking hell?
machine=vbox.find_machine("TinyPlus")
progress=machine.launch_vm_process(session,"gui","")
progress.wait_for_completion()
time.sleep(6)
# shit.
session.console.keyboard.put_keys("./startup.sh\n")
session.unlock_machine()
# really need to do this?
# locked.
# print(dir(machine))
# shit.
# must use network based.