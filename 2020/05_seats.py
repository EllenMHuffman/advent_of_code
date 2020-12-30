from math import ceil

def read_lines():
    file = open("05_seats.txt")
    lines = file.read().split("\n")
    return lines


def find_row(chars):
    rows = [0, 127]
    for char in chars:
        midpoint = ceil((rows[1] - rows[0]) / 2)
        if char == "F":
            rows[1] -= midpoint
        elif char == "B":
            rows[0] += midpoint
    return rows[0]

def find_col(chars):
    cols = [0, 7]
    for char in chars:
        midpoint = ceil((cols[1] - cols[0]) / 2)
        if char == "L":
            cols[1] -= midpoint
        elif char == "R":
            cols[0] += midpoint
    return cols[0]


def get_seat_id(row, col):
    return row * 8 + col


def find_missing_seat(seat_ids):
    seat_ids.sort()
    for i, seat in enumerate(seat_ids):
        if seat + 2 == seat_ids[i + 1]:
            return seat + 1


def main():
    lines = read_lines()
    max_seat_id = 0
    seat_ids = []

    for line in lines:
        row_chars, col_chars = line[:7], line[7:]
        row = find_row(row_chars)
        col = find_col(col_chars)

        seat_id = get_seat_id(row, col)
        seat_ids.append(seat_id)

        if seat_id > max_seat_id:
            max_seat_id = seat_id

    missing_seat = find_missing_seat(seat_ids)

    print("max_seat_id", max_seat_id)
    print("missing_seat", missing_seat)


if __name__ == "__main__":
    main()
