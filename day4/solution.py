import re
from utils import import_data

URL = "https://adventofcode.com/2020/day/4/input"


def process_data(data: str):
    processed_data = []
    passports = [passport.replace(' ', '\n') for passport in data.split('\n\n')]
    for passport in passports:
        pp_dict = dict()
        fields = passport.split('\n')
        for field in fields:
            try:
                pp_dict[field.split(':')[0]] = field.split(':')[1]
            except IndexError:
                continue
        processed_data.append(pp_dict)
    return processed_data


def is_containing_mandatory_fields(passport: {}) -> bool:
    fields = [
        'ecl',
        'pid',
        'eyr',
        'hcl',
        'byr',
        'iyr',
        'hgt'
    ]
    return all(field in passport for field in fields)


def part_1(data: [{}]) -> int:
    def count_valid_passports(data: [{}]) -> int:
        counter = 0
        for passport in data:
            if is_containing_mandatory_fields(passport):
                counter += 1
        return counter

    count = count_valid_passports(data)
    return count


def part_2(data: [{}]) -> int:
    def is_hcl_valid(hcl: str) -> bool:
        match = re.fullmatch('^#(\w){6}$', hcl)
        return match is not None

    def is_pid_valid(pid: str) -> bool:
        match = re.fullmatch('\d{9}', pid)
        return match is not None

    def is_hgt_valid(hgt: str) -> bool:
        hgt_map = {
            'cm': (150, 193),
            'in': (59, 76)
        }
        match = re.match('(^\d{2,3})((in)|(cm))$', hgt)
        if match is not None and len(match.group(1, 2)) == 2:
            val, unit = match.group(1, 2)
            if unit is not None and val is not None:
                if hgt_map[unit][0] <= int(val) <= hgt_map[unit][1]:
                    return True

        return False

    def is_byr_valid(byr: str) -> bool:
        return 1920 <= int(byr) <= 2002

    def is_iyr_valid(iyr: str) -> bool:
        return 2010 <= int(iyr) <= 2020

    def is_eyr_valid(eyr: str) -> bool:
        return 2020 <= int(eyr) <= 2030

    def is_ecl_valid(ecl: str) -> bool:
        valid_ecls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return ecl in valid_ecls

    counter = 0
    for passport in data:
        if is_containing_mandatory_fields(passport):
            if all([is_hcl_valid(passport['hcl']),
                    is_pid_valid(passport['pid']),
                    is_hgt_valid(passport['hgt']),
                    is_byr_valid(passport['byr']),
                    is_iyr_valid(passport['iyr']),
                    is_eyr_valid(passport['eyr']),
                    is_ecl_valid(passport['ecl'])
                    ]):
                counter += 1

    return counter


if __name__ == '__main__':
    data = import_data(4, __file__)
    data = process_data(data)
    count = part_2(data)
    print(count)
