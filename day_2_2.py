from utils import parse_input

def parse_line(line):
    policy, password = line.split(": ")
    rule, letter = policy.split(" ")
    first_pos, second_pos = rule.split("-")
    return letter, int(first_pos)-1, int(second_pos)-1, password # Indexes start at 1

def test_policy(letter, first_pos, second_pos, password):
    return (password[first_pos] == letter) ^ (password[second_pos] == letter)

def count_valid_passwords(inputs):
    return [test_policy(*parse_line(line)) for line in inputs].count(True)

inputs = parse_input("inputs/day_2.txt")

print(count_valid_passwords(inputs))