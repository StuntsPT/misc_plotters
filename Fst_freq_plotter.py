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

# Usage: python3 Fst_freq_plotter.py loci-list.txt
# Where loci-list.txt is a single column file with one Fst value per line


import matplotlib.pyplot as plt
import numpy as np


def parse_fsts(fst_filename):
    """Parses the Fst file and returns a np.array object with the values."""
    fsts = np.genfromtxt(fst_filename, dtype=None, skip_header=True)

    return fsts


def plotter(fsts):
    """Creates and plots the histogram from a list of values or a 1D array."""
    hist, bins = np.histogram(fsts, bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.ylabel("Frequency")
    plt.xlabel("Fst")
    plt.show()

if __name__ == "__main__":
    from sys import argv
    ps = parse_fsts(argv[1])
    plotter(ps)
