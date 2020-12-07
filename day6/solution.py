from utils import import_data, submit
from collections import Counter


def process_data(data: str) -> []:
    data = data.split('\n\n')
    data = [d.split('\n') for d in data]
    return data


def part_1(data: [[]]) -> int:
    c = Counter()
    for group in data:
        answer_set = set()
        for person_answers in group:
            for answer in person_answers:
                answer_set.add(answer)
        c.update(answer_set)
    return sum(c.values())


def part_2(data: [[]]) -> int:
    c1 = Counter({"yes": 0})
    for group in data:
        c2 = Counter()
        for person_answers in group:
            for answer in person_answers:
                c2.update(answer)
        for key, val in c2.most_common():
            if val == len(group):
                c1.update("yes")
            else:
                break

    return c1["yes"]


if __name__ == "__main__":
    data = import_data(6, __file__)
    data = process_data(data)
    count = part_1(data)
    print(count)

    count = part_2(data)
    print(count)

    res, status = submit(day_nr=6, part=2, ans=count)
    print(f"Status code: {status}")
    if status == 200:
        print(res)

