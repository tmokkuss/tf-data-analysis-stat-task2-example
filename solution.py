import pandas as pd
import numpy as np

from scipy.stats import t


chat_id = 861665812 

def solution(p: float, x: np.array) -> tuple:
    a = 0.095
    n = len(x)
    x_max = x.max()
    alpha = (1 - p)**(1./n)
    left = x_max
    right= (x_max - a) / alpha + a
    return (left, right)
