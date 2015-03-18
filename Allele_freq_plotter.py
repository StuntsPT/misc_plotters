#!/usr/bin/python3
# Copyright 2015 Francisco Pina Martins <f.pinamartins@gmail.com>
# This file is part of misc_plotters.
# 4misc_plotters is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# misc_plotters is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with misc_plotters.  If not, see <http://www.gnu.org/licenses/>.

import matplotlib.pyplot as plt
import numpy
from scipy.stats import itemfreq


class SNP():
    def __init__(self, name):
        self.name = name[:-3]
        self.bases = name[-3:]
        self.freqs = {}
        

def data_gather(SNPs_filename):
    snp_data = numpy.genfromtxt(SNPs_filename, delimiter = " ", autostrip=True, 
                                 dtype=str, skip_header=False,
                                 filling_values=False)
    cols = numpy.hsplit(snp_data, len(snp_data[0]))
    pops = numpy.delete(cols[0], (0), axis=0)
    pops = sorted(list(set(pops.flat)))
#    test = numpy.concatenate((cols[0], cols[1]), axis=1)
#    split_pops = [test[test[:, 0]==k] for k in numpy.unique(test[:, 0])]
#    print(itemfreq(split_pops[0][:, 1]))
    for i in range(1, len(cols)):
        multicol = numpy.concatenate((cols[0], cols[i]), axis=1)
        target = [multicol[multicol[:, 0]==k] for k in numpy.unique(multicol[:, 0])]
        for p in pops:
            print(itemfreq(target[0][:, 1]))

    #SNPs = snp_data[0][1:]
    #snp_data = numpy.delete(snp_data, (0), axis=0)
    #split_pops = [snp_data[snp_data[:,0]==k] for k in numpy.unique(snp_data[:,0])]
    #print(split_pops[0][0][0])
    #for pop in split_pops:
    #    print(itemfreq(i))

        

data_gather("/home/francisco/Dropbox/Science/PhD/Sequenom_SNPs/Frequencies/SNPs.csv")
