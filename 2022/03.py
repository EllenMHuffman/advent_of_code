def read_input_data():
    file = open("03.txt")
    lines = file.read().split("\n")
    return lines

ASCII_OFFSET = 96
PRIORITY_OFFSET = 26
def get_item_value(item):
    value = ord(item.lower()) - ASCII_OFFSET
    if item == item.upper():
        value += PRIORITY_OFFSET

    return value


def main():
    # solution 1
    solution_1_priority_sum = 0

    lines = read_input_data()
    for line in lines:
        if line:
            size = len(line)//2
            comp_1, comp_2 = line[:size], line[size:]
            items_1, items_2 = set([*comp_1]), set([*comp_2])
            intersect = items_1.intersection(items_2)
            solution_1_priority_sum += get_item_value(intersect.pop())

    print(solution_1_priority_sum)

    # solution 2
    solution_2_priority_sum = 0
    group = []

    lines = read_input_data()
    for line in lines:
        if line:
            group.append(line)

        if len(group) == 3:
            items_1, items_2, items_3 = set([*group[0]]), set([*group[1]]), set([*group[2]])
            badge = items_1.intersection(items_2, items_3)
            solution_2_priority_sum += get_item_value(badge.pop())
            group = []

    print(solution_2_priority_sum)


if __name__ == "__main__":
    main()
