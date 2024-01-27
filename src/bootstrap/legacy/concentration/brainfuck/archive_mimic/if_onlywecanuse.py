# import pygcn
# slowly?
import numpy as np
import time
import torch
import torch.nn.functional as F
import torch.optim as optim
# you know it works.
from pygcn.utils import load_data, accuracy
from pygcn.models import GCN
# they are always listening.
# not using that train thing.
class args_:
    def __init__(self):
        self.hidden=16
        self.no_cuda=False
        self.fastmode=False
        self.seed=42
        self.epochs=200
        self.lr=0.01
        self.weight_decay=5e-4
        self.dropout=0.5
# this does not matter at all.
# whatever.
args=args_()
args.cuda = not args.no_cuda and torch.cuda.is_available()
# Load data
adj, features, labels, idx_train, idx_val, idx_test = load_data(path="/root/AGI/lazero/brainfuck/pygcn/data/cora/")
# you'd better see this.
# idx is for index.
# active: 10:00 AM -> 12:00 PM
# 12:00 noon <-> 2:00 AM 
# mod operation.
# how to let computer calc this?
# you can assign random things.
# Model and optimizer
# anyway, do you want to train some letters? the network made up of letters.
model = GCN(nfeat=features.shape[1],
            nhid=args.hidden,
            nclass=labels.max().item() + 1,
            dropout=args.dropout)
optimizer = optim.Adam(model.parameters(),
                       lr=args.lr, weight_decay=args.weight_decay)
# just think about the thing.
if args.cuda:
    model.cuda()
    features = features.cuda()
    adj = adj.cuda()
    labels = labels.cuda()
    idx_train = idx_train.cuda()
    idx_val = idx_val.cuda()
    idx_test = idx_test.cuda()


def train(epoch):
    t = time.time()
    model.train()
    optimizer.zero_grad()
    output = model(features, adj)
    loss_train = F.nll_loss(output[idx_train], labels[idx_train])
    acc_train = accuracy(output[idx_train], labels[idx_train])
    loss_train.backward()
    optimizer.step()

    if not args.fastmode:
        # Evaluate validation set performance separately,
        # deactivates dropout during validation run.
        model.eval()
        output = model(features, adj)

    loss_val = F.nll_loss(output[idx_val], labels[idx_val])
    acc_val = accuracy(output[idx_val], labels[idx_val])
    print('Epoch: {:04d}'.format(epoch+1),
          'loss_train: {:.4f}'.format(loss_train.item()),
          'acc_train: {:.4f}'.format(acc_train.item()),
          'loss_val: {:.4f}'.format(loss_val.item()),
          'acc_val: {:.4f}'.format(acc_val.item()),
          'time: {:.4f}s'.format(time.time() - t))


def test():
    model.eval()
    output = model(features, adj)
    loss_test = F.nll_loss(output[idx_test], labels[idx_test])
    acc_test = accuracy(output[idx_test], labels[idx_test])
    print("Test set results:",
          "loss= {:.4f}".format(loss_test.item()),
          "accuracy= {:.4f}".format(acc_test.item()))


# Train model
t_total = time.time()
for epoch in range(args.epochs):
    train(epoch)
print("Optimization Finished!")
print("Total time elapsed: {:.4f}s".format(time.time() - t_total))

# Testing
test()
