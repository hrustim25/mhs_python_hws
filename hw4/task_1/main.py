import time
import threading
import multiprocessing as mp


def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def run_sync(n, repeats):
    start = time.perf_counter()
    for _ in range(repeats):
        fib(n)
    elapsed = time.perf_counter() - start
    return elapsed


def run_threads(n, workers):
    threads = []

    def worker():
        fib(n)

    start = time.perf_counter()
    for _ in range(workers):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    elapsed = time.perf_counter() - start
    return elapsed


def run_processes(n, workers):
    procs = []

    def worker():
        fib(n)

    start = time.perf_counter()
    for _ in range(workers):
        p = mp.Process(target=worker)
        procs.append(p)
        p.start()

    for p in procs:
        p.join()

    elapsed = time.perf_counter() - start
    return elapsed


def main():
    n = 35
    repeats = 10

    time_sync = run_sync(n, repeats=repeats)

    time_threads = run_threads(n, workers=repeats)

    time_procs = run_processes(n, workers=repeats)

    out_file = "../artifacts/task_1_results.txt"
    with open(out_file, "w") as f:
        f.write(f"Sync total:             {time_sync:.6f} s\n")
        f.write(f"Threading total:        {time_threads:.6f} s\n")
        f.write(f"Multiprocessing total:  {time_procs:.6f} s\n")


if __name__ == "__main__":
    main()
