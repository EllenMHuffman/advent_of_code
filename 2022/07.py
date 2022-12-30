TOTAL_DISK_SIZE = 70000000
REQUIRED_SPACE = 30000000

def read_input_data():
    file = open("07.txt")
    lines = file.read().split("\n")
    return lines


# file == (size, name)
class Directory():
    name = None
    parent_directory = None
    files = None
    directories = None

    def __init__(self, name, parent=None):
        self.name = name
        self.parent_directory = parent
        self.files = []
        self.directories = []

    @property
    def size(self):
        return sum([f[0] for f in self.files]) + sum([d.size for d in self.directories])

    def __repr__(self):
        return f"<{self.name}>"


def construct_filesystem():
    home = Directory("/")
    current_node = None
    total_size = 0

    lines = read_input_data()
    for line in lines:
        if line:
            if line == "$ cd /":
                current_node = home
            elif line == "$ cd ..":
                current_node = current_node.parent_directory
            elif line.startswith("$ cd"):
                _, _, name = line.split()
                for dir in current_node.directories:
                    if dir.name == name:
                        current_node = dir
                        break
            elif line == "$ ls":
                pass
            elif line.startswith("dir"):
                _, name = line.split()
                current_node.directories.append(Directory(name, current_node))
            else:
                size, name = line.split()
                total_size += int(size)
                current_node.files.append((int(size), name))

    return home


def get_directory_sizes(sizes, node):
    sizes.append(node.size)
    for d in node.directories:
        get_directory_sizes(sizes, d)


def main():
    filesystem = construct_filesystem()
    sizes = []
    get_directory_sizes(sizes, filesystem)
    restricted_sizes = [s for s in sizes if s <= 100000]

    print("Solution 1:", sum(restricted_sizes))

    used_space = sizes[0]
    needed_space = TOTAL_DISK_SIZE - REQUIRED_SPACE - used_space

    possible_deletions = [s for s in sizes if s >= abs(needed_space)]
    print("Solution 2:", sorted(possible_deletions)[0])


if __name__ == "__main__":
    main()
