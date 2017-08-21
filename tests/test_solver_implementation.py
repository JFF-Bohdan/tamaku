from solver.solver_impl import find_best_step, game_result_to_string, play_game_bool


def test_solver_implementation_by_fixture():
    with open("./tests/valid_output_fixture.txt", "rt") as file:
        for line in file:
            if line is None:
                break

            str(line).strip()
            if len(line) == 0:
                continue

            task = [str(item).strip() for item in line.split() if len(str(item).strip()) > 0]
            assert len(task) == 2

            assert str(task[0]).isnumeric()
            value = int(task[0])

            assert game_result_to_string(play_game_bool(value)) == task[1]


def test_solver_low_level_func():
    assert find_best_step(17) == 8
