#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fibonacci sequence numbers."""


def fibonacci(maxint):
    """Fibonacci gen

    Args:
        maxint: an integer that will serve as the upper bound of the loop

    Returns:
        If maxint is not an integer error message will return else, returns
        fiblist: the list containing the Fibonacci sequence numbers

    Examples:
        >>> fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]
        >>> fibonacci(40)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    if not isinstance(maxint, int):
        return '!!! ERROR !!! fibonacci() accepts an integer argument only.'
    else:
        fiba = 0
        fibb = 1
        fiblist = [fiba, fibb]
        while fibb < maxint:
            fiba, fibb = fibb, fiba + fibb
            if fibb < maxint:
                fiblist.append(fibb)
        return fiblist
