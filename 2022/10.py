def read_input_data():
    file = open("10.txt")
    lines = file.read().split("\n")
    return lines


def create_instructions(lines):
    cycles = []
    for i, line in enumerate(lines):
        if line:
            if line == "noop":
                cycles.append(0)
                continue
            instruction, value = line.split()
            value = int(value)
            if instruction == "addx":
                cycles.extend([0, value])
            else:
                print("OOOOOPS")
    return cycles


def compute_signal_strengths(instructions):
    total_signal = 0
    cycle = 20
    starting_pos = 1
    while cycle < 250:
        x_register = starting_pos + sum(instructions[:cycle-1])
        signal = cycle * x_register
        cycle += 40
        total_signal += signal

    return total_signal


def create_crt():
    return ["." for _ in range(240)]


def print_crt(crt):
    width = 40
    for i in range(0, len(crt), width):
        print("".join(crt[i:i+width]))


def make_crt_signals(instructions):
    sprite_pos = 1
    sprite_positions = [sprite_pos]
    for cycle in instructions:
        sprite_pos += cycle
        sprite_positions.append(sprite_pos)

    crt = create_crt()
    for i in range(240):
        sprite = sprite_positions[i]
        sprite_range = (sprite - 1, sprite, sprite + 1)
        if i % 40 in sprite_range:
            crt[i] = "#"

    return crt


def main():
    lines = read_input_data()
    instructions = create_instructions(lines)

    total_signal = compute_signal_strengths(instructions)
    print("Solution 1:", total_signal)

    crt = make_crt_signals(instructions)
    print("Solution 2:")
    print_crt(crt)


if __name__ == "__main__":
    main()
