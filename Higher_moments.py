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

# ============================================================
# TWO IID RANDOM VARIABLES  –  Covariance & Correlation
# ============================================================
# X and Y are independent and identically distributed (IID)
# Both drawn from N(mu=0.05, sigma=1.0) with the same
# extreme-event contamination used above.

np.random.seed(99)
n = 1000

X = np.concatenate([
    np.random.normal(loc=0.05, scale=1.0, size=950),
    np.random.normal(loc=-3.0, scale=0.5, size=50)
])

Y = 3*X 

# --- Covariance (manual) ---
mu_X = np.mean(X)
mu_Y = np.mean(Y)
cov_XY = np.mean((X - mu_X) * (Y - mu_Y))

# --- Correlation (manual) ---
sigma_X = np.std(X)
sigma_Y = np.std(Y)
corr_XY = cov_XY / (sigma_X * sigma_Y)

# --- NumPy built-in (for verification) ---
cov_matrix = np.cov(X, Y, ddof=0)        # population covariance matrix
corr_matrix = np.corrcoef(X, Y)           # correlation matrix

print("\n===== Two IID Variables (X, Y) =====")
print(f"E[X]  = {mu_X:.4f}    E[Y]  = {mu_Y:.4f}")
print(f"σ(X)  = {sigma_X:.4f}   σ(Y)  = {sigma_Y:.4f}")
print(f"Cov(X,Y)  = {cov_XY:.4f}   (expected ≈ 0 for independent vars)")
print(f"Corr(X,Y) = {corr_XY:.4f}   (expected ≈ 0 for independent vars)")
print(f"\nNumPy cov matrix:\n{cov_matrix}")
print(f"\nNumPy corr matrix:\n{corr_matrix}")

# --- Scatter plot ---
fig2, ax2 = plt.subplots(figsize=(6, 6))
ax2.scatter(X, Y, s=8, alpha=0.5, color="steelblue")
ax2.axhline(mu_Y, color="grey", linestyle="--", linewidth=0.8)
ax2.axvline(mu_X, color="grey", linestyle="--", linewidth=0.8)
ax2.set_title(f"Scatter X vs Y  (ρ = {corr_XY:.4f})")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_aspect("equal")
plt.tight_layout()
plt.show()
