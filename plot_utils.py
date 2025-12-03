import matplotlib.pyplot as plt
import os

def ensure_plots_dir():
    if not os.path.exists("plots"):
        os.makedirs("plots")

def save(name):
    ensure_plots_dir()
    plt.savefig(f"plots/{name}", dpi=200)
    plt.close()

def plot_synthetic_models(X1, X2, X3, X4):
    plt.figure(figsize=(12, 6))
    plt.plot(X1, label="Const + Normal")
    plt.plot(X2, label="Const + Uniform")
    plt.plot(X3, label="Quad + Normal")
    plt.plot(X4, label="Quad + Uniform")
    plt.legend()
    plt.grid()
    plt.title("Синтетичні моделі")
    save("synthetic_models.png")

def plot_trend_comparison(trend_const, trend_quad):
    plt.figure(figsize=(12, 6))
    plt.plot(trend_const, label="Постійний тренд")
    plt.plot(trend_quad, label="Квадратичний тренд")
    plt.legend()
    plt.grid()
    plt.title("Порівняння трендів")
    save("trend_comparison.png")

def plot_noise_hist(noise_norm, noise_unif):
    plt.hist(noise_norm, bins=30)
    plt.title("Гістограма нормального шуму")
    plt.grid()
    save("noise_hist_normal.png")

    plt.hist(noise_unif, bins=30)
    plt.title("Гістограма рівномірного шуму")
    plt.grid()
    save("noise_hist_uniform.png")

def plot_real_data(USD, EUR, PLN):
    plt.figure(figsize=(12, 6))
    plt.plot(USD, label="USD (НБУ)")
    plt.plot(EUR, label="EUR (НБУ)")
    plt.plot(PLN, label="PLN (НБУ)")
    plt.legend()
    plt.grid()
    plt.title("Реальні дані Oschadbank")
    save("real_data_trends.png")
