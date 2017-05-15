# tamaku
Tamaku game solver

## General information

I got this task on interview for one company. And I was amazed by task. So, here is my solution of this task.

As a part of task candidate must provide source code and output file for large input file. Large input file provided by company.

Name of game was changed according to company requirements.


## Game rules

Pat and Mat are playing a game called GoRoKu on their pocket calculator. The game begins
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


## Task

**Input**

The first line of the input contains G, a number of games played. 0 < G < 10,000,000Then
follows G lines, each containing a starting integer 0 < N < 1,000,000,000.

**Output**

For each game print Pat if the first player has winning strategy, otherwise print Mat.

**Sample Input**

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

**Sample Output**

```
MAT
PAT
MAT
PAT
PAT
PAT
MAT
```

**Explanation**

In the first game, N=1 and Pat has no valid move, and looses.
In the second game, N=2. Pat subtracts 1, and Mat looses the game.

## Usage

### Solving input taks
If you just process input file use:

```
tamaku.py -i .\tasks\task_file.data
```

Where ```.\tasks\task_file.data``` path to your input task file. In this case program will read input file and then produce solutions to console.

### Solving input tasks and measuring execution time
If you want program to be a little bit more verbose, for example calculate execution time, you can use ```-v``` switch:

```
tamaku.py -v -i .\tasks\task_file.data
```

In this case, after all output lines, program will print information about execution time.

### Limiting output

In case when you developing new features and profiling program, you can set limit for output. In this case, program will be terminated when **<count>** solutions will be found. For example, if your file contains 10M tasks, you can solve just 100K tasks and measure execution time to predict time needed for 10M tasks.

Use ```-l <count>``` command line argument, where ```<count>``` your limit.

```
tamaku.py -l 3 -v -i .\tasks\task_file.data
```

In given example output will be limited to 3 lines.


### Only measure execution time, without results print

In case when you testing algorithm modifications you can use ```-n``` switch with ```-v``` switch

```
tamaku.py -n -l 3 -v -i .\tasks\task_file.data
```

In given example:

* ```-i .\tasks\task_file.data``` - input file ```.\tasks\task_file.data```
* ```-v``` - verbose output enabled
* ```-l 3``` - output limited to 3 lines
* ```-n```- output will not be printed to output console

In this case program ouput will be:

```
solving tasks
0.0s
```

So, program execution time is less than a second.