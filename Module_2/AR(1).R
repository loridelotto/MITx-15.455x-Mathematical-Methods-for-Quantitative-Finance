Nt <- 252;
Np = 1e4;
dt <- 1/252;

lambda <- 0.4;
mu <- 0.1;
sigma <- 0.3;
R <- matrix(0, Nt, Np)
epsilon <- matrix(rnorm(Nt*Np, sd=sigma*sqrt(dt)), nrow = Nt)

for (t in 2:Nt){
    R[t,] <- (1+lambda)*(mu*dt) - lambda*R[t-1,] + epsilon[t,]
}
r <- log(1 + R)
acf(R[,1])