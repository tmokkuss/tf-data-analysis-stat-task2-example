import pandas as pd
import numpy as np

from scipy.stats import t


chat_id = 861665812 

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    alpha = 1 - p
    loc = x.mean()
    t_alpha2 = t.ppf(1 - alpha / 2, n - 1)
    scale = np.sqrt(np.var(x, ddof=1))
    a_hat = 2 * loc / 50**2
    left = a_hat - t_alpha2 * scale / np.sqrt(n) * 2
    right = a_hat + t_alpha2 * scale / np.sqrt(n) * 2
    return (left, right)
