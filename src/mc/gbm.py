import numpy as np


def simulate_terminal_gbm(S0: float, r: float, sigma: float, T: float, Z: np.ndarray) -> np.ndarray:
    """
    Simulate terminal stock prices under risk-neutral GBM using the exact solution.

    Model (risk-neutral):
        S_T = S0 * exp((r - 0.5*sigma^2) * T + sigma * sqrt(T) * Z),
    where Z ~ N(0,1).

    Inputs
    ------
    S0 : initial price
    r  : risk-free rate
    sigma : volatility
    T  : maturity (in years)
    Z  : standard normal draws, shape (n_paths,)

    Returns
    -------
    ST : terminal prices, shape (n_paths,)
    """
    return S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)


def simulate_gbm_paths(
    S0: float, r: float, sigma: float, T: float, n_steps: int, Z: np.ndarray
) -> np.ndarray:
    """
    Simulate full GBM paths on an equally spaced grid using exact lognormal increments.

    Z should be shape (n_paths, n_steps) with i.i.d. N(0,1).

    Returns
    -------
    S : array of shape (n_paths, n_steps + 1)
        S[:,0] = S0, S[:,-1] = S_T
    """
    n_paths = Z.shape[0]
    dt = T / n_steps

    increments = (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z  # log-returns
    logS = np.cumsum(increments, axis=1)
    logS = np.hstack([np.zeros((n_paths, 1)), logS])

    return S0 * np.exp(logS)


def european_call_payoff(ST: np.ndarray, K: float) -> np.ndarray:
    """
    Payoff of a European call option: max(S_T - K, 0).
    """
    return np.maximum(ST - K, 0.0)


def discounted_mean(x: np.ndarray, r: float, T: float) -> float:
    """
    Discounted Monte Carlo estimator: e^{-rT} * mean(x)
    """
    return float(np.exp(-r * T) * np.mean(x))


def mc_price_european_call_terminal(
    S0: float, K: float, r: float, sigma: float, T: float, n_paths: int, seed: int | None = None
) -> float:
    """
    Price a European call option by simulating terminal prices only (fast baseline MC).
    """
    rng = np.random.default_rng(seed)
    Z = rng.standard_normal(n_paths)

    ST = simulate_terminal_gbm(S0=S0, r=r, sigma=sigma, T=T, Z=Z)
    payoff = european_call_payoff(ST, K)

    return discounted_mean(payoff, r=r, T=T)
