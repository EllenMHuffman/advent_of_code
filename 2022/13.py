import sys
from functools import cmp_to_key


def read_input_data(filename):
    file = open(filename)
    lines = file.read().split("\n")
    return lines


def _append_number(lists, number):
    if number != "":
        lists[-1].append(int(number))
        number = ""
    return lists, number


def parse_line(line):
    lists = []
    elements = [e for e in line]
    number = ""

    for e in elements:
        if e == "[":
            lists.append([])
        elif e == "]":
            lists, number = _append_number(lists, number)
            item = lists.pop()
            if lists:
                lists[-1].append(item)
            else:
                return item
        elif e == ",":
            lists, number = _append_number(lists, number)
        else:
            number += e


def evaluate_pair(left, right):
    for i, left_val in enumerate(left):
        try:
            right_val = right[i]
        except IndexError:
            return 1

        if type(left_val) == type(right_val) == int:
            if left_val < right_val:
                return -1
            elif left_val > right_val:
                return 1
        else:
            if type(left_val) == int:
                left_val = [left_val]
            if type(right_val) == int:
                right_val = [right_val]
            result = evaluate_pair(left_val, right_val)
            if result is not None:
                return result

    if len(left) < len(right):
        return -1


def count_ordered_pairs(lines):
    correct_pairs = []
    pair_number = 1
    left = None
    right = None

    for line in lines:
        if line:
            if left is None:
                left = parse_line(line)
            elif right is None:
                right = parse_line(line)
        else:
            is_ordered = evaluate_pair(left, right)
            if is_ordered == -1:
                correct_pairs.append(pair_number)
            pair_number += 1
            left = right = None

    return sum(correct_pairs)


def find_decoder_key(lines):
    DIVIDER_1, DIVIDER_2 = [[2]], [[6]]
    packets = [DIVIDER_1, DIVIDER_2]

    for line in lines:
        if line:
            packets.append(parse_line(line))

    sorted_packets = sorted(packets, key=cmp_to_key(evaluate_pair))

    index_1 = sorted_packets.index(DIVIDER_1) + 1
    index_2 = sorted_packets.index(DIVIDER_2) + 1

    return index_1 * index_2


def main(filename):
    lines = read_input_data(filename)

    ordered_pair_count = count_ordered_pairs(lines)
    print("Solution 1:", ordered_pair_count)

    decoder_key = find_decoder_key(lines)
    print("Solution 2:", decoder_key)


if __name__ == "__main__":
    args = sys.argv
    number = args[0].split(".")[0]
    suffix = "a" if "--test" in args else ""
    filename = f"{number}{suffix}.txt"

    main(filename)
