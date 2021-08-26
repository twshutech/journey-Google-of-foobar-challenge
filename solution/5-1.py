# floor(1*sqrt(2)) +
# floor(2*sqrt(2)) +
# floor(3*sqrt(2)) +
# floor(4*sqrt(2)) +
# floor(5*sqrt(2))
# = 1+2+4+5+7 = 19
def solution(str_n):
    import math
    str_n = int(str_n)
    l = [math.floor(i * math.sqrt(2)) for i in range(1, str_n + 1)]
    # print(sum(l))
    return int(sum(l))

print(solution('77'))
print(solution('5'))