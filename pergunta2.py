# Question 2
# Author: Esther Mattos
# 
# Problem:
# Considering the following numeric sequence (11, 18, 25, 32, 39...),
# create a function that receives a position as input and returns 
# the corresponding value in the sequence. 
# For this problem, the sequence starts at position 1.
#
# Solution:
# This is an arithmetic progression with:
#   - First term (a1) = 11
#   - Common difference (d) = 7
# The formula for the n-th term is:
#   a_n = a1 + (n - 1) * d
#
# Examples:
#   get_sequence_value(1)          -> 11
#   get_sequence_value(2)          -> 18
#   get_sequence_value(200)        -> 1404
#   get_sequence_value(254)        -> 1782
#   get_sequence_value(3_542_158)  -> 24_795_110
#

def get_sequence_value(position: int) -> int:
    return 11 if position == 1 else 11 + ((position - 1) * 7)


# Tests
print(get_sequence_value(1))          # 11
print(get_sequence_value(2))          # 18
print(get_sequence_value(200))        # 1404
print(get_sequence_value(254))        # 1782
print(get_sequence_value(3_542_158))  # 24_795_110

# Extra examples
print(get_sequence_value(10))         # 74
print(get_sequence_value(50))         # 356
print(get_sequence_value(1000))       # 7004
print(get_sequence_value(10_000))     # 70_004
