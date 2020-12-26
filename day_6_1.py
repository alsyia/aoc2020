from utils import parse_input

def parse_groups(inputs):
    groups = []
    current_group = ""
    for entry in inputs:
        if entry == "":
            groups.append(current_group)
            current_group = ""
        else:
            current_group += entry
    groups.append(current_group)
    return groups

def count_positive_answers_per_group(groups):
    return sum(len(set(answer)) for answer in groups)  

inputs = parse_input("inputs/day_6.txt")

groups = parse_groups(inputs)
print(count_positive_answers_per_group(groups))