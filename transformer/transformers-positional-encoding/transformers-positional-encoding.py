import numpy as np
import math

def positional_encoding(seq_length: int, d_model: int) -> np.ndarray:
    """
    Generate sinusoidal positional encodings.
    """
    # Your code here
    result = np.zeros((seq_length, d_model))
    for i in range(d_model):
        if i % 2 == 0:
            omega = np.exp(i * -(math.log(10000.0) / d_model))
            for j in range(seq_length):
                result[j, i] = math.sin(j / omega)
        else:
            for j in range(seq_length):
                result[j, i] = math.cos(j / omega)
    return result
                
                
        
        
        