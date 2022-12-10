def prime_validator(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_primes(nums):
    for i in nums:
        if prime_validator(i):
            yield i

