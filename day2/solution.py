import re
from utils import import_data


def part_1(pw_list: [str]) -> int:
    counter = 0
    for pw in pw_list:
        match = re.findall("(\w+)", pw)

        if match:
            occ = len(re.findall(match[2], match[3]))
            if int(match[0]) <= occ <= int(match[1]):
                counter += 1

    return counter


def part_2(pw_list: [str]) -> int:
    counter = 0
    for pw in pw_list:
        match = re.findall("(\w+)", pw)

        if len(match) == 4:
            balance = 0
            idx = int(match[0]) - 1
            idy = int(match[1]) - 1
            if match[3][idx] == match[2] or match[3][idy] == match[2]:
                balance += 1
            if match[3][idx] != match[2] or match[3][idy] != match[2]:
                balance -= 1
            if balance == 0:
                counter += 1

    return counter


if __name__ == '__main__':
    data = import_data(2, __file__, True)

    count = part_1(data)
    print(f'Approved {count} passwords for part 1')

    count = part_2(data)
    print(f'Approved {count} passwords for part 2')
