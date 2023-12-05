from collections import defaultdict
from functools import reduce
import operator
import sys

RED = "red"
GREEN = "green"
BLUE = "blue"

TARGETS = {
    RED: 12,
    GREEN: 13,
    BLUE: 14,
}


def read_input_data(is_test):
    test_path = "_test" if is_test else ""
    file = open(f"02_input{test_path}.txt")
    lines = file.readlines()
    return lines


def parse_reveals(reveals):
    parsed_reveals = []
    for reveal in reveals:
        counts = {}
        color_counts = reveal.split(", ")
        for color_count in color_counts:
            qty, color = color_count.split(" ")
            counts[color] = int(qty)
        parsed_reveals.append(counts)
    return parsed_reveals


def parse_game(line):
    game, rest = line.split(":")
    game_id = int(game.split(" ")[1])
    reveals = rest.strip().split("; ")
    parsed_reveals = parse_reveals(reveals)

    return game_id, parsed_reveals


def evaluate_reveals(reveals):
    for reveal in reveals:
        for color, qty in reveal.items():
            if qty > TARGETS[color]:
                return False
    return True


def evaluate_game(game_id, reveals, possible_games):
    is_possible = evaluate_reveals(reveals)
    if is_possible:
        possible_games.append(game_id)


def find_power(reveals, powers):
    min_counts = defaultdict(int)

    for reveal in reveals:
        for color, qty in reveal.items():
            min_counts[color] = max(qty, min_counts[color])

    power = reduce(operator.mul, min_counts.values())
    powers.append(power)


def main(lines):
    possible_games = []
    powers = []

    for line in lines:
        game_id, reveals = parse_game(line)

        evaluate_game(game_id, reveals, possible_games)
        find_power(reveals, powers)

    print("Part 1 Solution: ", sum(possible_games))
    print("Part 2 Solution: ", sum(powers))


if __name__ == "__main__":
    args = sys.argv
    is_test = "--test" in args
    lines = read_input_data(is_test)

    main(lines)
