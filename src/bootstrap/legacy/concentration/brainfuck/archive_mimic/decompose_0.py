import numpy as np
import scipy.sparse as sp
idx_features_labels = np.genfromtxt("pygcn/data/cora/cora.content",
                                        dtype=np.dtype(str))
print(idx_features_labels)
print(idx_features_labels.shape)
# whatever shit you do.
# do something useful?
# such as some char?
# great. do it.
# it is not adj matrix.
# why so many zeros? i need to check.
# so both thing have some property.
# the node has property, while nodes have some relationships inbetween.
# z0=idx_features_labels[:, 1:-1]
# features = sp.csr_matrix(z0, dtype=np.float32)
# # just some decompose.
# print(features)
# just move on.
# print(z0)
# # only have these zeros.
# adj = sp.coo_matrix((np.ones(edges.shape[0]), (edges[:, 0], edges[:, 1])),
#                         shape=(labels.shape[0], labels.shape[0]),
#                         dtype=np.float32)
