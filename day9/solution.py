from utils import import_data,submit


def part_1(data: []) -> int:
    def find_outlier(data, i: int = 0, j: int = 25) -> int:
        if j == len(data):
            return float('-inf')
        next_val = data[j]
        m = {next_val - num: num for num in data[i: j]}
        for e in data[i: j]:
            if e in m:
                return find_outlier(data, i + 1, j + 1)
        return next_val
    return find_outlier(data)


def part_2(data:[], invalid_num: int):
    def find_sequence(target: int, data: [], i=0, j=1) -> int:
        seq_sum = sum(data[i:j+1])
        if seq_sum == target:
            return min(data[i:j+1]) + max(data[i:j+1])
        if seq_sum > target:
            return find_sequence(target, data, i+1, j)
        return find_sequence(target, data, i, j+1)

    return find_sequence(invalid_num, data)


if __name__ == "__main__":
    data = [int(x) for x in import_data(9, __file__, True)]
    outlier = part_1(data)
    ans = part_2(data, outlier)
#    res, status = submit(9, 2, ans)
#    print(status)
#    print(res)