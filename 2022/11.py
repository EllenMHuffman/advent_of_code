import sys
import math


class Monkey:
    inspections = 0
    name = None
    items = None
    operation = None
    modulo = None
    next = None

    def __init__(
        self, name, items, operation, modulo, next
    ):
        self.name = name
        self.items = items
        self.operation = operation
        self.modulo = modulo
        self.next = next  # (A, B) for true/false modulo condition

    def _inspect(self, item, reducer):
        self.inspections += 1
        # solution 2
        if reducer:
            item %= reducer

        updated_item = self.operation(item)

        # solution 1
        if not reducer:
            updated_item //= 3

        return updated_item

    def inspect_items(self, reducer=None):
        return [self._inspect(item, reducer) for item in self.items]

    @property
    def test(self):
        return lambda x: self.next[1] if x % self.modulo else self.next[0]

    def __repr__(self):
        items = ", ".join([str(i) for i in self.items]) or "-"
        return f"<Monkey {self.name}>: {items}"


MONKEYS_TEST = [
    Monkey(
        name=0,
        items=[79, 98],
        operation=lambda x: x * 19,
        modulo=23,
        next=(2, 3),
    ),
    Monkey(
        name=1,
        items=[54, 65, 75, 74],
        operation=lambda x: x + 6,
        modulo=19,
        next=(2, 0),
    ),
    Monkey(
        name=2,
        items=[79, 60, 97],
        operation=lambda x: x * x,
        modulo=13,
        next=(1, 3),
    ),
    Monkey(
        name=3,
        items=[74],
        operation=lambda x: x + 3,
        modulo=17,
        next=(0, 1),
    ),
]
MONKEYS = [
    Monkey(
        name=0,
        items=[80],
        operation=lambda x: x * 5,
        modulo=2,
        next=(4, 3),
    ),
    Monkey(
        name=1,
        items=[75, 83, 74],
        operation=lambda x: x + 7,
        modulo=7,
        next=(5, 6),
    ),
    Monkey(
        name=2,
        items=[86, 67, 61, 96, 52, 63, 73],
        operation=lambda x: x + 5,
        modulo=3,
        next=(7, 0),
    ),
    Monkey(
        name=3,
        items=[85, 83, 55, 85, 57, 70, 85, 52],
        operation=lambda x: x + 8,
        modulo=17,
        next=(1, 5),
    ),
    Monkey(
        name=4,
        items=[67, 75, 91, 72, 89],
        operation=lambda x: x + 4,
        modulo=11,
        next=(3, 1),
    ),
    Monkey(
        name=5,
        items=[66, 64, 68, 92, 68, 77],
        operation=lambda x: x * 2,
        modulo=19,
        next=(6, 2),
    ),
    Monkey(
        name=6,
        items=[97, 94, 79, 88],
        operation=lambda x: x * x,
        modulo=5,
        next=(2, 7),
    ),
    Monkey(
        name=7,
        items=[77, 85],
        operation=lambda x: x + 6,
        modulo=13,
        next=(4, 0),
    ),
]


def main(monkeys, worried):
    modulo_lcm = math.prod([m.modulo for m in monkeys]) if worried else None
    iterations = 10_000 if worried else 20

    for _ in range(iterations):
        for monkey in monkeys:
            items = monkey.inspect_items(modulo_lcm)
            for item in items:
                new_monkey = monkey.test(item)
                monkeys[new_monkey].items.append(item)
            monkey.items = []

    inspections = [m.inspections for m in monkeys]
    inspections.sort()
    monkey_business = inspections[-2] * inspections[-1]
    print("Monkey business:", monkey_business)


if __name__ == "__main__":
    args = sys.argv
    monkeys = MONKEYS_TEST if "--test" in args else MONKEYS
    worried = "--worried" in args

    main(monkeys, worried)
