PACKET_LENGTH = 4
MARKER_LENGTH = 14


def read_input_data():
    file = open("06.txt")
    lines = file.read().split("\n")
    return lines


def is_starter_marker(marker, marker_length):
    chars = [c for c in marker] if marker else []
    return len(chars) == marker_length == len(set(chars))


def find_first_marker(datastream, marker_length):
    for i in range(len(datastream[:-(marker_length-1)])):
        marker_pos = i + marker_length
        marker = datastream[i:marker_pos]
        if is_starter_marker(marker, marker_length):
            return marker_pos


def main():
    lines = read_input_data()
    datastream = lines[0]
    packet_marker = find_first_marker(datastream, PACKET_LENGTH)
    message_marker = find_first_marker(datastream, MARKER_LENGTH)

    print("packet marker: ", packet_marker)
    print("message marker: ", message_marker)


if __name__ == "__main__":
    main()
