from synthetic_model import generate_noise, generate_trends, generate_models, save_synthetic_data
from analysis_script import load_real_data, real_stats
from plot_utils import (
    plot_synthetic_models,
    plot_trend_comparison,
    plot_noise_hist,
    plot_real_data
)

# 1. Генерація синтетичних даних
N = 300
noise_norm, noise_unif = generate_noise(N)
trend_const, trend_quad = generate_trends(N)
X1, X2, X3, X4 = generate_models(trend_const, trend_quad, noise_norm, noise_unif)

# Збереження синтетики
save_synthetic_data(X1, X2, X3, X4)

# Графіки синтетики
plot_synthetic_models(X1, X2, X3, X4)
plot_trend_comparison(trend_const, trend_quad)
plot_noise_hist(noise_norm, noise_unif)

# 2. Реальні дані
USD, EUR, PLN = load_real_data()

# 3. Статистика (реальні + синтетичні)
real_stats(USD, EUR, PLN, X1, X2, X3, X4)

# 4. Графік реальних даних
plot_real_data(USD, EUR, PLN)

print("Готово! Дані та графіки створені.")
