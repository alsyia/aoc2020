from utils import parse_input

def find_result(inputs):

    for idx_a, a in enumerate(inputs):
        for idx_b, b in enumerate(inputs[idx_a + 1:]):
            for c in inputs[idx_b + 0:]:
                if a + b + c == 2020:
                    return a * b * c

inputs = [int(input) for input in parse_input("inputs/day_1.txt")]

print(find_result(inputs))

