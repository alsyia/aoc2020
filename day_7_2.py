import regex
from collections import defaultdict
from itertools import chain
from utils import parse_input

def build_contains_dict(inputs):
    containers = defaultdict(list)
    reg = regex.compile("(?P<source_bag>.+) bags contain (?:(?P<dest_bag>.+?) bags*(?:, |\.))+")
    for entry in inputs:
        if "contain no other bags." in entry:
            continue
        matches = reg.match(entry)
        source_bag = matches.captures("source_bag")[0]
        dests = matches.captures("dest_bag")
        for dest in dests:
            amount, bag = dest.split(" ", 1)
            containers[source_bag].append((bag, int(amount)))
    return containers

def count_bags_in(bag, contains_dict):
    if bag not in contains_dict:
        return 0
    else:
        return sum(c[1] + c[1]*count_bags_in(c[0], contains_dict) for c in contains_dict[bag])
    
inputs = parse_input("inputs/day_7.txt")

containers = build_contains_dict(inputs)
print(count_bags_in("shiny gold", containers))