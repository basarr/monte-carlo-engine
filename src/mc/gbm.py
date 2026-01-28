import numpy as np

def simulate_terminal_gbm(S0, r, sigma, T, Z):
    return S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

def european_call_payoff(ST, K):
    return np.maximum(ST - K, 0.0)

def discounted_mean(x, r, T):
    return float(np.exp(-r * T) * np.mean(x))
