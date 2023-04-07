import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 702381553 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = x.shape[0]
    q1 = chi2.ppf(1 - alpha / 2, n * 2)
    q2 = chi2.ppf(alpha / 2, n * 2)
    #  loc = x.mean()
    #  scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return (np.sqrt(sum(x**2) / (q1 * 44)), np.sqrt(sum(x**2) / (q2 * 44)))
