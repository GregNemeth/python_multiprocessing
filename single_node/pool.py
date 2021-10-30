from multiprocessing import Pool
import time

def f(x):
    return x*x

if __name__ == '__main__':
    start = time.perf_counter()
    with Pool(6) as p:
        print(p.map(f, [35, 47, 87, 118, 232, 345, 356, 649]))
    end = time.perf_counter()
    print(end-start)
