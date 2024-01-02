import typing


def yield_ints_from_stream(stream: typing.IO):
    for line in stream:
        yield int(line)
