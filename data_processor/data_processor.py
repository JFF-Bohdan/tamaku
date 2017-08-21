import mmap
import multiprocessing
import time
from multiprocessing import Pool

from solver.solver_impl import game_result_to_string, play_game_bool

from support.support_funcs import print_seconds_nice


def process_data(input_file, output, can_print_results, limit=None, verbose=False):
    with open(input_file, "rt") as file:
        tm_begin = None
        if verbose:
            tm_begin = time.time()

        m = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)

        tasks_count = m.readline()
        tasks_count = int(str(tasks_count.decode("ascii")).strip())
        if limit is not None:
            tasks_count = min(tasks_count, limit)

        tasks = tasks_count * [None]
        assert len(tasks) == tasks_count

        for index, _ in enumerate(range(tasks_count)):
            line = m.readline().decode("ascii")
            tasks[index] = int(line)

        assert len(tasks) == tasks_count

    if verbose:
        delta = round(time.time() - tm_begin, 3)
        msg = print_seconds_nice(delta, "file loaded @ ")
        output.write("data loaded @ {}\n".format(msg))

    if verbose:
        output.write("cpu count: {}\n".format(multiprocessing.cpu_count()))

    pool = Pool(processes=multiprocessing.cpu_count())

    results = pool.map(play_game_bool, tasks)
    assert len(results) == tasks_count

    if can_print_results:
        for result in results:
            output.write(game_result_to_string(result) + "\n")

    return len(results)
