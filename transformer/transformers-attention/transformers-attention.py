import torch
import torch.nn.functional as F
import math

def scaled_dot_product_attention(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor) -> torch.Tensor:
    """
    Compute scaled dot-product attention.
    """
    # Your code here
    dk = K.size(-1)
    s = torch.matmul(Q, torch.transpose(K, -2, -1))
    s = s / math.sqrt(dk)
    s = F.softmax(s, dim = -1)
    res = torch.matmul(s, V)
    return res