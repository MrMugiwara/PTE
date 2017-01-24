# -*- encoding: utf-8 -*-
# a subset of the six module

from __future__ import unicode_literals, division, print_function,\
                       absolute_import
import operator
import sys


PY2 = sys.version_info[0] == 2

text_type = type('')


if PY2:
    viewitems = operator.methodcaller("viewitems")
else:
    viewitems = operator.methodcaller("items")
