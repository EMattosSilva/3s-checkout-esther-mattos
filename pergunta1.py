# Author: Esther Mattos
# Description:
# This function checks whether a given string starts with an uppercase 'B' 
# and ends with an uppercase 'A'. 
# The check is case-sensitive, meaning lowercase 'b' or 'a' will not be valid.
# Examples:
#   "BA"      -> True
#   "Bola"    -> False (ends with lowercase 'a')
#   "BananaA" -> True
#   "bananaA" -> False (starts with lowercase 'b')

def valid_BA_string(s):
    return True if (s[len(s) - 1] == 'A' and s[0] == 'B') else False

strings = [
    "BA",        # starts with B and ends with A → True
    "Bola",      # starts with B but ends with lowercase 'a' → False (case-sensitive)
    "BananaA",   # starts with B and ends with A → True
    "bananaA",   # starts with lowercase b → False
    "BrasilA",   # starts with B and ends with A → True
    "Brasil",    # starts with B but does not end with A → False
    "A",         # does not start with B → False
    "B",         # does not end with A → False
]

for s in strings:
    print(f"'{s}' -> {valid_BA_string(s)}")