"""
8 Queens Problem

The 8 queens problem is a classic chess puzzle.
A chess board is an 8x8 grid. The goal is to place 8 queens on the board such that no two queens can "attack" each other using the rules
of chess.

- "Attack" means that two queens are in the same row, column, or diagonal.

=== Example input ===

None

=== Example output ===

Output a solution for the 8 queens in the form of
an 8x8 grid where each cell is either " " or "Q".
"""

import z3
import pytest
from helper import solve, get_solution, SAT, UNSAT, UNKNOWN

"""
=== Generalizations ===

Generalize to an arbitrary N x N board.

"""
