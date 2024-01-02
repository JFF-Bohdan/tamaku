import datetime as dt
import shutil
import tempfile
import time

import click

import humanize

from loguru import logger

from tamaku import consts
from tamaku import file_processor
from tamaku import support_funcs


@click.command(name="tamaku")
@click.option("--input-file", required=True, help="Path to input file")
@click.option("--output-file", required=True, help="Path to output file")
@click.option("--chunk-size", default=consts.DEFAULT_CHUNK_SIZE, required=False, type=int, help="Processing chunk size")
def tamaku(input_file: str, output_file: str, chunk_size: int):
    logger.info("Application started")

    tmp_folder_name = None
    try:
        if support_funcs.is_file_zipped(input_file):
            tmp_folder_name = tempfile.mkdtemp(suffix="tmp-input-file", prefix="tamaku-")
            logger.info(f"Decompressing original file into temp folder {tmp_folder_name}")

            input_file = support_funcs.decompress_file(
                compressed_file_name=input_file,
                output_dir=tmp_folder_name
            )

        time_start = time.monotonic()
        processed_tasks_count = file_processor.process_file(
            input_file=input_file,
            output_file=output_file,
            chunk_size=chunk_size,
        )
        logger.debug(f"Processed tasks count: {processed_tasks_count}")
        time_end = time.monotonic()

        human_readable_execution_time = humanize.precisedelta(
            dt.timedelta(seconds=time_end - time_start),
            minimum_unit="milliseconds"
        )
        logger.info(f"Execution time {human_readable_execution_time} ({processed_tasks_count} tasks processed)")

    finally:
        if tmp_folder_name:
            logger.info(f"Removing temp folder {tmp_folder_name}")
            shutil.rmtree(
                tmp_folder_name,
                ignore_errors=False
            )

    logger.info("Application finished")
