import torch
from torch.nn import Sequential as Seq, Linear as Lin, ReLU
from torch_geometric.nn import MessagePassing
# what the heck does it contain?


class EdgeConv(MessagePassing):
    def __init__(self, F_in, F_out):
        super(EdgeConv, self).__init__(aggr="max")
        self.mlp = Seq(Lin(2*F_in, F_out), ReLU(), Lin(F_out, F_out))

    def forward(self, x, edge_index):
        return self.propagate(edge_index, x=x)

    def message(self, x_i, x_j):
        edge_features = torch.cat([x_i, x_j-x_i], dim=1)
        return self.mlp(edge_features)


a = EdgeConv(10, 10)
# works? never know.