from itertools import permutations
"""
A rock X
B paper Y
C scissors Z

0 if lost, 3 if draw, 6 if won
"""
# solution 1
translate = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}

loses_to = {
    "A": "B",
    "B": "C",
    "C": "A",
}
# solution 2
wins_to = {v: k for [k, v] in loses_to.items()}
need_to_choose = {
    "X": wins_to,
    "Y": {},
    "Z": loses_to,
}
shape_score = {
    "A": 1,
    "B": 2,
    "C": 3,
}


def read_input_data():
    file = open("02.txt")
    lines = file.read().split("\n")
    return lines


def make_score_rubric():
    rubric = {}

    combs = list(permutations(["A", "B", "C"], 2))
    combs.extend([("A", "A"), ("B", "B"), ("C", "C"),])
    for comb in combs:
        opponent, me = comb

        score = shape_score[me]
        if opponent == me:
            score += 3
        elif loses_to[opponent] == me:
            score += 6

        rubric[comb] = score

    return rubric


def main():
    rubric = make_score_rubric()
    solution_1_total_score = 0
    solution_2_total_score = 0

    lines = read_input_data()
    for line in lines:
        if line:
            # solution 1
            opponent, me = line.split(" ")
            me = translate[me]
            solution_1_total_score += rubric[(opponent, me)]

            # solution 2
            opponent, outcome = line.split(" ")
            me = need_to_choose[outcome].get(opponent, opponent)
            solution_2_total_score += rubric[(opponent, me)]

    print("solution 1 total score: ", solution_1_total_score)
    print("solution 2 total score: ", solution_2_total_score)

if __name__ == "__main__":
    main()
