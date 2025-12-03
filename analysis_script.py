import pandas as pd
from synthetic_model import compute_stats

def load_real_data():
    df = pd.read_excel("data/Oschadbank_USD_EUR_PLN.xlsx")

    USD = df["Нбу USD"].dropna().values
    EUR = df["Нбу EUR"].dropna().values
    PLN = df["Нбу PLN"].dropna().values

    return USD, EUR, PLN

def real_stats(USD, EUR, PLN, X1, X2, X3, X4):
    result = pd.DataFrame({
        "USD": compute_stats(USD),
        "EUR": compute_stats(EUR),
        "PLN": compute_stats(PLN),
        "X1_const_normal": compute_stats(X1),
        "X2_const_uniform": compute_stats(X2),
        "X3_quad_normal": compute_stats(X3),
        "X4_quad_uniform": compute_stats(X4),
    })
    result.to_csv("data/stats_real_synthetic.csv")
    return result
