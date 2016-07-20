#!/usr/bin/env python3

import os
import sys

import pytest


os.environ['test'] = '1'
args = ['-rsxX', '--tb=native'] + sys.argv[1:]

sys.exit(pytest.main(args + ['unclebob/tests/']))
