import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# =============================================================
# PARAMETERS
# =============================================================
lam1 = 1.0     # rate of X ~ Exp(λ1)
lam2 = 2.0     # rate of Y ~ Exp(λ2)
a    = 3.0     # upper bound of Z ~ Unif(0, a)

# =============================================================
# STEP 0 – Individual PDFs
# =============================================================
# Hint: the PDF of Exp(λ) is  λ * exp(-λ*x)  for x >= 0
# Hint: the PDF of Unif(0,a) is  1/a  for 0 <= z <= a

def f_X(x):
    if x < 0:
        return 0
    return lam1 * np.exp**(-lam1*x)

def f_Y(y):
    if y < 0:
        return 0
    return lam2 * np.exp**(-lam2 *y)

def f_Z(z):
    if 0 <= z <=a:
        return 1.0/a
    return 0.0 

# =============================================================
# STEP 1 – Convolution  S = X + Y
# =============================================================
# f_S(s) = ∫₀ˢ f_X(x) · f_Y(s - x) dx ,   s >= 0
#
# Hint 1: you can compute this analytically! For lam1 ≠ lam2:
#   f_S(s) = (lam1 * lam2) / (lam1 - lam2) * [exp(-lam2*s) - exp(-lam1*s)]
#
# Hint 2: or numerically with scipy.integrate.quad:
#   result, _ = integrate.quad(lambda x: f_X(x) * f_Y(s - x), 0, s)

 def f_S_analytic(s):
    # TODO: implement the closed-form formula above
    #       return 0 for s < 0
    pass

def f_S_numeric(s):
    # TODO: use integrate.quad to compute the convolution integral
    #       return 0 for s < 0
    pass


# =============================================================
# STEP 2 – Convolution  T = S + Z
# =============================================================
# f_T(t) = ∫ f_S(t - z) · f_Z(z) dz
#
# Hint: Z lives in [0, a], and S needs (t - z) >= 0,
#       so the integration limits are z ∈ [max(0, t-?), min(a, t)]
#       Think carefully about what constraint (t - z >= 0) gives you.

def f_T(t):
    # TODO: implement the second convolution
    #       use f_S_analytic (or f_S_numeric) inside the integrand
    #       use integrate.quad with the correct limits
    pass


# =============================================================
# STEP 3 – Theoretical E[T] and Var(T)
# =============================================================
# Since X, Y, Z are independent:
#   E[T] = E[X] + E[Y] + E[Z]
#   Var(T) = Var(X) + Var(Y) + Var(Z)
#
# Recall:  E[Exp(λ)] = 1/λ,   Var[Exp(λ)] = 1/λ²
#          E[Unif(0,a)] = a/2, Var[Unif(0,a)] = a²/12

# TODO: compute E_T and Var_T
E_T   = None
Var_T = None

print(f"E[T]   = {E_T}")
print(f"Var[T] = {Var_T}")
print(f"Std[T] = {np.sqrt(Var_T)}")


# =============================================================
# STEP 4 – Monte Carlo simulation
# =============================================================
np.random.seed(42)
N = 100_000

# TODO: generate N samples from each distribution
# X_samples = np.random.exponential(scale=???, size=N)
#   careful: np.random.exponential takes scale = 1/λ, NOT λ
# Y_samples = ...
# Z_samples = np.random.uniform(low=???, high=???, size=N)
# T_samples = X_samples + Y_samples + Z_samples

# TODO: print simulated mean and variance and compare with theory
# print(f"Simulated E[T]   = {np.mean(T_samples):.4f}")
# print(f"Simulated Var[T] = {np.var(T_samples):.4f}")


# =============================================================
# STEP 5 – Plot: histogram vs theoretical PDF
# =============================================================
# TODO: uncomment and complete once the functions above work
#
# t_vals = np.linspace(0, 15, 500)
# f_T_vals = [f_T(t) for t in t_vals]
#
# plt.figure(figsize=(10, 5))
# plt.hist(T_samples, bins=100, density=True, alpha=0.6,
#          color="steelblue", label="Monte Carlo")
# plt.plot(t_vals, f_T_vals, color="red", linewidth=2,
#          label="Theoretical PDF (convolution)")
# plt.xlabel("t")
# plt.ylabel("Density")
# plt.title("PDF of T = X + Y + Z  via Convolution vs Simulation")
# plt.legend()
# plt.tight_layout()
# plt.show()


# =============================================================
# STEP 6 (bonus) – Verify ∫ f_T(t) dt = 1
# =============================================================
# TODO: use integrate.quad(f_T, 0, np.inf) and check it's ≈ 1.0
