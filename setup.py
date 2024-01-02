import codecs
import copy
import os
from importlib.machinery import SourceFileLoader

from setuptools import find_packages, setup

module_name = "tamaku"

# Probably module is not installed yet (or different version is available)
# Considering this, it would be better to load __init__.py by machinery
module = SourceFileLoader(
    module_name, os.path.join(module_name, "__init__.py")
).load_module()


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))

    res = []
    for line in lineiter:
        if line.startswith("#"):
            continue

        split_data = [str(item) for item in line.split(" ") if str(item).strip()]
        if not split_data:
            continue

        if split_data[0] == "-r":
            continue

        res.append(line)

    return res


def load_file_content(file_name, encoding="utf-8") -> str:
    with codecs.open(file_name, "r", encoding=encoding) as input_file:
        return input_file.read()


requirements = parse_requirements("requirements.txt")

extra_requirements = copy.deepcopy(requirements)
extra_requirements.extend(parse_requirements("requirements-dev.txt"))


setup(
    name=module_name,
    version=module.__version__,
    author=module.__author__,
    license=load_file_content("LICENSE"),
    description="App to solve Tamaku task",
    long_description=open("README.md").read(),
    keywords=["Calculations", "Algorithm"],
    url="https://github.com/",
    platforms="all",
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: Linux",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython"
    ],
    python_requires=">=3.6",
    packages=find_packages(exclude=["tests", "dev_doc", "doc"]),
    install_requires=requirements,
    extras_require={"dev": extra_requirements},
    include_package_data=True,

    entry_points={
        "console_scripts": [
            "tamaku = tamaku.scripts.cli:tamaku",
        ],
    },
)
