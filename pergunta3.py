# Question 3
# Author: Esther Mattos
#
# Problem:
# A board game with a unidirectional path has two players. The winner is the first
# to reach the last square of the board in the fewest turns.
# 
# Players move by spinning a roulette that randomly returns 1, 2, or 3 steps.
# If the number spun is greater than the steps remaining, the player must "loop"
# back to the beginning. Example: if only 2 steps remain and the spin is 3,
# the player moves 2 to the end and then 1 extra back to the first square.
#
# Rule: The minimum board size is 3 squares (no maximum).
#
# Task: Create a function that receives the board size and returns:
#   1. The minimum number of turns required to reach the last square (optimal path).
#   2. The probability of achieving this optimal path.
#   3. The number of different move sequences that reach the last square
#      WITHOUT looping back at any point.
#
# Solution strategy:
#   - (1) Minimum turns = ceil(house / 3), since the maximum step is 3.
#   - (2) Probability = (number of optimal paths) / (3 ^ min_turns).
#   - (3) Count how many sequences of steps (1, 2, 3) sum exactly to `house`
#         in the minimal number of turns (no looping).
#

from math import ceil

def count_paths(remaining, moves_left):
    if remaining == 0 and moves_left == 0:
        return 1
    if remaining < 0 or moves_left == 0:
        return 0
    return (count_paths(remaining - 1, moves_left - 1) +
            count_paths(remaining - 2, moves_left - 1) +
            count_paths(remaining - 3, moves_left - 1))

def board(house: int):
    # (1) Minimum turns
    min_turns = ceil(house / 3)

    # (2) and (3): Count valid paths (no looping, exact fit to "house"
    valid_paths = count_paths(house, min_turns)

    # Total possible paths with min_turns (since roulette always has 3 outcomes)
    total_paths = 3 ** min_turns

    # (2) Probability of success with optimal path
    probability = valid_paths / total_paths if total_paths > 0 else 0

    return min_turns, probability, valid_paths


# Tests
print(board(3))   # (1, probability ~0.333..., valid_paths=1)
print(board(4))   # (2, probability, valid_paths=3)
print(board(5))   # (2, probability, valid_paths=2)
print(board(6))   # (2, probability, valid_paths=1)
print(board(7))   # (3, probability, valid_paths=6)
