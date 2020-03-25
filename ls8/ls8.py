#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

# file = open("examples/mult.ls8", "rb")

cpu = CPU()

cpu.load()
cpu.run()