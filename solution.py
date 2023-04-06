import numpy as np
import pandas as pd
from scipy.stats import chi2

chat_id = 861665812 

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    mean_x = np.mean(x)
    var_x = np.var(x)
    T = (n - 1) * var_x / 3
    chi_low = np.percentile(np.random.chisquare(n-1, size=100000), (1-p)/2)
    chi_high = np.percentile(np.random.chisquare(n-1, size=100000), 1-(1-p)/2)
    lower = np.sqrt(T / chi_high)
    upper = np.sqrt(T / chi_low)
    return (lower, upper)
