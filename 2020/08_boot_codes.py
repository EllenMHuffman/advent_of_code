from collections import defaultdict


def read_lines():
    file = open("08_boot_codes.txt")
    lines = file.read().split("\n")
    return lines


def execute_code(code, i, acc, flipped=False):
    if not code:
        return None, acc

    action, value = code.split(" ")
    if (not flipped and action == "nop") or (flipped and action == "jmp"):
        i += 1
    elif action == "acc":
        i += 1
        acc += int(value)
    elif (not flipped and action == "jmp") or (flipped and action == "nop"):
        i += int(value)
    return i, acc


def find_acc_before_loop(codes):
    i = 0
    acc = 0
    used_instructions = set()

    while i not in used_instructions:
        used_instructions.add(i)
        i, acc = execute_code(codes[i], i, acc)

    return acc


def search(graph, visited, current):
    if current not in visited:
        visited.add(current)
        for i in graph[current]:
            search(graph, visited, i)
    return visited


def find_acc_for_flipped_instruction(instructions):
    # create dict of index and what points to it
    target_graph = defaultdict(list)
    for i, instruction in enumerate(instructions):
        target_i, _ = execute_code(instructions[i], i, 0)
        target_graph[target_i].append(i)

    # find set of values that lead to final index
    success_set = search(target_graph, set(), None)

    # start executing instructions, flipping each and checking if new value is in target set
    should_flip = True
    i = 0
    acc = 0
    while i is not None:
        new_i, new_acc = execute_code(instructions[i], i, acc, should_flip)
        if should_flip and new_i in success_set:
            should_flip = False
            i, acc = new_i, new_acc
        elif not should_flip:
            i, acc = new_i, new_acc
        else:
            i, acc = execute_code(instructions[i], i, acc)

    return acc


def main():
    lines = read_lines()
    # Part 1
    acc_value = find_acc_before_loop(lines)
    print("acc before loop", acc_value)
    assert acc_value == 1600

    # Part 2
    acc_value = find_acc_for_flipped_instruction(lines)
    print("acc after success", acc_value)
    assert acc_value == 1543

if __name__ == "__main__":
    main()
