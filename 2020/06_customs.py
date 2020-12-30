from collections import defaultdict


def read_lines():
    file = open("06_customs.txt")
    lines = file.read().split("\n")
    return lines


def get_total_yes_answers(lines):
    total_yes_answers = 0
    yes_answers = set([])

    for line in lines:
        if not line:
            total_yes_answers += len(yes_answers)
            yes_answers = set([])
        else:
            [yes_answers.add(letter) for letter in line]

    return total_yes_answers


def get_group_yes_answers(lines):
    group_yes_answers = 0
    group_answers = defaultdict(int)
    num_in_group = 0

    for line in lines:
        if not line:
            for answer, count in group_answers.items():
                if count == num_in_group:
                    group_yes_answers += 1
            group_answers = defaultdict(int)
            num_in_group = 0
        else:
            num_in_group += 1
            for letter in line:
                group_answers[letter] += 1

    return group_yes_answers


def main():
    lines = read_lines()

    total_yes_answers = get_total_yes_answers(lines)
    group_yes_answers = get_group_yes_answers(lines)

    print(total_yes_answers)
    print(group_yes_answers)


if __name__ == "__main__":
    main()
