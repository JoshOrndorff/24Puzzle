# 24 Solver
The 24 Puzzle is a game where four integers are given and the goal is to make 24 by combining the given numbers using the operations +, -, *, /.

For example if the numbers are `2, 3, 5, 8`, a solution is `8 * 2 + 3 + 5`.

# Usage
The only dependency is python3. Run the program from a command line with `python3 solver.py`

# Features
* Finds all solutions using the given operators
* Improved runtime (vs brute force) by detecting duplicate states during the search (Dijkstra's Algorithm)
* Finds difficult solutions that are not strictly-left-associative such as `(2 * 5) + (2 * 7)`
* Finds difficult solutions that have non-integer intermediate steps (kinda hack with floats) such as `6 / (1 - 3 / 4)`
* Minor code modification allows increasing (or decreasing) the number of inputs arbitrarily.

# Missing features
* Understanding commutative and associative rules
* Specifying inputs via command line
* Selecting which operators are allowed
* Disabling non-integer intermediaries

# Author
Written by [Joshy Orndorff](https://joshyorndorff.com)

# License
MIT See LICENSE.txt for details
