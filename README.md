# misc_plotters
A collection of scripts for plotting several kinds of data.

Some examples of what these scripts produce can be found in the "examples" directory.

-------

## Fst_heatmap.R

This is a dirty script (it's all hardcoded, and uses non-conventional files) to draw the two parts of a Fst plot.

### Input files

The data utilized in this script can be obtained with [Genepop](http://kimura.univ-montp2.fr/~rousset/), in the output.MIG

The first part requires a triangular matrix (upper and lower) of pairwise Fst values. Eg.:

       A B C D
    A  0 2 2 2
    B  1 0 2 2
    C  1 1 0 2
    D  1 1 1 0

Where the 1's are the pairwise Fst values from one dataset and the 2's are for a different dataset. The diagonal must be filled with 0's.

For the second part (the line plots) you will require a file with Fst values for each dataset (one value per line). Eg.:

    1
    1
    1
    1
    1

To use the script, just replace the hard-coded paths with the path to your own files.

### Requirements

This script requires the "corrplot" package. You can download it from CRAN.

-------

## Mantel_plotter.R

This script will plot the data used for a Mantel test and the associates correlation line.
Does not give a very nice result. It has been abandoned before being really useful.
Still full hard-coded.

--------

## Correlogram.R

This script will grab 2 triangular matrices (generated with GenePop), one genetic distance and one of geographic distance and will plot the respective Mantel correlograms.
Fully hard coded.

---------

## map_plotter.R

This script will plot a measurement of genetic diversity (or any value as for that matter) in a coordinate system, along with the interpolation between each data point.
Hard coded and poorly documented (but the code should be simple enough to understand). Use at your own risk.

--------

## Allele_freq_plotter.py

Not yet documented. Sorry for any inconvenience.


## p-value-freqs.py

This script will parse a single column file with one p-value (or q-value) per line and plot a frequency histogram.
Requirements and usage can be found within the script itself.

## License

GPLv3
