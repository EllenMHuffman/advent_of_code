import sys
from collections import defaultdict

START = ord("S")
END = ord("E")


def read_input_data(filename):
    file = open(filename)
    lines = file.read().split("\n")
    return lines


def make_grid(lines):
    grid = []
    for line in lines:
        if line:
            row = [ord(l) for l in line]
            grid.append(row)
    return grid


def find_targets(grid):
    start = None
    end = None
    for i, row in enumerate(grid):
        for j, elevation in enumerate(row):
            if elevation == START:
                start = (i, j)
            if elevation == END:
                end = (i, j)
    return start, end


def find_all_starts(grid):
    starts = []
    for i, row in enumerate(grid):
        for j, elevation in enumerate(row):
            if elevation == ord("a"):
                starts.append((i, j))
    return starts


def make_graph(grid):
    graph = defaultdict(list)
    for i, row in enumerate(grid):
        for j, elevation in enumerate(row):
            if elevation == START:
                elevation = ord("a")
            if elevation == END:
                elevation = ord("z")
            for x, y in (
                (i - 1, j),  # up
                (i + 1, j),  # down
                (i, j - 1),  # left
                (i, j + 1),  # right
            ):
                if x < 0 or y < 0:
                    continue
                try:
                    val = grid[x][y]
                    if val <= elevation + 1:
                        graph[(i, j)].append((x, y))
                except IndexError:
                    continue
    return graph


def traverse_graph(graph, start, end):
    visited = {start}
    paths = {}  # {end: prev}
    queue = [start]

    while queue:
        coord = queue.pop(0)
        if coord == end:
            return paths
        for n in graph[coord]:
            if n not in visited:
                visited.add(n)
                paths[n] = coord
                queue.append(n)


def retrace(paths, start, end):
    count = 0
    pos = end
    while pos != start:
        count += 1
        pos = paths[pos]

    return count


def main(filename):
    lines = read_input_data(filename)
    grid = make_grid(lines)  # 2D array of ord

    start_pos, end_pos = find_targets(grid)
    grid[start_pos[0]][start_pos[1]] = ord("a")
    grid[end_pos[0]][end_pos[1]] = ord("z")

    graph = make_graph(grid)  # dict {coord: [neighbor]}

    paths = traverse_graph(graph, start_pos, end_pos)
    count = retrace(paths, start_pos, end_pos)
    print("Solution 1:", count)

    all_starts = find_all_starts(grid)
    least_count = None
    for start in all_starts:
        paths = traverse_graph(graph, start, end_pos)
        if paths:
            count = retrace(paths, start, end_pos)
            if least_count is None or count < least_count:
                least_count = count
    print("Solution 2:", least_count)


if __name__ == "__main__":
    args = sys.argv
    number = args[0].split(".")[0]
    suffix = "a" if "--test" in args else ""
    filename = f"{number}{suffix}.txt"

    main(filename)
