def read_input_data():
    file = open("04.txt")
    lines = file.read().split("\n")
    return lines


def main():
    fully_contained_qty = 0
    overlapping_qty = 0

    lines = read_input_data()
    for line in lines:
        if line:
            area_1, area_2 = line.split(",")
            lower_1, upper_1 = [int(a) for a in area_1.split("-")]
            lower_2, upper_2 = [int(a) for a in area_2.split("-")]
            if (
                (lower_1 <= lower_2 and upper_1 >= upper_2) or
                (lower_2 <= lower_1 and upper_2 >= upper_1)
            ):
                fully_contained_qty += 1
                continue

            if (
                (lower_1 <= lower_2 <= upper_1) or
                (lower_1 <= upper_2 <= upper_1)
            ):
                overlapping_qty += 1

    print(fully_contained_qty)
    print(fully_contained_qty + overlapping_qty)


if __name__ == "__main__":
    main()
