# also easy to get killed: pydoc3 -k database
# pydoc3 is better than your fucking hell evil recursive import module.
# i need tool to inspect one package.
# it is accessible, via .__all__
# really funny.
# consider text writing as multidimentional. espec+-ially in source code composition.
# use ipython3?
# that is wrong. i always make the same mistake.
# it would be problematic.
# it only appends those with modules, but does not append those without a module.
# i think i need to sample those modules.
# cd /usr/lib/go-1.14/pkg/tool/linux_amd64
# addr2line*  buildid*  cover*  fix*   objdump*  test2json*
# api*        cgo*      dist*   link*  pack*     trace*
# asm*        compile*  doc*    nm*    pprof*    vet*
import torch
from sklearn import datasets
d = datasets.load_boston().data
# print(type(d))
e=torch.from_numpy(d)
# <class 'numpy.ndarray'>
# <class 'torch.Tensor'>
# print(type(e))
# and that is nothing.
p=e.size()
print(p)
# what the heck is that?
print(e[:2,:5])
# that is my dirty hack.
# doc that thing later.
# only use a small fraction of code.
# great. git will never store any valuable information.
# print(d.size())
# t = torch.FloatTensor([23, 24, 24.5])
# p = t.size()
# print(p)
# x = torch.rand(10)
# y = x.size()
# print(y)
# boston_tensor= torch.from_numpy(boston.data)
# print(boston_tensor)
