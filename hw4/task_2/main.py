import math
import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def integrate_part(f, a, step, start_i, end_i):
    acc = 0.0
    for i in range(start_i, end_i):
        acc += f(a + i * step) * step
    return acc


def integrate(f, a, b, *, n_jobs=1, n_iter=10000000, executor="none"):
    step = (b - a) / n_iter

    if executor == "none":
        acc = 0.0
        for i in range(n_iter):
            acc += f(a + i * step) * step
        return acc

    chunk = n_iter // n_jobs
    ranges = []
    start = 0
    for j in range(n_jobs):
        end = start + chunk
        if j == n_jobs - 1:
            end = n_iter
        ranges.append((start, end))
        start = end

    Executor = ThreadPoolExecutor if executor == "threads" else ProcessPoolExecutor

    with Executor(max_workers=n_jobs) as ex:
        futures = [
            ex.submit(integrate_part, f, a, step, s, e)
            for (s, e) in ranges
        ]
        results = [f.result() for f in futures]
        return sum(results)


def best_time(f, a, b, *, n_jobs, n_iter, executor, repeats=2):
    best_time = None
    for _ in range(repeats):
        start_time = time.perf_counter()
        integrate(f, a, b, n_jobs=n_jobs, n_iter=n_iter, executor=executor)
        cur_time = time.perf_counter() - start_time
        if best_time is None or cur_time < best_time:
            best_time = cur_time
    return best_time


def main():
    cpu_num = os.cpu_count() or 1
    max_jobs = cpu_num * 2

    a = 0.0
    b = math.pi / 2

    n_iter = 10000000
    repeats = 2

    results = []
    for n_jobs in range(1, max_jobs + 1):
        time_threads = best_time(math.cos, a, b, n_jobs=n_jobs, n_iter=n_iter, executor="threads", repeats=repeats)
        time_processes = best_time(math.cos, a, b, n_jobs=n_jobs, n_iter=n_iter, executor="processes", repeats=repeats)

        results.append(f"n_jobs={n_jobs} | threads time: {time_threads:.6f}s | processes time: {time_processes:.6f}s")

    out_file = "../artifacts/task_2_results.txt"
    with open(out_file, "w") as f:
        f.write('\n'.join(results))


if __name__ == "__main__":
    main()
