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

# Usage: python3 Allele_freq_plotter.py Genepop.DIV plots_dir

import matplotlib.pyplot as plt


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
                    alleles = list(map(str.__add__, alleles1, alleles2))
                else:
                    lines = lines.split()
                    pop=lines[0][:3]

                    freqs = lines[-1 - len(alleles):-1]
                    snp_dict[locus][pop] = list(map(str.__add__, alleles, freqs))
    
    return snp_dict

def plotter(snp_dict, outpath):
    """Docment here"""
    

if __name__ == "__main__":
    from sys import argv
    freq_gather(argv[1])
