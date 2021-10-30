import time

def f(x):
    return x*x

if __name__ == '__main__':
    start = time.perf_counter()
    print(list(map(f, [35, 47, 87, 118, 232, 345, 356, 649])))
    end = time.perf_counter()
    print(end-start)

