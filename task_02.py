#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""truthy or falsy"""


def bool_to_str(bval):
    """truthy or falsy which equals yes or no

    Args:
        bval: boolean value to determine truthy or falsy

    Returns:
        'Yes' if turhty or 'No'  if falsy

    Examples:
        >>> bool_to_str(True)
        'Yes'
        >>> bool_to_str('')
        'No'
        >>> bool_to_str([])
        'No'
    """

    if bval:
        return 'Yes'
    else:
        return 'No'
