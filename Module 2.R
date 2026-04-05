set.seed(123)

p <- 0.5
Nt <- 252
Np <- 1e4

z <- matrix(runif(Nt * Np), nrow = Nt)
x <- sign(p - z)

# Each column is one simulated path over time.
s <- rbind(rep(0, Np), apply(x, 2, cumsum))

matplot(
    s,
    type = "l",
    lty = 1,
    lwd = 0.35,
    col = rgb(0.1, 0.2, 0.8, 0.06),
    xlab = "Time step",
    ylab = "Position",
    main = "Random Walk: 10^4 Simulated Paths"
)