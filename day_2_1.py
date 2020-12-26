from utils import parse_input

def parse_line(line):
    policy, password = line.split(": ")
    rule, letter = policy.split(" ")
    min_occurrences, max_occurrences = rule.split("-")
    return letter, int(min_occurrences), int(max_occurrences), password

def test_policy(letter, min_occurrences, max_occurrences, password):
    occurrences = password.count(letter)
    return min_occurrences <= occurrences <= max_occurrences

def count_valid_passwords(inputs):
    return [test_policy(*parse_line(line)) for line in inputs].count(True)

inputs = parse_input("inputs/day_2.txt")

print(count_valid_passwords(inputs))