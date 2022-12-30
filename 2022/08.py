def read_input_data():
    file = open("08.txt")
    lines = file.read().split("\n")
    return lines


def construct_tree_grid():
    lines = read_input_data()

    rows = []
    columns = [[] for _ in range(len(lines[0]))]

    for line in lines:
        if line:
            trees = [int(l) for l in line]
            rows.append(trees)
            for i, tree in enumerate(trees):
                columns[i].append(tree)

    return rows, columns


def find_visible_trees(rows):
    visible_trees = set()
    for i, row in enumerate(rows):
        # starting from beginning
        highest = 0
        for j, tree in enumerate(row):
            if j == 0 or tree > highest:
                visible_trees.add((i, j))
                highest = tree
            if tree == 9:
                break

        # starting from end
        row_length = len(row) - 1
        highest = 0
        for k, tree in enumerate(row[::-1]):
            if k == 0 or tree > highest:
                visible_trees.add((i, (row_length - k)))
                highest = tree
            if tree == 9:
                break

    return visible_trees


def get_row_score(rows, i, j):
    if i == 0 or i == len(rows) - 1 or j == 0 or j == len(rows[i]) - 1:
        return 0

    max_tree = rows[i][j]
    left_score = 0
    for tree in rows[i][j+1:]:
        left_score += 1
        if tree >= max_tree:
            break

    right_score = 0
    right_slice = rows[i][:j]
    right_slice.reverse()
    for tree in right_slice:
        right_score += 1
        if tree >= max_tree:
            break
    return left_score * right_score


def find_scenic_score(rows, columns):
    highest_score = 0
    scores = dict()
    for i, row in enumerate(rows):
        for j, _ in enumerate(row):
            row_score = get_row_score(rows, i, j)
            scores[(i, j)] = row_score

    for i, col in enumerate(columns):
        for j, _ in enumerate(col):
            row_score = get_row_score(columns, i, j)
            new_score = scores[(j, i)] * row_score
            scores[(j, i)] = new_score
            if new_score > highest_score:
                highest_score = new_score

    return highest_score


def main():
    rows, columns = construct_tree_grid()

    visible_row_trees = find_visible_trees(rows)
    visible_column_trees = set([(y, x) for (x, y) in find_visible_trees(columns)])

    visible_trees = visible_row_trees.union(visible_column_trees)
    print("Visible trees:", len(visible_trees))

    scenic_score = find_scenic_score(rows, columns)
    print("Highest scenic score:", scenic_score)

if __name__ == "__main__":
    main()
