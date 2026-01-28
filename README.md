# monte-carlo-engine

This repository contains a sequence of small Monte Carlo experiments I built to understand how randomness, uncertainty, and simulation are used in financial mathematics.
The goal is learning and intuition, not performance or production-ready code.

The notebooks are written step by step, starting from basic Monte Carlo ideas and gradually moving toward applications in asset pricing and option valuation.

⸻

Motivation

In many real financial problems, expectations cannot be computed analytically.
Monte Carlo methods provide a practical way to approximate these quantities by simulating many possible future outcomes and averaging results.

I built this project to:
	•	understand Monte Carlo methods beyond formulas
	•	see how uncertainty behaves over time
	•	connect probability theory to financial models such as GBM and Black–Scholes
	•	gain hands-on experience with simulation-based pricing

⸻

Notebook Overview

01_mc_basics.ipynb

Introduces Monte Carlo estimation using simple random variables.

Focus:
	•	Law of Large Numbers
	•	Central Limit Theorem
	•	Convergence of sample averages

Real-world relevance:
	•	Estimating expectations when no closed-form solution exists
	•	Foundation for all simulation-based pricing and risk models

⸻

02_mc_paths_random_walks.ipynb

Constructs discrete-time random walks.

Focus:
	•	Pathwise uncertainty
	•	Accumulation of randomness over time

Real-world relevance:
	•	Modeling time-evolving uncertainty
	•	Building intuition for stochastic processes used in finance

⸻

03_mc_brownian_motion.ipynb

Simulates Brownian motion and verifies theoretical properties.

Focus:
	•	Continuous-time stochastic processes
	•	Empirical vs theoretical variance growth

Real-world relevance:
	•	Brownian motion is the core noise process in modern financial models
	•	Used in interest rates, equity prices, and volatility modeling

⸻

04_mc_gbm.ipynb

Simulates Geometric Brownian Motion using the exact analytical solution.

Focus:
	•	Log-normal price dynamics
	•	Drift and volatility effects
	•	Distribution of terminal prices

Real-world relevance:
	•	Baseline model for equity prices
	•	Used in option pricing and valuation under uncertainty

⸻

05_mc_option_pricing.ipynb

Prices a European call option using Monte Carlo simulation.

Focus:
	•	Risk-neutral pricing
	•	Discounted payoffs
	•	Convergence to the Black–Scholes benchmark
	•	Confidence intervals via CLT

Real-world relevance:
	•	Pricing derivatives when closed-form solutions are unavailable
	•	Foundation for exotic option pricing and risk analysis

⸻

06_mc_variance_reduction_antithetic.ipynb

Applies antithetic variates to reduce Monte Carlo variance.

Focus:
	•	Variance reduction techniques
	•	Efficiency improvements without increasing simulations

Real-world relevance:
	•	Essential for large-scale pricing and risk systems
	•	Used in practice to reduce computational cost

⸻

What This Project Is (and Is Not)

This project is:
	•	educational
	•	exploratory
	•	focused on intuition and correctness

This project is not:
	•	a production pricing engine
	•	optimized for speed
	•	a replacement for analytical methods

⸻

Why Monte Carlo Matters

Monte Carlo methods are widely used in:
	•	derivative pricing (especially exotic products)
	•	risk management and stress testing
	•	portfolio simulation
	•	financial engineering problems with high uncertainty

This project reflects my interest in understanding these tools at a fundamental level and motivates further study in financial mathematics and stochastic modeling.

⸻

Tools Used
	•	Python
	•	NumPy
	•	Matplotlib
	•	Jupyter / Google Colab
