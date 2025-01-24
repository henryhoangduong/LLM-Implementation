import torch
import torch.nn as nn
import torch.nn.functional as F

import math
from typing import Optional, List

class LoRALayer():
    def __init__(self):
        pass

class Embedding(nn.Embedding, LoRALayer):
    def __init__(self):
        pass

    def reset_parameters(self):
        pass

    def train(self, mode: bool = True):
        pass

class Linear(nn.Linear, LoRALayer):
    def __init__(self):
        pass    

    def train(self, mode: bool = True):
        def T(w):
            pass

    def forward(self, x: torch.Tensor):
        pass

class MergedLinear(nn.Linear, LoRALayer):
    def __init__(self):
        pass   

class ConvLoRA(nn.Module, LoRALayer):
    pass

class Conv2d(ConvLoRA):
    pass

class Conv1d(ConvLoRA):
    pass

class Conv3d(ConvLoRA):
    pass