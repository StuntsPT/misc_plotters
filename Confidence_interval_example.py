#!/usr/bin/python3
# Copyright 2016 Francisco Pina Martins <f.pinamartins@gmail.com>
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

import numpy as np
import matplotlib.pyplot as plt

def example():
    """
    This is just example code on how to implement confidence intervals on
    numpy/matplotlib.
    """
    y = np.array([0.84097025,0.75629977,0.81300453,0.92482685,0.97089265,0.95719490,1.05375884,0.92784199,0.90493792,0.87466980,1.06920686,0.95997053,0.99620446,0.93575349,0.93254295,0.88172193]) # Marker 420

    y = np.array([6.233, 10.000, 10.033, 1.333, 11.300, 7.000, 4.867, 9.633, 7.400, 10.967, 10.433, 6.600, 6.233, 8.667, 11.633, 8.667]) # Marker 43

    x = np.array([6.233, 10.000, 10.033, 1.333, 11.300, 7.000, 4.867, 9.633, 7.400, 10.967, 10.433, 6.600, 6.233, 8.667, 11.633, 8.667]) # Covariate 8

    x = np.array([69, 175, 121, 60, 134, 110, 93, 133, 71, 144, 112, 111, 77, 121, 116, 126]) # Covariate 10

    fit = np.polyfit(x, y, 1)
    fit_fn = np.poly1d(fit)

    print(fit)

    # Confidence interval
    coord_y = [np.min(fit_fn(x)), np.max(fit_fn(x))]
    coord_x = [np.min(x), np.max(x)]

    predict_y = fit[0] * x + fit[1]
    print(predict_y)

    error_y = y - predict_y

    predict_x = np.arange(np.min(x),np.max(x)+1,1)

    mean_x = np.mean(x)
    n = len(x)
    t = 2.31 # Two tailed 95%
    sum_sq_err = np.sum(np.power(error_y, 2))

    confs = t * np.sqrt((sum_sq_err/(n - 2)) * (1.0 / n + (np.power((predict_x - mean_x), 2) / ((np.sum(np.power(x, 2))) - n * (np.power(mean_x, 2))))))

    # now predict y based on test x-values
    predict_y = fit[0] * predict_x + fit[1]

    # get lower and upper confidence limits based on predicted y and confidence intervals
    lower = predict_y - abs(confs)
    upper = predict_y + abs(confs)

    # /Confidence interval

    # set-up the plot
    #plt.axes().set_aspect('equal')
    plt.xlabel('Covariate 10')
    plt.ylabel('Marker 43 standard freqs')
    plt.title('Linear regression and confidence limits')

    plt.plot(x, y, 'bo', label='Observations')
    plt.plot(coord_x, coord_y, 'r-', label='Regression line')

    plt.plot(predict_x, lower, 'b--',label='Lower confidence limit (95%)')
    plt.plot(predict_x, upper, 'b--',label='Upper confidence limit (95%)')


    plt.xlim(0, 200)
    plt.ylim(0, 15)

    plt.show()
