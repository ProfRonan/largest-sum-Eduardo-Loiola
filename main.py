def largest_sum(numbers: list[int]) -> tuple[int, int]:
    if len(numbers) < 2:
        return None
num_alvos = sorted(numbers)
primeiro = num_alvos[-2]
segundo = num_alvos[-1]
   return primeiro, segundo
