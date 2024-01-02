import os

from tamaku import data_types
from tamaku import file_processor

from tests import datasets as test_datasets
from tests.helpers import hash_file


def generate_input_file(
    file_name: str,
    dataset: list[tuple[int, data_types.WinnerType]]
) -> None:
    with open(file_name, "wt") as output:
        output.write(f"{len(dataset)}\n")

        for value, _ in dataset:
            output.write(f"{value}\n")


def generate_expected_output_file(
        file_name: str,
        dataset: list[tuple[int, data_types.WinnerType]]
):
    with open(file_name, "wt") as output:
        for _, expected_result in dataset:
            output.write(f"{expected_result}\n")


def files_identical(file1, file2: str) -> bool:
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)

    return hash1 == hash2


def test_can_process_small_dataset(tmp_path):
    input_file_name = os.path.join(tmp_path, "input_file.txt")
    generate_input_file(input_file_name, test_datasets.SMALL_DATA_SET)

    output_file_name = os.path.join(tmp_path, "output_file.txt")

    expected_output_file_name = os.path.join(tmp_path, "expected_output_file.txt")
    generate_expected_output_file(
        expected_output_file_name,
        test_datasets.SMALL_DATA_SET
    )

    file_processor.process_file(
        input_file=input_file_name,
        output_file=output_file_name,
    )

    assert files_identical(output_file_name, expected_output_file_name) == True


def test_can_process_big_dataset(tmp_path):
    input_file_name = os.path.join(tmp_path, "input_file.txt")
    generate_input_file(input_file_name, test_datasets.BIG_DATA_SET)

    output_file_name = os.path.join(tmp_path, "output_file.txt")

    expected_output_file_name = os.path.join(tmp_path, "expected_output_file.txt")
    generate_expected_output_file(
        expected_output_file_name,
        test_datasets.BIG_DATA_SET
    )

    file_processor.process_file(
        input_file=input_file_name,
        output_file=output_file_name,
    )

    assert files_identical(output_file_name, expected_output_file_name) == True
