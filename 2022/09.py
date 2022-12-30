def read_input_data():
    file = open("09.txt")
    lines = file.read().split("\n")
    return lines


def move(current_head, direction):
    x, y = current_head
    if direction == "R":
        x += 1
    if direction == "L":
        x -= 1
    if direction == "U":
        y += 1
    if direction == "D":
        y -= 1
    return x, y


def trail(head, current_tail):
    head_x, head_y = head
    tail_x, tail_y = current_tail
    x_diff = head_x - tail_x
    y_diff = head_y - tail_y

    if abs(x_diff) > 1 and y_diff == 1:
        tail_x, tail_y = move((tail_x, tail_y), "U")
    if x_diff == 1 and abs(y_diff) > 1:
        tail_x, tail_y = move((tail_x, tail_y), "R")
    if abs(x_diff) > 1 and y_diff == -1:
        tail_x, tail_y = move((tail_x, tail_y), "D")
    if x_diff == -1 and abs(y_diff) > 1:
        tail_x, tail_y = move((tail_x, tail_y), "L")

    if x_diff > 1:
        tail_x, tail_y = move((tail_x, tail_y), "R")
    if x_diff < -1:
        tail_x, tail_y = move((tail_x, tail_y), "L")
    if y_diff > 1:
        tail_x, tail_y = move((tail_x, tail_y), "U")
    if y_diff < -1:
        tail_x, tail_y = move((tail_x, tail_y), "D")

    return tail_x, tail_y


def handle_rope(lines, rope_length):
    knot_coordinates = [[(0,0)] for _ in range(rope_length)]

    for line in lines:
        if line:
            direction, qty = line.split()
            moves = int(qty)
            for _ in range(moves):
                first_knot = knot_coordinates[0]
                current_head = first_knot[-1]
                new_head = move(current_head, direction)
                first_knot.append(new_head)

                for knot_coords in knot_coordinates[1:]:
                    current_tail = knot_coords[-1]
                    new_head = trail(new_head, current_tail)
                    knot_coords.append(new_head)

    return knot_coordinates[-1]


def main():
    lines = read_input_data()

    tail_coordinates = handle_rope(lines, 2)
    print("Unique short tail:", len(set(tail_coordinates)))

    tail_coordinates_long = handle_rope(lines, 10)
    print("Unique long tail:", len(set(tail_coordinates_long)))


if __name__ == "__main__":
    main()
