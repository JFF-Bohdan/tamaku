from tamaku import data_types


def find_best_response(value: int) -> int:
    """
    Returns best solution for a given value. For example for 17=b10001 it would respond with 8=b1000.
    If not response available it would return zero.

    :param value: a value which need to be a tested
    :return: the best response or 0 when no response available.
    """
    bin_value = bin(value)[2:]
    zero_position = bin_value.find("0")
    if zero_position == -1:
        return 0

    return 1 << len(bin_value) - zero_position - 1


def solve_task(number: int) -> data_types.WinnerType:
    """
    Takes a number and then computes which player would win for it.

    :param number: number which need to be tested.
    :return: name of a player who would win.
    """
    won_games_count = 0
    while True:
        # looking for the best solution for a current task
        bst = find_best_response(number)
        if not bst:
            break

        # computing new number which need to be tested
        number -= bst
        won_games_count += 1

    won_games_count = won_games_count % 2 == 1
    return data_types.WinnerType.PAT if won_games_count else data_types.WinnerType.MAT
