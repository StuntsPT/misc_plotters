#!/usr/bin/Rscript
# Copyright 2015 Francisco Pina Martins <f.pinamartins@gmail.com>
# This file is part of Mantel_plotter.R.
# Mantel_plotter.R is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Mantel_plotter.R is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Mantel_plotter.R. If not, see <http://www.gnu.org/licenses/>.

slatkin_dist_all <- read.csv("~/Dropbox/Science/PhD/Sequenom_SNPs/GenePop/No PIS/Geo/All/Slatkin_distance.txt", sep="\t", header=FALSE)
matrixdata_all <- as.matrix(slatkin_dist_all)
colnames(matrixdata_all) <- c("Slatkin", "Geo")

#all <- plot(matrixdata_all[,"Geo"], matrixdata_all[,"Slatkin"], col="red")
lines(lowess(matrixdata_all[,"Geo"], matrixdata_all[,"Slatkin"]), col="red")

slatkin_dist_neut <- read.csv("~/Dropbox/Science/PhD/Sequenom_SNPs/GenePop/No PIS/Geo/Neutrals/Slatkin_distance.txt", sep="\t", header=FALSE)
matrixdata_neut <- as.matrix(slatkin_dist_neut)
colnames(matrixdata_neut) <- c("Slatkin", "Geo")

all <- plot(matrixdata_neut[,"Geo"], matrixdata_neut[,"Slatkin"], col="green")
#points(matrixdata_neut[,"Geo"], matrixdata_neut[,"Slatkin"], col="green")
lines(lowess(matrixdata_neut[,"Geo"], matrixdata_neut[,"Slatkin"]), col="green")

slatkin_dist_non_neut <- read.csv("~/Dropbox/Science/PhD/Sequenom_SNPs/GenePop/No PIS/Geo/Non-Neutrals/Slatkin_distance.txt", sep="\t", header=FALSE)
matrixdata_non_neut <- as.matrix(slatkin_dist_non_neut)
colnames(matrixdata_non_neut) <- c("Slatkin", "Geo")

points(matrixdata_non_neut[,"Geo"], matrixdata_non_neut[,"Slatkin"], col="blue")
lines(lowess(matrixdata_non_neut[,"Geo"], matrixdata_non_neut[,"Slatkin"]), col="blue")


