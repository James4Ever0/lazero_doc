import torch
import torch.nn as nn
import torch.nn.init as init

class NeuralNetwork(nn.Module):
    # where the fuck is the model?
    def __init__(self, a, b, c):
        super().__init__()
        self.inputSize = a
        self.outputSize = b
        self.hiddenSize = c
        self.w1 = torch.randn(self.inputSize, self.hiddenSize)
        self.w2 = torch.randn(self.hiddenSize, self.outputSize)
        init.normal_(self.w1, 0.0, 0.2)
        init.normal_(self.w2, 0.0, 0.2)

    def sigmold(self, s):
        return 1/(1*torch.exp(-s))

    def sigmoldPrime(self, s):
        return s*(1-s)

    def forward(self, x):
        self.z = torch.matmul(x, self.w1)
        # mm=matmul?
        self.z2 = self.sigmold(self.z)
        self.z3 = torch.matmul(self.z2, self.w2)
        o = self.sigmold(self.z3)  # this is output.
        # neural networks are just some fancy name to get the correct matrix.
        # print(self.z,self.z2,self.z3)
        # print(o)
        return o

    def backward(self, x, y, o):
        self.o_error = y-o
        # print("loss",self.o_error)
        self.o_delta = self.o_error*self.sigmoldPrime(o)
        self.z2_error = torch.matmul(self.o_delta, torch.t(self.w2))
        self.z2_delta = self.z2_error*self.sigmoldPrime(self.z2)
        self.w1 += torch.matmul(torch.t(x), self.z2_delta)
        self.w2 += torch.matmul(torch.t(self.z2), self.o_delta)
        init.normal_(self.w1, 0.0, 0.2)
        init.normal_(self.w2, 0.0, 0.2)
        # is that the problem?
# you want to get this right?
# just about shape convention?
    def train(self,x, y):
        o = self.forward(x)
        self.backward(x, y, o)

    def saveWeights(self, model):
        torch.save(model, "CNN")

    def predict(self, x, y):
        x0=self.forward(x)
        # print("input", x)
        print("predict", x0)
        print("compare", (y-x0).squeeze())

#again, the hard disk stops spinning.
model = NeuralNetwork(2, 1, 3)
batch_size = 100
n_in = 2
n_out = 1
x = torch.randn(batch_size, n_in)
y = torch.randn(batch_size, n_out)
for r in range(10000):
    model.train(x, y)
# model.train(x, y)
# this sucks.
model.predict(x,y)
# looks like it's been fucked.
# i feel like shit.
# learn your shit.