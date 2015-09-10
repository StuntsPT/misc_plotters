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

# Usage: python3 p-values_freqs.py p-values.txt
# Where p-values.txt is a single column file with one p-value per line


import matplotlib.pyplot as plt
import numpy as np


def parse_pvalues(pvalue_filename):
    infile = open(pvalue_filename, 'r')
    pvalues = []
    for lines in infile:
        pvalues.append(float(lines.strip()))

    infile.close()
    return pvalues


def plotter(pvalues):
    hist, bins = np.histogram(pvalues, bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.ylabel("Frequency")
    plt.xlabel("p-value")
    plt.show()

if __name__ == "__main__":
    from sys import argv
    ps = parse_pvalues(argv[1])
    plotter(ps)
