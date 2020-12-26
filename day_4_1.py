from utils import parse_input

def parse_passports(inputs):
    passport = dict()
    for entry in inputs:
        if entry == "":
            yield passport
            passport = dict()
        else:
            tokens = entry.split(" ")
            for token in tokens:
                key, value = token.split(":")
                passport[key] = value
    yield passport

def is_passport_valid(passport):
    required_keys = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
    return passport.keys() >= required_keys

inputs = parse_input("inputs/day_4.txt")

valid_passports = 0
for passport in parse_passports(inputs):
    if is_passport_valid(passport):
        valid_passports += 1

print(valid_passports)