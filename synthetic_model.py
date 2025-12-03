import numpy as np
import pandas as pd

# Генерація шумів
def generate_noise(N):
    noise_norm = np.random.normal(0, 1, N)
    noise_unif = np.random.uniform(-1, 1, N)
    return noise_norm, noise_unif

# Генерація трендів
def generate_trends(N):
    t = np.arange(N)
    trend_const = np.full(N, 50)
    trend_quad = 0.01 * t**2 + 0.2 * t + 10
    return trend_const, trend_quad

# Формування моделей
def generate_models(trend_const, trend_quad, noise_norm, noise_unif):
    X1 = trend_const + noise_norm
    X2 = trend_const + noise_unif
    X3 = trend_quad + noise_norm
    X4 = trend_quad + noise_unif
    return X1, X2, X3, X4

# Статистика
def compute_stats(series):
    return pd.Series({
        "mean": float(np.mean(series)),
        "variance": float(np.var(series)),
        "std": float(np.std(series)),
        "min": float(np.min(series)),
        "max": float(np.max(series)),
        "q25": float(np.percentile(series, 25)),
        "median": float(np.median(series)),
        "q75": float(np.percentile(series, 75))
    })

# Збереження синтетичних даних
def save_synthetic_data(X1, X2, X3, X4):
    df = pd.DataFrame({
        "X1_const_normal": X1,
        "X2_const_uniform": X2,
        "X3_quad_normal": X3,
        "X4_quad_uniform": X4
    })
    df.to_excel("data/synthetic_data.xlsx", index=False)
