def largest_sum(numbers: list[int]) -> tuple[int, int]:
    if len(numbers) < 2:
        return None

    sorted_num = sorted(numbers)
    first = sorted_num[-2]
    second = sorted_num[-1]
    return first, second
