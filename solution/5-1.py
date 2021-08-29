# r = Decimal(2).sqrt()
# Bir = math.floor(i * r)
# SBn = sum([Bir(i) for i in range(1,n)])



# def solution(str_n):
#     import math
#     str_n = int(str_n)
#     l = [math.floor(i * math.sqrt(2)) for i in range(1, str_n + 1)]
#     # print(sum(l))
#     return int(sum(l))

# print(solution('77'))
# print(solution('5'))
import math
from decimal import Decimal, localcontext

def beatty_sequence(r):
    return

def generator(int_n):
    n = 1
    # l = list([])
    with localcontext() as ctx:
        ctx.prec = 102
        while True:
            n_prime =  n * Decimal(2).sqrt()
            # l.append((n_prime))
            
            frag = n_prime - int(n_prime)
            yield [frag, n]
            n+=1
            if n == int_n + 1:
                # print(l)
                break

def solution(str_n):
    str_n = int(str_n)
    sum_n = 0
    sum_theta = 0
    for i in generator(str_n):
        # print(i)
        sum_n += i[0]
        sum_theta += i[1]

    # sum of numbers
    s = sum_theta
    non_precise_sum = s * Decimal(2).sqrt()
    return int(non_precise_sum - sum_n)
# print(int(23456789876543 * Decimal(2).sqrt()))
print(solution('10'))
print(solution('77'))
print(solution('409400'))
print(solution('5'))



# with localcontext() as ctx:
#     ctx.prec = 102
#     fl_theta = lambda i: i * Decimal(2).sqrt()
#     print(sum([int(fl_theta(i)) for i in range(1, 5)]))
#     print([fl_theta(i) for i in range(1, 5)])
#     print([int(fl_theta(i)) for i in range(1, 5)])
