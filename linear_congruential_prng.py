import time

def lcprng(m, i, p, seed=None):
    if seed is None:
        seed = time.time_ns()

    while True:
        seed = (m*seed + i) % p
        yield seed

def gen_values(gen_func, count):
    for i in range(count):
        yield next(gen_func)

def get_loop_length(m, i, p):
    loop_length = []
    for seed in range(0,p):
        past_n = []
        for n in lcprng(m, i, p, seed):
            if n in past_n:
                break
            past_n.append(n)
        loop_length.append(len(past_n))

    return max(zip(loop_length, range(0,p)))[::-1]

def get_optimal_mip(mrange=(1,300),irange=(1,300),prange=(1,300)):
    results = []
    for m in range(*mrange):
        for i in range(*irange):
            for p in range(*prange):
                print(m, i, p)
                seed, repeat_length = get_loop_length(m,i,p)
                results.append((repeat_length,(m,i,p,seed)))
    return results
