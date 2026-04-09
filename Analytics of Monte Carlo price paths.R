set.seed(123)

Nt <- 252
Np <- 1e4

sigma <- 0.3
mu    <- 0.1
dt    <- 1/252

z <- matrix(rnorm(Nt*Np), nrow=Nt)
r <- mu*dt + z*sigma*sqrt(dt)

r <- matrix(rnorm(Nt*Np, mean=mu*dt, sd=sigma*sqrt(dt)), nrow=Nt)

s <- matrix(0, Nt+1, Np)
for (t in 1:Nt) {
  s[t+1,] <- s[t,] + r[t,]
}

P <- exp(s)
matplot(P[,1:Np], type="l")

R <- P[Nt + 1, ] - 1

mean(R)
sd(R)
hist(R, breaks = 50)
hist(log(1+R))
plot.ecdf(1+R)
barplot(sort(1+R))
qqnorm(1+R)