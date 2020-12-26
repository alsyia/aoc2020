import regex
from collections import defaultdict
from itertools import chain
from utils import parse_input

def build_containers_dict(inputs):
    containers = defaultdict(list)
    reg = regex.compile("(?P<source_bag>.+) bags contain (?:\d+ (?P<dest_bag>.+?) bags*(?:, |\.))+")
    for entry in inputs:
        if "contain no other bags." in entry:
            continue
        matches = reg.match(entry)
        source_bag = matches.captures("source_bag")[0]
        dest_bags = matches.captures("dest_bag")
        for bag in dest_bags:
            containers[bag].append(source_bag)
    return containers

def find_containers(bag, containers):
    if bag not in containers:
        return None
    else:
        all_containers = []
        for parent_bag in containers[bag]:
            parents = find_containers(parent_bag, containers)
            if parents is not None:
                all_containers += parents
        return containers[bag] + all_containers

inputs = parse_input("inputs/day_7.txt")

containers = build_containers_dict(inputs)
print(len(set(find_containers("shiny gold", containers))))
