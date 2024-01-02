import hashlib


def hash_file(file_name: str, buff_size: int = 64 * 1024) -> str:
    hasher = hashlib.sha1()
    with open(file_name, "rb") as file_object:
        while True:
            data = file_object.read(buff_size)
            if not data:
                break

            hasher.update(data)

        return hasher.hexdigest()
