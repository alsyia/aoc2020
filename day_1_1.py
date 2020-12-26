from utils import parse_input

def find_result(inputs):
    for idx, a in enumerate(inputs):
        for b in inputs[idx+1:]:
            if a + b == 2020:
                return a * b

inputs = [int(input) for input in parse_input("inputs/day_1.txt")]

print(find_result(inputs))

