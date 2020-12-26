from utils import parse_input

def parse_map(inputs):
    map = [list(line) for line in inputs]
    map_width = len(map[0])
    return map, map_width

def count_trees(map, map_width):
    # Slope: right 3, down 1
    # Axis: Y right
    y = 0
    trees = 0
    for row in map:
        if row[y % map_width] == "#":
            trees += 1
        y = y + 3
    return trees

inputs = parse_input("inputs/day_3.txt")
map, map_width = parse_map(inputs)
print(count_trees(map, map_width))