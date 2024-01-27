import sys
while True:
    for o in sys.stdin:
        print("this is the input somehow")
        # do we need another thread?
        print(type(o),o)
    print(">>>>>>THE BREAK<<<<<<")
    # it does has the loop over here. nothing detected in stdin.
