# tamaku
Tamaku game solver

## General information

I got this task during an interview, and I was amazed by it. So, here is my solution for this task.

Candidate must provide a source code and output file for large input file. 
Example large input file provided by a company, can be found in `data/large_data.zip`

The name of this game was changed following a deal with the company to share information about this task.

## Game rules

### Description

Pat and Mat are playing a game called Tamaku on their pocket calculator. The game begins
with a positive integer displayed on the calculator screen. Pat starts the game and then they
alternate their turns. At each turn:

1. A player computes how many 1s are in the binary representation of the integer d on the
display. E.g. for 17 it is two 1s because 17=b10001
2. The player picks up a positive integer k<d with exactly one 1 in its binary representation,
e.g. 8=b1000, and subtracts it from a number displayed on the calculator.
3. The player computes 1s in the binary representation of the new number. E.g.
17-8=9=b1001, which contains two 1s.
4. If the number of 1s in the former number and the new number differs, the player loose the
game. If the player can’t make any move, he looses the game.

Both players are pretty clever and play the game optimally. Still, there can be only one
winner. Can you determine who wins, if you know the starting number?

### Task

#### Input file

The first line of the input contains G, a number of games played. 0 < G < 10,000,000Then
follows G lines, each containing a starting integer 0 < N < 1,000,000,000.

Sample input:

```
7
1
2
3
10
17
47
999999999
```

#### Output file

For each game print PAT if the first player has winning strategy, otherwise print MAT.

Sample output (for the input provided above):

```
MAT
PAT
MAT
PAT
PAT
PAT
MAT
```

Explanation:

- In the first game, N=1 and Pat has no valid move, and looses.
- In the second game, N=2. Pat subtracts 1, and Mat looses the game.

#### Additional requirements

Solution and output file for [large_data.zip](./data/large_data.zip) is 
need to be provided within 2 hours.

## Solution

This is a new version, focused on simplicity and efficiency. It uses `multiprocessing` for utilization of all CPU 
cores and able to decompress input file if necessary.

### Initialization:

First initialize and activate virtual environment by 
following [instructions](https://docs.python.org/3/library/venv.html) or simply by running:

```shell
python -m virtualenv venv
```

and then (on Windows):

```shell
.\venv\Scripts\activate
```

then you need to install all dependencies by running:

```shell
pip install -r requirements-dev.txt
```

Personally I prefer to use `task` utility from https://taskfile.dev/ which is a very good replacement 
for Makefiles. If you have it you can run:

```shell
task environ
```

(I tested it on Windows, hope it would work on Linux too)

Once you will have all dependencies installed, you can install package itself by running (in virtual environment):

```shell
python setup.py develop
```

or (with help of `task` utility)

```shell
task develop-install
```

### Usage

You can run the application by using:

```shell
tamaku --input-file ./data/small_data.txt --output-file ./results/small_data.txt
```

Where:

- `tamaku` - is application itself
- `--input-file ./data/small_data.txt` - path to input file
- `--output-file ./results/small_data.txt` - path to output file

Optionally you can use `--processes-count <num_processes>` to specify how many processes will be used 
to process input file. if not specified all CPU cores would be used. 

In case if zip-compressed file will be provided as input file, tool will automatically 
decompress it in a temporary folder, process it and then delete temporary folder.

At the end of execution tool will generate information about execution time spent for file 
processing.

Example command line for big dataset:

```shell
tamaku --input-file ./data/large_data.zip --output-file ./results/large_data.txt
```

### Testing

To run tests please execute:

```shell
python -m pytest tests -vvv
```

Or just simply:

```shell
task tests
```

For coverage report generation please run:

```shell
python -m pytest tests -vvv --cov=tamaku
```

And then generate reports by using:

```shell
python -m coverage html
```

Or just use (I told you, `task` tool is just great):

```shell
task coverage
```

### Tuning and profiling

At the end of execution tool will generate information about time used for processing dataset 
excluding time for decompression (if it was necessary).

Example outputs:

- `Done @ 6.0m 35.93s - 10000000 tasks processed` (older version, executed on i7-3632QM with 32 GiB RAM)
- `Execution time 51 seconds and 656 milliseconds (10000000 tasks processed)` (i9-10885H with 64 GiB RAM)

If you would like to make it faster, you probably will focus on 
`tamaku.solver:solve_task` and `tamaku.solver:find_best_response`. You can tune it with help of 
[`timeit`](https://docs.python.org/3/library/timeit.html) module.

Example results (on i9-10885H):

```
$ python -m timeit --setup "from tamaku import solver" "solver.solve_task(789541776)
10000 loops, best of 5: 32.5 usec per loop
```

Hope you like it. Enjoy!
