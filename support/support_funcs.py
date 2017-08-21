import os
import zipfile


def print_seconds_nice(seconds, prefix=""):
    """
    Static method for interval print in human readable format
    :param seconds: seconds count
    :param prefix: prefix for print
    :return: string which contains human readable representation of interval
    """
    if seconds < 60:
        return "{}{}s".format(prefix, seconds)

    minutes = seconds // 60
    seconds -= minutes * 60

    if minutes < 60:
        seconds = round(seconds, 2)
        return "{}{}m {}s".format(prefix, minutes, seconds)

    hours = minutes // 60
    minutes -= hours * 60

    if hours < 24:
        minutes = int(minutes)
        seconds = round(seconds, 2)
        return "{}{}h {}m {}s".format(prefix, hours, minutes, seconds)

    days = hours // 24
    hours -= days * 24

    seconds = round(seconds, 2)
    return "{}{}d {}h {}m {}s".format(prefix, days, hours, minutes, seconds)


def get_file_extension(file_name):
    _, file_extension = os.path.splitext(file_name)
    return file_extension


def is_file_zipped(file_name):
    return str(get_file_extension(file_name)).lower() == ".zip"


def decompress_file(compressed_file_name, tmp_path):
    with zipfile.ZipFile(compressed_file_name, "r") as archive:
        compressed_filename = archive.filelist[0].filename

        archive.extract(compressed_filename, tmp_path)

        return os.path.abspath(os.path.join(tmp_path, compressed_filename))
