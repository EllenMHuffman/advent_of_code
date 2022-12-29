def read_input_data():
    file = open("01.txt")
    lines = file.read().split("\n")
    return lines


def main():
    lines = read_input_data()

    calories_per_elf = []
    calories = 0
    for line in lines:
        if line:
            calories += int(line)
        else:
            calories_per_elf.append(calories)
            calories = 0

    calories_per_elf.sort()
    print("most calories: ", calories_per_elf[-1])
    print("top 3 calories: ", sum(calories_per_elf[-3:]))

if __name__ == "__main__":
    main()
