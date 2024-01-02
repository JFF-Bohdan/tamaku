import os
import zipfile


def get_file_extension(file_name: str) -> str:
    """
    Returns file extension

    :param file_name: full file name / path
    :return: file extension
    """
    _, file_extension = os.path.splitext(file_name)
    return file_extension


def is_file_zipped(file_name: str) -> bool:
    """
    Returns true if file is compressed with zip
    :param file_name: path to a file
    :return: True if file is compressed with zip
    """
    return str(get_file_extension(file_name)).lower() == ".zip"


def decompress_file(compressed_file_name: str, output_dir: str) -> str:
    """
    Decompresses first file from archive. Return path to a decompressed file.

    :param compressed_file_name: path to a compressed file.
    :param output_path: output directory name.
    :return: path to decompressed file.
    """
    with zipfile.ZipFile(compressed_file_name, "r") as archive:
        compressed_filename = archive.filelist[0].filename
        archive.extract(compressed_filename, output_dir)

        return os.path.abspath(os.path.join(output_dir, compressed_filename))
