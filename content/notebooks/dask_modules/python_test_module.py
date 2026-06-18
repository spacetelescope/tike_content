"""
This is a simple test module. It will be used to demonstrate how to use files from local modules on a Dask cluster.
"""

import numpy as np


def sum_to_num(num):
    """
    Sums all numbers between 0 and `num`, inclusive of `num`.

    Inputs
    ------
        :num: (int) maximum number to include in the sum.

    Outputs
    -------
        :summed: (int) the sum of all the numbers.
    """

    summed = np.sum(np.arange(num + 1))
    return summed