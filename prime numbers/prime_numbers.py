import numpy as np
import time


def get_index(numbers, low):
    i = 0
    while low > numbers[i]:
        i += 1
    return i


def prime_numbers_1(low, high):
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
    low_ind = get_index(prime_nums, low)

    return prime_nums[low_ind:]


def is_divided(numbers, num):
    return any([num % i == 0 for i in numbers])


def prime_numbers_2(low, high):
    primes = [2, 3]

    for i in range(4, high + 1):
        if not is_divided(primes, i):
            primes.append(i)

    low_ind = get_index(primes, low)

    return primes[low_ind:]


first_time = time.time()
res_1 = prime_numbers_1(0, 100000)
print("--- %s seconds ---" % (time.time() - first_time))

second_time = time.time()
res_2 = prime_numbers_2(0, 100000)
print("--- %s seconds ---" % (time.time() - second_time))

print(f"Are results same? {np.allclose(res_1, res_2)}")
