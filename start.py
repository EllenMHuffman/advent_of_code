import sys
from pathlib import Path


DIRECTORY = "advent_of_code"
FILENAMES = ["input.txt", "input_test.txt", "solution.py"]


def make_boilerplate(year, day):
    return f"""import sys


def read_input_data(is_test):
    test_path = "_test" if is_test else ""
    file = open("{DIRECTORY}/{year}/{day}" + "_input" + test_path + ".txt")
    lines = file.read().split("\\n")
    return lines


def main(lines):
    solution_1 = ""
    print("Part 1 Solution: ", solution_1)

    solution_2 = ""
    print("Part 2 Solution: ", solution_2)


if __name__ == "__main__":
    args = sys.argv
    is_test = "--test" in args
    lines = read_input_data(is_test)

    main(lines)
"""

def main(year, day):
    dir_path = Path(DIRECTORY).resolve() / year
    dir_path.mkdir(parents=True, exist_ok=True)

    for filename in FILENAMES:
        file_path = dir_path / f"{day}_{filename}"
        if file_path.exists():
            print(f"{file_path} already exists. Skipping...")
        else:
            print(f"Creating {file_path}")
            file_path.touch()

        if filename == "solution.py" and file_path.stat().st_size == 0:
            print("Adding boilerplate to solution file")
            with open(file_path, "a") as file:
                # Append data to the file
                file.write(make_boilerplate(year, day))


if __name__ == "__main__":
    args = sys.argv

    try:
        year = args[1]
        day = args[2]
    except IndexError:
        print("ERROR: must include year and day numbers in args")
    else:
        main(year, day)
