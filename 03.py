from aoc_utils import Grid2d, Vector2
import string
from itertools import chain

with open('./inp/03.txt') as f:
    schematic = Grid2d('.', f.read().split('\n')) 

class Number: 
    def __init__(self, num, positions): 
        self.num = num
        self.positions = positions

    def __str__(self) -> str:
        return f'{self.num}: {str(self.positions)}'
    
    def __repr__(self) -> str:
        return self.__str__()

#####
#  Part A
#####

# all symbols minus '.', as that's used as the empty char
symbols = set(string.punctuation).difference(set('.'))

possible_part_numbers = []
actual_part_numbers = []

# set cursors and make them aware of bounds
c_x = 0; c_y = 0
ybound, xbound = [schematic.get_bounds()[1].x, schematic.get_bounds()[1].y]

while c_y <= ybound: 
    while c_x < xbound:
        
        num = ""
        n = []
        while schematic[Vector2(c_x, c_y)] in string.digits:
            num = num + schematic[Vector2(c_x, c_y)]
            n.append(Vector2(c_x, c_y))
            c_x += 1

        if num == "":
            c_x += 1
        
        else: 
            possible_part_numbers.append(Number(int(num), n))
    
    c_x = 0
    c_y += 1

_sum = 0
for n in possible_part_numbers: 
    # get set of all neighbors of this number 
    all_neighbors = set(list(chain(*[schematic.get_all_neighbors(position) for position in n.positions]))) - set(n.positions)

    # if there's no surrounding symbol, pass!
    if not any(schematic[i] in symbols for i in all_neighbors):
        continue

    # has surrounding symbol, add to sum
    _sum += n.num
    actual_part_numbers.append(n)

print(_sum)

#####
#  Part B
#####

possible_gears = [k for k,v in schematic.items() if v == '*']

# map of each position that is within a part to the number it's pointing to
position_to_part = {p: part.num for part in actual_part_numbers for p in part.positions}

gear_ratio_sum = 0

# Go through all possible gears, grab their neighbors, and find which has 2 neighbors. 
for pg in possible_gears:
    all_pg_neighbors = schematic.get_all_neighbors(pg)
    parts_as_neighbors = set(position_to_part[i] for i in all_pg_neighbors if i in position_to_part)
    if len(parts_as_neighbors) == 2: 
        gear_ratio_sum += max(parts_as_neighbors) * min(parts_as_neighbors)

print(gear_ratio_sum)
