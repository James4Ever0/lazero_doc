class ARA:
    def init(self):
        self.code="nothing"
    def sup0(self,a):
        # def pr(a):
        #     print(a)
        # ab=super()# super of ARB.
        # print(type(sup0))
        # it is a super class?
        # must be in class.
        # print(dir(ab))
        # print(ab.sup(a))
        return a

class ARB(ARA):
    # waht the heck?
    def init(self):
        self.code="nothing"
    def sup(self,a):
        # def pr(a):
            # print(a)
        # ab=super(type(self))# super of ARB.
        ab=super().sup0
        # oh shit.
        # really awful.
        # init the class.
        print(type(ab))
        # it is a super class?
        # must be in class.
        print(dir(ab))
        print(ab(a))
        print(dir(self))
        print(dir(super()))
        # all hidden shit.
        return a
    # print(dir(pr.__code__))
    # print(pr.__code__.__format__(pr.__code__))
    # ac=ab.__thisclass__(pr.__code__,globals())
    # print(ac)
#     # what?
# Help on module code:
# whatever.
# NAME
#     code - Utilities needed to emulate Python's interactive interpreter.
C=ARB()
C.sup("2")