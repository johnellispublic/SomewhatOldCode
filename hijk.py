
def factors(n):
    factors = set()
    for i in range(1,int(n**0.5 + 1)):
        if n % i == 0:
            factors.add(i)
            factors.add(n//i)

    return factors


def factor_sum(n):
    return sum(factors(n))


def is_perfect(n):
    fact_sum = factor_sum(n) - n

    if n == fact_sum:
        return True
    else:
        return False


def find_perfects(minn,maxn):
    perfect_ns = []
    for n in range(minn,maxn+1):
        if is_perfect(n):
            perfect_ns.append(n)

    return perfect_ns


def find_amicable(minn,maxn):
    amicable_ns = []
    for i in range(minn,maxn+1):
        for j in range(minn,i):
            if factor_sum(i) - i == j and factor_sum(j) - j == i:
                amicable_ns.append((j,i))

    return amicable_ns

print(find_perfects(1,1000))
print(find_amicable(1,1000))
