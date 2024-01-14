import itertools
import multiprocessing as mp
import typing

from loguru import logger

from tamaku import consts
from tamaku import data_types
from tamaku import file_reader
from tamaku import solver


def chunks(iterable: typing.Iterable, size: int) -> typing.Generator:
    it = iter(iterable)
    chunk = tuple(itertools.islice(it, size))
    while chunk:
        yield chunk
        chunk = tuple(itertools.islice(it, size))


def chunk_processor(chunk: typing.Iterable[int]) -> typing.Iterable[data_types.WinnerType]:
    return [solver.solve_task(item) for item in chunk]


def process_stream(
    input_stream, output_stream: typing.IO,
    chunk_size: int = consts.DEFAULT_CHUNK_SIZE,
    processes_count: typing.Optional[int] = None,
) -> int:
    processes_count = processes_count if processes_count else mp.cpu_count()
    logger.debug(f"CPU cores count which would be used is {processes_count}")
    logger.debug(f"Chunk size would be {chunk_size}")

    tasks_count = input_stream.readline()
    tasks_count = int(tasks_count)
    tasks_generator = chunks(
        itertools.islice(
            file_reader.yield_ints_from_stream(
                input_stream
            ),
            0,
            tasks_count
        ),
        size=chunk_size
    )

    pool = mp.Pool(processes=processes_count)
    results_generator = pool.map(chunk_processor, tasks_generator)

    results_count = 0
    for _, chunk_data in enumerate(results_generator):
        output_stream.write("\n".join(chunk_data))
        output_stream.write("\n")
        results_count += len(typing.cast(typing.Sized, chunk_data))

    logger.debug(f"Tasks count: {tasks_count}, results count: {results_count}")
    return results_count


def process_file(
    input_file: str,
    output_file: str,
    chunk_size: int = consts.DEFAULT_CHUNK_SIZE,
    processes_count: typing.Optional[int] = None
) -> int:
    logger.debug(f"Input file: {input_file}")
    logger.debug(f"Output file: {output_file}")

    with (
        open(input_file, "rt") as input_stream,
        open(output_file, "wt") as output_stream
    ):
        return process_stream(
            input_stream=input_stream,
            output_stream=output_stream,
            chunk_size=chunk_size,
            processes_count=processes_count
        )
