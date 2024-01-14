from tamaku import solver

from tests import datasets as test_datasets


def test_solver_for_small_dataset():
    for value, expected_result in test_datasets.SMALL_DATA_SET:
        solver_result = solver.solve_task(value)
        assert expected_result == solver_result,\
            f'Expected: {expected_result}. Got: {solver_result}. Input: {value}'


def test_solver_for_big_dataset():
    for value, expected_result in test_datasets.BIG_DATA_SET:
        solver_result = solver.solve_task(value)
        assert expected_result == solver_result,\
            f'Expected: {expected_result}. Got: {solver_result}. Input: {value}'


def test_move_suggester():
    test_cases = [
        (0b100, 0b10),
        (0b101, 0b10),
        (0b1011111, 0b0100000),
        (0b1010101, 0b0100000),
        (0b1000000, 0b0100000),
        (0b10001, 0b1000),
        (0b1, 0),
        (0b10, 1),
        (0b1111, 0),
    ]
    for value, expected_result in test_cases:
        result = solver.find_best_response(value)
        assert result == expected_result


def test_suggested_moves_produce_correct_results():
    test_cases = [
        0b100,
        0b101,
        0b1011111,
        0b1010101,
        0b1000000,
        0b10001,
    ]

    for value in test_cases:
        bin_value = bin(value)[2:]
        result = value - solver.find_best_response(value)
        bin_result = bin(result)[2:]
        assert bin_value.count("1") == bin_result.count("1")
