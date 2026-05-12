S0    <- 100
mu    <- 0.06      # 6%
sigma <- 0.40      # 40%
Nt    <- 252
Np    <- 10000
dt    <- 1/252
K     <- 100
P     <- 100

Mcpaths <- function(S0, mu, sigma, Nt, Np, dt){
    s <- matrix(0, Nt+1, Np)
    z <- matrix(sign(rnorm(Nt*Np)), ncol=Np)
    r <- mu*dt + z*sigma*sqrt(dt)
    for (t in 1:Nt) { s[t+1, ] <- s[t, ] + r[t, ]}
    S <- S0 * exp(s)
    return(S)
}

S <- Mcpaths(S0, mu, sigma, Nt, Np, dt)
S.terminal <- S[nrow(S), ]

print(mean(S.terminal))
print(sd(S.terminal))

C <- (S-K) * (S>K)
C.terminal <- C[nrow(C), ]
print(mean(C.terminal))

Put <- (P-S) * (P>S)
Put.terminal <- Put[nrow(Put), ]
print(mean(Put.terminal))

# Plot first 100 simulations
matplot(S[, 1:100], type = "l", lty = 1, col = adjustcolor("steelblue", alpha.f = 0.4),
        xlab = "Time Steps", ylab = "Asset Price",
        main = "Monte Carlo Simulation: First 100 Price Paths")
abline(h = K, col = "red", lwd = 2, lty = 2)