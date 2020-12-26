from utils import parse_input

def parse_groups(inputs):
    groups = []
    current_group = []
    for entry in inputs:
        if entry == "":
            groups.append(current_group)
            current_group = []
        else:
            current_group += [entry]
    groups.append(current_group)
    return groups

def count_answers_everyone_had(groups):
    count = 0
    for group in groups:
        common_answers = set.intersection(*(set(person_answers) for person_answers in group))
        count += len(common_answers)
    return count
    
inputs = parse_input("inputs/day_6.txt")

groups = parse_groups(inputs)
print(count_answers_everyone_had(groups))