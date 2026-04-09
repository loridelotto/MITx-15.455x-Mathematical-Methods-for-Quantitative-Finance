p <- 0.5; q <- 1-p;
Nt <- 252;
Np <- 1e4;
z <- matrix(runif(Nt*Np), nrow=Nt)
x <- sign(p-z);

s <- rbind(0, apply(x, 2, cumsum))

matplot(0:Nt, s, type="l", lty=1, lwd=0.8,
        xlab="Time step", ylab="Position",
        main=paste(Np, "Random Walks,", Nt, "steps"),
        col=rainbow(Np))