import re

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
    if not passport.keys() >= required_keys:
        return False
    four_digits_regex = re.compile("^\d{4}$")
    hgt_regex = re.compile("(^\d{2}in$)|(^\d{3}cm$)")
    hcl_regex = re.compile("^#[a-f0-9]{6}$")
    pid_regex = re.compile("^\d{9}$")
    if not four_digits_regex.match(passport["byr"]) or not 1920 <= int(passport["byr"]) <= 2002:
        return False
    if not four_digits_regex.match(passport["iyr"]) or not 2010 <= int(passport["iyr"]) <= 2020:
        return False
    if not four_digits_regex.match(passport["eyr"]) or not 2020 <= int(passport["eyr"]) <= 2030:
        return False
    if not hgt_regex.match(passport["hgt"]):
        return False
    if passport["hgt"][-2] == "cm" and 150 <= int(passport["hgt"][:-2]) <= 193:
        return False
    if passport["hgt"][-2] == "in" and 59 <= int(passport["hgt"][:-2]) <= 76:
        return False
    if not hcl_regex.match(passport["hcl"]):
        return False
    if passport["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        return False
    if not pid_regex.match(passport["pid"]):
        return False
    return True

inputs = parse_input("inputs/day_4.txt")

valid_passports = 0
for passport in parse_passports(inputs):
    if is_passport_valid(passport):
        valid_passports += 1
    else:
        pass

print(valid_passports)