import learn2learn as l2l
# hey! don't you import local package.
# it is like another trap.
import torch
from learn2learn.data.transforms import KShots, NWays, LoadData, RemapLabels, ConsecutiveLabels
from torchvision import transforms
from custom_dataset_from_csv import CustomDatasetFromCsvData
# d=torch.d
import numpy as np
from torch import nn, optim

from torch.nn import functional as F


def accuracy(predictions, targets):
    predictions = predictions.argmax(dim=1)
    acc = (predictions == targets).sum().float()
    acc /= len(targets)
    return acc.item()
# maybe this works?
# it feels like shit coming out of my ass.


class Net(nn.Module):
    def __init__(self, ways=3):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 20, 5, 1)
        self.conv2 = nn.Conv2d(20, 50, 5, 1)
        self.fc1 = nn.Linear(4 * 4 * 50, 500)
        self.fc2 = nn.Linear(500, ways)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, 2, 2)
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, 2, 2)
        x = x.view(-1, 4 * 4 * 50)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)


device = torch.device("cuda")

transformations = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,)),
    lambda x: x.view(1, 28, 28),
])
# transformations = transforms.Compose([transforms.ToTensor()])

# d=CustomDatasetFromCsvLocation("./mnist-demo.csv")
d = CustomDatasetFromCsvData('./mnist-demo.csv',
                             28, 28,
                             transformations)
# import torch.dataset
t = l2l.data.MetaDataset(d)
train_tasks = l2l.data.TaskDataset(
    t, task_transforms=[NWays(t, n=3), KShots(t, k=2), LoadData(t), RemapLabels(t), ConsecutiveLabels(t)], num_tasks=1000)
model = Net(3)

# model = Net(ways)
maml_lr = 0.01
lr = 0.005
iterations = 1000
tps = 32
fas = 5
shots = 1
ways = 3
model.to(device)
meta_model = l2l.algorithms.MAML(model, lr=maml_lr)
opt = optim.Adam(meta_model.parameters(), lr=lr)
loss_func = nn.NLLLoss(reduction='mean')

for iteration in range(iterations):
    iteration_error = 0.0
    iteration_acc = 0.0
    for _ in range(tps):
        learner = meta_model.clone()
        train_task = train_tasks.sample()
        data, labels = train_task
        data = data.to(device)
        labels = labels.to(device)

        # Separate data into adaptation/evalutation sets
        adaptation_indices = np.zeros(data.size(0), dtype=bool)
        adaptation_indices[np.arange(shots*ways) * 2] = True
        evaluation_indices = torch.from_numpy(~adaptation_indices) # what the heck is that?
        adaptation_indices = torch.from_numpy(adaptation_indices)
        adaptation_data, adaptation_labels = data[adaptation_indices], labels[adaptation_indices]
        evaluation_data, evaluation_labels = data[evaluation_indices], labels[evaluation_indices]

        # Fast Adaptation
        for step in range(fas):
            train_error = loss_func(
                learner(adaptation_data), adaptation_labels)
            learner.adapt(train_error)

        # Compute validation loss
        predictions = learner(evaluation_data)
        valid_error = loss_func(predictions, evaluation_labels)
        valid_error /= len(evaluation_data)
        valid_accuracy = accuracy(predictions, evaluation_labels)
        iteration_error += valid_error
        iteration_acc += valid_accuracy

    iteration_error /= tps
    iteration_acc /= tps
    print('Loss : {:.3f} Acc : {:.3f}'.format(
        iteration_error.item(), iteration_acc))

    # Take the meta-learning step
    opt.zero_grad()
    iteration_error.backward()
    opt.step()
# does this work?
# it's that horrible.
# create a torch dataset.
# import pydoc as pd3
# d=dir(l2l)
# e=dir(pd3)
# print(d)
# always wondering the structure of a dataset.
# how to infer that?
# print(e)
# consider this problem: why your heart beats when seeing others not beating?
# the only way to break the rule, is making up a rule to monitor something uncertain (not the rule).
# FUCK.
# what is this anyway?
# this clone might increase some bytes on your machine!
# oh? may it be?
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_version', 'algorithms', 'clone_distribution', 'clone_module', 'clone_parameters', 'copy', 'data', 'detach_distribution', 'detach_module', 'gym', 'magic_box', 'text', 'torch', 'utils', 'vision']
# ['Doc', 'ErrorDuringImport', 'HTMLDoc', 'HTMLRepr', 'Helper', 'ModuleScanner', 'Repr', 'TextDoc', 'TextRepr', '_PlainTextDoc', '__all__', '__author__', '__builtins__', '__cached__', '__credits__', '__date__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_adjust_cli_sys_path', '_escape_stdout', '_get_revised_path', '_is_bound_method', '_re_stripid', '_split_list', '_start_server', '_url_handler', 'allmethods', 'apropos', 'browse', 'builtins', 'classify_class_attrs', 'classname', 'cli', 'cram', 'deque', 'describe', 'doc', 'format_exception_only', 'getdoc', 'getpager', 'help', 'html', 'importfile', 'importlib', 'inspect', 'io', 'isdata', 'ispackage', 'ispath', 'locate', 'os', 'pager', 'pathdirs', 'pipepager', 'pkgutil', 'plain', 'plainpager', 'plaintext', 'platform', 're', 'render_doc', 'replace', 'resolve', 'safeimport', 'sort_attributes', 'source_synopsis', 'splitdoc', 'stripid', 'synopsis', 'sys', 'sysconfig', 'tempfilepager', 'text', 'time', 'tokenize', 'ttypager', 'urllib', 'visiblename', 'warnings', 'writedoc', 'writedocs']
