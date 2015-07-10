#!/usr/bin/Rscript
# Copyright 2015 Francisco Pina Martins <f.pinamartins@gmail.com>
# This file is part of map_plotter.R.
# map_plotter.R is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# map_plotter.R is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with map_plotter.R. If not, see <http://www.gnu.org/licenses/>.



library(akima)

tdp <- read.csv("/home/francisco/Dropbox/Science/PhD/Sequenom_SNPs/Maps/He_geo_Ho.txt", sep="\t", header=FALSE)
tdm <- as.matrix(tdp)

x <- as.vector(tdm[,3])
y <- as.vector(tdm[,2])
z <- as.vector(tdm[,4])


akima.li <- interp(x,y,z,yo = seq(min(y), max(y), length = 100),
                   xo = seq(min(x), max(x), length = 100))

with(akima.li,image(x,y,z))

#points(x,y)

#Coordinate conversion:

library(mapproj)
convcoords <- mapproject(x,y, projection="mercator")
newx <- as.vector(unlist(convcoords[1]))
newy <- as.vector(unlist(convcoords[2]))

akima.li <- interp(newx,newy,z,yo = seq(min(newy), max(newy), length = 100),
                   xo = seq(min(newx), max(newx), length = 100))
with(akima.li,image(x,y,z))

#points(newx,newy)
