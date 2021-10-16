def fiboNaive(n):
    if n <= 1:
        return n
    return fiboNaive(n-2) + fiboNaive(n-1)


def fibo_bp(n):
    mem = [1, 1]
    for i in range(1, n-1):
        mem.append(mem[-2]+mem[-1])
    return mem[-1]




















