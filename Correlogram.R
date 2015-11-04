#!/usr/bin/Rscript

library(vegan)

load_trianguar_martix <- function(matrix_file){
    # Load a triangular matrix into a distance object.

    data <- scan(matrix_file)
    num_cols <- (1 + sqrt(1 + 8*length(data)))/2 - 1
    mat <- matrix(0, num_cols, num_cols)
    mat[row(mat) <= col(mat)] <- data
    mat <- t(mat)

    #Finally to get a 'dist' object:

    mat <- rbind(0, mat)
    mat <- cbind(mat, 0)
    dobj <- as.dist(mat)

    return(dobj)
}

Geo.dist <- load_trianguar_martix("~/GeoLN_dist.txt")

All.gen <- load_trianguar_martix("~/Gen_dist.txt")
All.corr <- mantel.correlog(D.eco=All.gen, D.geo=Geo.dist, mult="fdr", nperm=9999)
# summary(All.corr)
plot(All.corr)

Neutral.gen <- load_trianguar_martix("~/Neutral_Gen_dist.txt")
Neutral.corr <- mantel.correlog(D.eco=Neutral.gen, D.geo=Geo.dist, mult="fdr", nperm=9999)
# summary(Neutral.corr)
plot(Neutral.corr)

NNeutral.gen <- load_trianguar_martix("~/NNeutral_Gen_dist.txt")
NNeutral.corr <- mantel.correlog(D.eco=NNeutral.gen, D.geo=Geo.dist, mult="fdr", nperm=9999)
# summary(NNeutral.corr)
plot(NNeutral.corr)

a<-mantel(load_trianguar_martix("~/Neutral_Gen_dist.txt"), Geo.dist, permutations=10000, method="spearman")
a