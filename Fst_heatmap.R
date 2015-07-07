#!/usr/bin/Rscript
# Copyright 2015 Francisco Pina Martins <f.pinamartins@gmail.com>
# This file is part of Fst_heatmap.R.
# Fst_heatmap.R is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Fst_heatmap.R is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Fst_heatmap.R. If not, see <http://www.gnu.org/licenses/>.


# Usage: Rscript Fst_heatmap.R

# This will draw the color matrix plot
library(corrplot)
trimatirxdata <- read.csv("~/Dropbox/Science/PhD/Sequenom_SNPs/GenePop/With PIS/Fst_matrix_lowerNn_upperN_noPIS_names.txt", sep="\t", header=TRUE)
matrixdata <- as.matrix(trimatirxdata)
corrplot(matrixdata,method="shade", is.corr = FALSE)

# This will draw the line plots

Neut_line_data <- read.csv("~/Dropbox/Science/PhD/Sequenom_SNPs/GenePop/With PIS/Neutrals/Fst_values.txt", sep="\t", header=FALSE)
Neut_matrix <- as.matrix(Neut_line_data)
Neut_matrix[Neut_matrix<0] <- 0

dens <- density(Neut_matrix)
plot(dens$x,length(Neut_matrix)*dens$y,type="l",xlab="Value",ylab="Density", col="black")

Non_neut_line_data <- read.csv("~/Dropbox/Science/PhD/Sequenom_SNPs/GenePop/With PIS/Non-neutral/Fst_values.txt", sep="\t", header=FALSE)
Non_neut_matrix <- as.matrix(Non_neut_line_data)
Non_neut_matrix[Non_neut_matrix<0] <- 0

dens <- density(Non_neut_matrix)
lines(dens$x,length(Non_neut_matrix)*dens$y,type="l",xlab="Value",ylab="Density", lty=2)
#plot(dens$x,length(Non_neut_matrix)*dens$y,type="l",xlab="Value",ylab="Density", col="green")

