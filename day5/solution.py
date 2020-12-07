from utils import import_data


def find_seat(b_pass: str) -> int:
    row, b_pass_remaining = find_row(b_pass)
    col = find_col(b_pass_remaining)
    return row * 8 + col


def find_col(b_pass: str, lo: int = 0, hi: int = 8) -> int:
    if not b_pass:
        return lo
    mid = (hi + lo) // 2
    if b_pass[0] == 'L':
        return find_col(b_pass[1:], lo, mid)
    return find_col(b_pass[1:], mid, hi)


def find_row(b_pass: str, lo: int = 0, hi: int = 128) -> (int, str):
    if len(b_pass) == 3:
        return lo, b_pass
    mid = (hi + lo) // 2
    if b_pass[0] == 'F':
        return find_row(b_pass[1:], lo, mid)
    return find_row(b_pass[1:], mid, hi)


def part_1(data: []) -> int:
    return max([find_seat(b_pass) for b_pass in data])


def part_2(data: []) -> int:
    sorted_seats = sorted([find_seat(b_pass) for b_pass in data])
    for i, seat_id in enumerate(sorted_seats):
        if sorted_seats[i + 1] != seat_id + 1:
            return seat_id + 1


if __name__ == "__main__":
    data = import_data(5, __file__, True)

    seat_id = part_1(data)
    print(f"Highest seatID: {seat_id}")

    seat_id = part_2(data)
    print(f"My seatID: {seat_id}")