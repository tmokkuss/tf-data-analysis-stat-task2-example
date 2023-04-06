import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 861665812 

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    
    n = len(x)
    s2=np.var(x, ddof=1)
    q1 = chi2.ppf(p/2, df = n -1)
    q2 = chi2.ppf(alpha/2, df = n-1)
    left = np.sqrt((n-1)*s2/q2)/np.sqrt(48)
    right =  np.sqrt((n-1)*s2/q1)/np.sqrt(48)
    
    return (left, right)
