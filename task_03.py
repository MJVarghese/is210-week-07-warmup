#! usr/bin/env python
# -*- coding: utf-8 -*-
"""Analysis"""

import decimal


def lexicographics(to_analyze):
    """ Analysis and Calculations.

    Args:
        to_analyze(str): the required string

    Returns:
        A tuple with max, min and average of words.

    Examples:
        >>> lexicographics('''Don't stop believing,
        Hold on to that feeling.''')
        (5, 3, Decimal('4.0'))
        >>> import data
        >>> lexicographics(data.SHAKESPEARE)
        (12, 5, Decimal('8.14'))
    """
    my_value = []
    my_tup = to_analyze.split('\n')

    for item in my_tup:
        val = len(item.split())
        my_value.append(val)
    return (max(my_value), min(my_value),
            sum(my_value)/decimal.Decimal(len(my_value)))
