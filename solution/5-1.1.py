from decimal import Decimal, localcontext
import math

def solution(s):
    n = Decimal(s)
    with localcontext() as ctx:
        ctx.prec = 102
        r = Decimal(2).sqrt()
        s = Decimal(2) + Decimal(2).sqrt()

        def solve(n):
            # print('n',n)
            if n == 0:
                return 0
            Brn = int(r * n)
            # print(Brn) 
            Brns = int(Decimal(Brn) / s)
            
            print('return',(Brn * (Brn + 1)) / 2 - solve(Brns) - Brns * (Brns + 1),Brns)
            return (Brn * (Brn + 1)) / 2 - solve(Brns) - Brns * (Brns + 1)

        return str(int(solve(n)))


# print(solution('10'))
solution('77')
# print()
# print(solution('5'))
# print(solution('23456789876543'))