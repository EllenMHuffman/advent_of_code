from collections import defaultdict


def read_lines():
    file = open("07_bags.txt")
    lines = file.read().split("\n")
    return lines


def parse_rules(lines):
    rules = {}

    for line in lines:
        if not line:
            return rules

        outside_bag, insides = line.split(" contain ")
        outside_bag = outside_bag[:-4].strip()

        bag_rules = {}
        for inside_bag in insides.split(","):
            inside_bag.strip()
            rule = inside_bag.split(" bag")[0].strip()
            if rule != "no other":
                bag_rules[rule[2:]] = int(rule[0])

        rules[outside_bag] = bag_rules

    return rules


def flip_rules(rules):
    flipped_rules = defaultdict(list)

    for outside, insides in rules.items():
        for color in insides:
            flipped_rules[color].append(outside.strip())

    return flipped_rules


def search(rules, visited, target):
    if target in visited:
        return visited

    visited.add(target)
    for color in rules[target]:
        search(rules, visited, color)

    return visited


def find_qty_containing_gold(rules):
    flipped = flip_rules(rules)
    contains_gold = search(flipped, set(), "shiny gold")
    return len(contains_gold) - 1


def find_qty_inside(rules, target):
    total = 0
    if not rules[target]:
        return total

    for color, value in rules[target].items():
        total += value * find_qty_inside(rules, color)

    total += sum(rules[target].values())
    return total


def main():
    rules = {
        "shiny gold": {"pale indigo": 2,},
        "pale indigo": {"drab blue": 2,},
        "drab blue": {"red": 2,},
        "red": {"yellow": 2,},
        "yellow": {"orange": 2,},
        "orange": {"pale yellow": 2,},
        "pale yellow": {},
    }

    qty = find_qty_inside(rules, "shiny gold")
    print("inside gold test 1", qty)
    assert qty == 126

    rules = {
        "faded blue": {},
        "dotted black": {},
        "vibrant plum": {
            "faded blue": 5,
            "dotted black": 6,
        },
        "dark olive": {
            "faded blue": 3,
            "dotted black": 4,
        },
        "shiny gold": {
            "dark olive": 1,
            "vibrant plum": 2,
        },
    }
    qty = find_qty_inside(rules, "shiny gold")
    print("inside gold test 2", qty)
    assert qty == 32

    lines = read_lines()
    rules = parse_rules(lines)
    print("contains gold", find_qty_containing_gold(rules))
    print("inside gold", find_qty_inside(rules, "shiny gold"))


if __name__ == "__main__":
    main()
