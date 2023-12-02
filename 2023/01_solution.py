import sys


WORD_TO_NUM = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def read_input_data(is_test):
    test_path = "_test" if is_test else ""
    file = open(f"01_input{test_path}.txt")
    lines = file.read().split("\n")
    return lines


def count_digits(line, digits):
    first, last = None, None
    chars = [*line]
    i, x = 0, -1
    while first is None or last is None:
        if i == len(chars):
            print("not found", line)
            break
        if first is None:
            if chars[i].isdigit():
                first = chars[i]
            else:
                i += 1
        if last is None:
            if chars[x].isdigit():
                last = chars[x]
            else:
                x -=1
    if first is not None and last is not None:
        digits.append(f"{first}{last}")


def count_real_digits(line, digits):
    first, last = None, None
    chars = [*line]

    for i, char in enumerate(chars):
        if char.isdigit():
            if first is None:
                first = char
            last = char
        else:
            for word in WORD_TO_NUM.keys():
                if word == "".join(chars[i : i + len(word)]):
                    if first is None:
                        first = WORD_TO_NUM[word]
                    last = WORD_TO_NUM[word]
                    break

    digits.append(f"{first}{last}")


def main(lines):
    digits_1 = []
    digits_2 = []

    for line in lines:
        if line:
            count_digits(line, digits_1)
            count_real_digits(line, digits_2)

    print("Part 1 Solution: ", sum([int(d) for d in digits_1]))
    print("Part 2 Solution: ", sum([int(d) for d in digits_2]))


if __name__ == "__main__":
    args = sys.argv
    is_test = "--test" in args
    lines = read_input_data(is_test)

    main(lines)
