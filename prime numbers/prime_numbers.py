import numpy as np


def get_index(numbers, low):
    i = 0
    while low > numbers[i]:
        i += 1
    return i


def prime_numbers(low, high):
    if not isinstance(low, int) or not isinstance(high, int):
        return []

    if low > high:
        return []

    if low < 0:
        return []

    nums = list(np.arange(0, high + 1))
    nums[1] = 0
    i = 2

    while i <= high:
        if nums[i] != 0:
            j = 2 * i
            while j <= high:
                nums[j] = 0
                j += i
        i += 1

    prime_nums = [num for num in nums if num != 0]

    if not prime_nums:
        return []

    if prime_nums[-1] < low:
        return []

    low_ind = get_index(prime_nums, low)

    return prime_nums[low_ind:]


print(prime_numbers(0, 1))

