from functools import reduce


def read_trees():
    file = open("03_trees.txt")
    lines = file.read().split("\n")
    return lines


def move(current_position, slope):
    width = 30
    new_position = current_position + slope
    if new_position > width:
        new_position = new_position - width - 1

    return new_position



def main():
    lines = read_trees()
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    positions = [0, 0, 0, 0, 0]
    trees_qty = [0, 0, 0, 0, 0]

    for i, line in enumerate(lines):
        if line:
            for j, pos in enumerate(positions):
                slope = slopes[j]
                if i % slope[1] == 0:
                    if line[pos] == "#":
                        trees_qty[j] += 1
                    positions[j] = move(pos, slope[0])

    print(trees_qty)
    print(reduce(lambda x, y: x * y, trees_qty))


if __name__ == "__main__":
    main()
