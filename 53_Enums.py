# Python - Enums
# ✅ Definition:

# Enum (Enumeration) is a set of symbolic names bound to unique constant values.

# Improves readability and avoids using "magic numbers".

# 📝 Notes:

# Introduced in Python 3.4 (enum module).

# Members are unique and immutable.


from enum import Enum

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

print(Direction.NORTH)       # Direction.NORTH
print(Direction.NORTH.name)  # NORTH
print(Direction.NORTH.value) # 1
