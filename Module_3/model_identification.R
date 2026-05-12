library(readr)
library(forecast)

dati <- read_csv("asset-v1_MITx+15.455x+2T2024+type@asset+block@PS3-data_Updated.csv")

r1 <- dati$TS1
r2 <- dati$TS2
r3 <- dati$TS3
r4 <- dati$TS4
r5 <- dati$TS5

cat("media annualizzata ritorni 5:", mean(r5, na.rm = TRUE) * 252, "\n")
cat("deviazione standard annualizzata ritorni 5:", sd(r5, na.rm = TRUE) * sqrt(252), "\n")

acf(r1)
acf(r2)
acf(r3)
acf(r4)
acf(r5)