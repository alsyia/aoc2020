import math
from utils import parse_input

def parse_map(inputs):
    map = [list(line) for line in inputs]
    map_width = len(map[0])
    return map, map_width

def count_trees(map, map_width, slope_right, slope_down):
    # Slope: right 3, down 1
    # Axis: X down, Y right
    x = 0
    y = 0
    trees = 0
    while x <= len(map) - 1:
        if map[x][y % map_width] == "#":
            trees += 1
        x = x + slope_down
        y = y + slope_right
    return trees

inputs = parse_input("inputs/day_3.txt")
map, map_width = parse_map(inputs)

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

trees_by_slope = [count_trees(map, map_width, slope_right, slope_down) for slope_right, slope_down in slopes]

print(math.prod(trees_by_slope))
