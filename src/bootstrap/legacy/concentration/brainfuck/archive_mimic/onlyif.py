# import pygcn
# slowly?
import numpy as np
import time
import torch
import torch.nn.functional as F
import torch.optim as optim

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
adj, features, labels, idx_train, idx_val, idx_test = load_data(path="pygcn/data/cora/")
# first is adj matrix.
# second??
print(adj.shape, features.shape, labels.shape, idx_train.shape, idx_val.shape, idx_test.shape)
# torch.Size([2708, 2708]) torch.Size([2708, 1433]) torch.Size([2708]) torch.Size([140]) torch.Size([300]) torch.Size([1000])
print(type(adj) ,type(features) ,type(labels) ,type(idx_train) ,type(idx_val) ,type(idx_test))
# pdd={"adj":adj, "features":features, "labels":labels, "idx_train":idx_train, "idx_val":idx_val, "idx_test":idx_test}
# for x in pdd.keys():
# print(labels)
#     # print(x.__name__)
#     print(x,pdd[x].shape)
#     print(pdd[x])
# you'd better see this.
# # Model and optimizer
# # anyway, do you want to train some letters? the network made up of letters.
# model = GCN(nfeat=features.shape[1],
#             nhid=args.hidden,
#             nclass=labels.max().item() + 1,
#             dropout=args.dropout)
# optimizer = optim.Adam(model.parameters(),
#                        lr=args.lr, weight_decay=args.weight_decay)
# # just think about the thing.
# if args.cuda:
#     model.cuda()
#     features = features.cuda()
#     adj = adj.cuda()
#     labels = labels.cuda()
#     idx_train = idx_train.cuda()
#     idx_val = idx_val.cuda()
#     idx_test = idx_test.cuda()


# def train(epoch):
#     t = time.time()
#     model.train()
#     optimizer.zero_grad()
#     output = model(features, adj)
#     loss_train = F.nll_loss(output[idx_train], labels[idx_train])
#     acc_train = accuracy(output[idx_train], labels[idx_train])
#     loss_train.backward()
#     optimizer.step()

#     if not args.fastmode:
#         # Evaluate validation set performance separately,
#         # deactivates dropout during validation run.
#         model.eval()
#         output = model(features, adj)

#     loss_val = F.nll_loss(output[idx_val], labels[idx_val])
#     acc_val = accuracy(output[idx_val], labels[idx_val])
#     print('Epoch: {:04d}'.format(epoch+1),
#           'loss_train: {:.4f}'.format(loss_train.item()),
#           'acc_train: {:.4f}'.format(acc_train.item()),
#           'loss_val: {:.4f}'.format(loss_val.item()),
#           'acc_val: {:.4f}'.format(acc_val.item()),
#           'time: {:.4f}s'.format(time.time() - t))


# def test():
#     model.eval()
#     output = model(features, adj)
#     loss_test = F.nll_loss(output[idx_test], labels[idx_test])
#     acc_test = accuracy(output[idx_test], labels[idx_test])
#     print("Test set results:",
#           "loss= {:.4f}".format(loss_test.item()),
#           "accuracy= {:.4f}".format(acc_test.item()))


# # Train model
# t_total = time.time()
# for epoch in range(args.epochs):
#     train(epoch)
# print("Optimization Finished!")
# print("Total time elapsed: {:.4f}s".format(time.time() - t_total))

# # Testing
# test()
