import base64
import os

from tamaku import support_funcs
from tests.helpers import hash_file


def test_decompressor_can_decompress_file(tmp_path):
    compressed_data = """
        UEsDBBQAAAAIAM+5IVglmkPeeAAAAIQAAAANAAAAdGVzdF9maWxlLnR4dPNIzcnJVyjPL8pJ0VPg
        5QpJLS5RSEksSVRIK8rPVUhJTc7PLShKLS7OzM/T4+Xi5bow/2LDhR0XNl2cdrFJ4WIjhAGUubDo
        wtaLjRebLuwDCSlc2HJhw4W9EMbui/0KQE37Lmy/sB8ouuti84VNIFmgfD9Qp4ICAFBLAQIUABQA
        AAAIAM+5IVglmkPeeAAAAIQAAAANAAAAAAAAAAAAIAAAAAAAAAB0ZXN0X2ZpbGUudHh0UEsFBgAA
        AAABAAEAOwAAAKMAAAAAAA==
    """

    input_zip_file = os.path.join(tmp_path, "test_file.zip")
    with open(input_zip_file, "wb") as output_file:
        decoded_data = base64.b64decode(compressed_data.encode("ascii"))
        output_file.write(decoded_data)

    decompressed_file_name = support_funcs.decompress_file(
        compressed_file_name=input_zip_file,
        output_dir=str(tmp_path)
    )

    assert os.path.basename(decompressed_file_name) == "test_file.txt"
    assert hash_file(decompressed_file_name) == "b6d503cc6a60b9e35a42582edcce613a185e4cb9"


def test_returns_expected_file_extension():
    test_data = [
        ("some_file.zip", ".zip"),
        ("/some/folder/in/path/some_file.zip", ".zip"),
        ("some_file.ZiP", ".ZiP"),
        ("non-compressed-file.txt", ".txt"),
        ("non-compressed-file.txt.gz", ".gz"),
    ]

    for file_name, expected_result in test_data:
        assert support_funcs.get_file_extension(file_name) == expected_result


def test_can_detect_compressed_files():
    test_data = [
        ("some_file.zip", True),
        ("/some/folder/in/path/some_file.zip", True),
        ("some_file.ZiP", True),
        ("non-compressed-file.txt", False),
    ]

    for file_name, expected_result in test_data:
        assert support_funcs.is_file_zipped(file_name) == expected_result
