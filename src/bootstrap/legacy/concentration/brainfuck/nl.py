# all the imports. it turns out computer does not need to speak correctly?
# the need to repeat?
class initMachine(object):
    def __init__(self, a=None):
        self.a = a
# do we need to start from basic things?
# what is this for?

    def refresh(self, a=None, k=False):
        if a != None:
            if k:
                self.a = a
            return a
        else:
            return self.a


i = initMachine("something")
print(i.refresh())
print(i.a)
print(i.refresh("nothing"))
print(i.a)
print(i.refresh("everything", True))
print(i.a)