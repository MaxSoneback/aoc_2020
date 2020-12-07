from utils import import_data
from collections import deque


def part_1(t_map: [], x: int = 0, counter: int = 0) -> int:
    if len(t_map) == 0:
        return counter

    row = t_map.popleft()
    x += 3
    if x >= len(row):
        x = x - len(row)
    counter += row[x]

    return part_1(t_map, x, counter)


def part_2(t_map: []) -> int:
    def helper(t_map: [], slope: (int, int), x: int = 0, counter: int = 0) -> int:
        if len(t_map) == 0:
            return counter
        row = []
        for i in range(slope[1]):
            row = t_map.popleft()

        x += slope[0]
        if x >= len(row):
            x = x - len(row)

        counter += row[x]

        return helper(t_map, slope, x, counter)

    r1d1 = helper(t_map.copy(), (1,1))
    r3d1 = helper(t_map.copy(), (3, 1))
    r5d1 = helper(t_map.copy(), (5, 1))
    r7d1 = helper(t_map.copy(), (7, 1))
    r1d2 = helper(t_map.copy(), (1, 2))

    return r1d1 * r3d1 * r5d1 * r7d1 * r1d2


if __name__ == '__main__':
    data = import_data(3, __file__, True)

    treemap = deque()
    for string in data:
        treemap.append([0 if c == '.' else 1 for c in string])
    treemap.popleft()

    count = part_1(treemap.copy())
    print(count)

    count = part_2(treemap.copy())
    print(count)