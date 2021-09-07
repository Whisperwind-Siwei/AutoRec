import torch
from torch import nn

class AutoEncoder(nn.Module):
    def __init__(self, hidden):
