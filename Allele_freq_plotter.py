#!/usr/bin/python3
# Copyright 2015 Francisco Pina Martins <f.pinamartins@gmail.com>
# This file is part of misc_plotters.
# misc_plotters is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# misc_plotters is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with misc_plotters.  If not, see <http://www.gnu.org/licenses/>.

# Usage: python3 Allele_freq_plotter.py Genepop.DIV plots_dir

import matplotlib.pyplot as plt
from collections import OrderedDict
from numpy import arange


def freq_gather(freq_filename):
    """Parses the Genepop output file with allele frequencies and returns a
    dict like this: {locus:{pop:[allelesFreq, allelesFreq]}"""
    snp_dict = {}
    with open(freq_filename, "r") as infile:
        interesting = 0
        for lines in infile:
            if interesting == 0 and lines.startswith("Locus:"):
                interesting = 1
                locus = lines.strip().split()[1]
                snp_dict[locus] = {}
            elif interesting == 1 and lines.startswith("Total:"):
                interesting = 0
            elif interesting == 1 and lines.startswith(("\n", "=", "Pop",  "          -")) == False:
                if lines.strip("\n").endswith(" "):
                    alleles1 = lines.strip().split()
                elif lines.strip().endswith("Total"):
                    alleles2 = lines.strip().split()[:-1]
                    alleles = translation(list(map(str.__add__, alleles1, alleles2)))
                else:
                    lines = lines.split()
                    pop = lines[0][:3]

                    freqs = lines[-1 - len(alleles):-1]
                    snp_dict[locus][pop] = OrderedDict()
                    snp_dict[locus][pop] = list(map(str.__add__, alleles, freqs))
    
    return snp_dict

def plotter(snp_dict, outpath):
    """Docment here"""
    width = 0.5
    figcounter = 0
    for snp in snp_dict:
        plt.figure(figcounter)
        locus = snp
        N = len(snp_dict[snp])
        ind = list(range(N))
        ind = arange(N)
        alleles = [x[:2] for x in list(snp_dict[snp].values())[0]]
        frequencies = OrderedDict()
        for pop in snp_dict[snp]:
            frequencies[pop] = list(map(int, [x[2:] for x in snp_dict[snp][pop]]))

        if len(alleles) == 2:
            freqs = [x for x in frequencies.values()]
            p1 = plt.bar(ind, [x[0] for x in freqs], width, color='r')
            p2 = plt.bar(ind, [x[1] for x in freqs], width, color='y', bottom=[x[0] for x in freqs])
            plt.ylabel("Allele Frequency")
            plt.title(locus)
            plt.xticks(ind+width/2., list(frequencies.keys()))
            plt.legend((p1[0], p2[0]), alleles)
            plt.savefig(argv[2] + locus + "_plot.svg", format="svg")
            print(locus + "____2")
            
        elif len(alleles) == 3:
            freqs = [x for x in frequencies.values()]
            p1 = plt.bar(ind, [x[0] for x in freqs], width, color='r')
            p2 = plt.bar(ind, [x[1] for x in freqs], width, color='y', bottom=[x[0] for x in freqs])
            p3 = plt.bar(ind, [x[2] for x in freqs], width, color='g', bottom=[x[1] for x in freqs])
            plt.ylabel("Allele Frequency")
            plt.title(locus)
            plt.xticks(ind+width/2., list(frequencies.keys()))
            plt.legend((p1[0], p2[0], p3[0]), alleles)
            plt.savefig(argv[2] + locus + "_plot.svg", format="svg")
            print(locus + "____3")
            
        plt.close(figcounter)
        figcounter += 1
        
            
def translation(alleles):
    """Get the number encoded alleles and return their ACGT value."""
    tr_table = {ord("1"):"A", ord("2"):"C", ord("3"):"G", ord("4"):"T"}
    alleles = [x.translate(tr_table) for x in alleles]
    
    return alleles


if __name__ == "__main__":
    from sys import argv
    plotter(freq_gather(argv[1]), argv[2])
