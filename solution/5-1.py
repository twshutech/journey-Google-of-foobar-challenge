from decimal import Decimal, getcontext

def solution(s):
    # Use Decimal for flaot precision 101 place.
    getcontext().prec = 101
    r = Decimal(2).sqrt()

    def bs(n):
        if n == 1:
            return 1
        if n < 1:
            return 0
        n_prime = long((r - 1) * n)
        # By beatty sequence properties, we use recurssion.
        return n * n_prime + n * (n + 1) / 2 - n_prime * (n_prime + 1) / 2 - bs(n_prime)
    return str(bs(long(s)))
