def read_lines():
    file = open("09_xmas_cipher.txt")
    lines = file.read().split("\n")
    return lines


def find_pair(numbers, target):
    numbers.sort()
    i, j = 0, len(numbers) - 1

    while i < j:
        pair_sum = numbers[i] + numbers[j]
        if pair_sum == target:
            return numbers[i], numbers[j]
        if pair_sum < target:
            i += 1
        elif pair_sum > target:
            j -= 1

    return None, None


def find_invalid_number(numbers):
    i = 25
    for number in numbers[i:]:
        pair = find_pair(numbers[i-25:i], number)
        if pair == (None, None):
            return number
        i += 1


def find_contiguous_block(numbers, target):
    i, j = 0, 1

    while j < len(numbers) and i < j:
        block = numbers[i:j]
        block_sum = sum(block)
        if block_sum == target:
            return min(block), max(block)
        if block_sum < target:
            j += 1
        elif block_sum > target:
            i += 1

    return None, None


def find_block_min_max(numbers, target):
    block_min, block_max = find_contiguous_block(numbers, target)
    return block_min + block_max


def main():
    lines = read_lines()
    lines = [int(num) for num in lines if num]
    # Part 1
    invalid_number = find_invalid_number(lines)
    print("first invalid number", invalid_number)
    assert invalid_number == 400480901

    # Part 2
    block_min_max_sum = find_block_min_max(lines, invalid_number)
    print("sum of min/max block", block_min_max_sum)
    assert block_min_max_sum == 67587168


if __name__ == "__main__":
    main()
