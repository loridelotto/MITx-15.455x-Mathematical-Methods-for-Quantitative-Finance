import numpy as np
import matplotlib.pyplot as plt

# Simulated daily returns of a financial asset (in %)
np.random.seed(42)
returns = np.concatenate([
    np.random.normal(loc=0.05, scale=1.0, size=950),  # normal returns
    np.random.normal(loc=-3.0, scale=0.5, size=50)    # extreme events (left tail)
])

# Expectation Value (Mean)

mu = np.mean(returns)

# variance

sigma2 = np.mean((returns - mu) ** 2)
sigma = np.sqrt(sigma2)

#  Skewness

skewness = np.mean((returns - mu) ** 3) / sigma**3

# Kurtosis

kurtosis = np.mean((returns - mu) ** 4) / sigma ** 4 - 3

# --- OUTPUT ---
print(f"Mean:      {mu:.4f}")
print(f"Variance:  {sigma2:.4f}")
print(f"Std Dev:   {sigma:.4f}")
print(f"Skewness:  {skewness:.4f}  (expected: negative, left tail)")
print(f"Kurtosis:  {kurtosis:.4f}  (expected: positive, heavy tails)")

# --- PLOT ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Left: histogram of returns with a normal overlay
x = np.linspace(returns.min(), returns.max(), 300)
normal_pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

axes[0].hist(returns, bins=60, density=True, color="steelblue", alpha=0.7, label="Returns")
axes[0].plot(x, normal_pdf, color="red", linewidth=2, label="Normal fit")
axes[0].axvline(mu, color="black", linestyle="--", linewidth=1.2, label=f"Mean = {mu:.2f}")
axes[0].set_title("Return Distribution vs Normal")
axes[0].set_xlabel("Daily Return (%)")
axes[0].set_ylabel("Density")
axes[0].legend()

# Right: time series of returns
axes[1].plot(returns, color="steelblue", linewidth=0.7, alpha=0.8)
axes[1].axhline(mu, color="black", linestyle="--", linewidth=1.2, label=f"Mean = {mu:.2f}")
axes[1].set_title("Daily Returns Over Time")
axes[1].set_xlabel("Day")
axes[1].set_ylabel("Return (%)")
axes[1].legend()

plt.tight_layout()
plt.show()
