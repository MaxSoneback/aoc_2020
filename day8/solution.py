from utils import import_data, submit
import time


def pre_process(data: []) -> [()]:
    return [(line.split(' ')[0], int(line.split(' ')[1])) for line in data]


def part_1(data: [()], part_2: bool = False) -> int:
    acc = 0
    i = 0
    hist = set()
    while True:
        instr, val = data[i]

        if i in hist:
            break

        hist.add(i)

        if instr == "jmp":
            i += val - 1

        elif instr == "acc":
            acc += val
        i += 1
    if part_2:
        return hist
    return acc


def part_2(data:[()], hist:set) -> int:
    switch = {
        'nop': 'jmp',
        'jmp': 'nop'
    }

    for index in hist:
        instr, val = data[index]
        if instr in switch:
            data[index] = (switch[instr], val)

            timeout = time.time() + 0.1
            acc = 0
            i = 0

            while True:
                instr, val = data[i]

                if time.time() >= timeout:
                    data[index] = (switch[data[index][0]], data[index][1])
                    break

                if instr == "jmp":
                    i += val - 1

                elif instr == "acc":
                    acc += val
                if i == len(data) - 1:
                    return acc
                i += 1

        else:
            continue


if __name__ == "__main__":
    data = import_data(8, __file__, True)
    data = pre_process(data)
    #counter = part_1(data)

    hist = part_1(data, True)
    counter = part_2(data, hist)
    print(f"ans: {counter}")
    res, status = submit(8, 2, counter)
    print(res)
    print(status)