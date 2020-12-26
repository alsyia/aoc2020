def parse_input(filepath):
    with open(filepath) as input_file:
        lines = input_file.readlines()
        return [line.rstrip("\n") for line in lines]