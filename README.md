# misc_plotters
A collection of scripts for plotting several kinds of data.

Some examples of what these scripts produce can be found in the "examples" diectory.

-------

## Fst_heatmap.R

This is a dirty script (it's all hardcoded, and uses non-conventional files) to draw the two parts of a Fst plot.

### Input files

The first part requires a triangular matrix (upper and lower) of pairwise Fst values. Eg.:

       A B C D
    A  0 2 2 2
    B  1 0 2 2
    C  1 1 0 2
    D  1 1 1 0
    
Where the 1's are the pairwise Fst values from one dataset and the 2's are for a differente dataset. The diagonal must be filled with 0's.

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

## Allele_freq_plotter.py

Not yet documented. Sorry for any inconvenience.

## License

GPLv3