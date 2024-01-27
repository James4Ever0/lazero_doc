registry = None
def recv(number):
    global registry
    if registry is not None:
        if number == registry:
            return number+number*1j
        else:
            r=number+registry*1j
            registry=number
            return r
    else:
        registry=number
        return number
# this is self-repeating.
px=[1,2,3,4,5,4,3,2,1]
for x in px:
    print(recv(x))
    # are you sure we can do deeplearning by generating numbers?
    # yes! i am pretty sure. by generating numbers, computer can turn some abstract things into their puriest form.