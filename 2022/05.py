from copy import deepcopy


def read_input_data():
    file = open("05.txt")
    lines = file.read().split("\n")
    return lines


def make_initial_crate_stacks():
    rows = []
    lines = read_input_data()
    for line in lines[:9]:
        rows.append(line)

    index = 1
    crates = {}
    stack_names = rows.pop()
    while index < len(stack_names):
        crates[stack_names[index]] = []
        index += 4

    stack = 1
    index = 1
    for row in rows[::-1]:
        while index < len(row):
            value = row[index]
            if value != " ":
                crates[str(stack)].append(value)
            stack += 1
            index += 4
        stack = 1
        index = 1

    return crates


def parse_line(line):
    words = line.split()
    qty = words[1]
    source = words[3]
    target = words[5]
    return int(qty), source, target


def move_crates(crate_stacks, qty, source, target, individually=False):
    moving_crates = crate_stacks[source][-qty:]
    if individually:
        moving_crates.reverse()
    crate_stacks[target].extend(moving_crates)
    crate_stacks[source] = crate_stacks[source][:-qty]
    return crate_stacks


def main():
    crate_stacks_1 = make_initial_crate_stacks()
    crate_stacks_2 = deepcopy(crate_stacks_1)

    lines = read_input_data()
    for line in lines[10:]:
        if line:
            qty, source, target = parse_line(line)
            crate_stacks_1 = move_crates(crate_stacks_1, qty, source, target, True)
            crate_stacks_2 = move_crates(crate_stacks_2, qty, source, target)

    top_crates_1 = [stack[-1] for stack in crate_stacks_1.values()]
    top_crates_2 = [stack[-1] for stack in crate_stacks_2.values()]
    print("".join(top_crates_1))
    print("".join(top_crates_2))


if __name__ == "__main__":
    main()
