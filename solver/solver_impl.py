def find_best_step(v):
    """
    Returns best solution for given value
    :param v: value
    :return: best solution or None when no any solutions available
    """
    s = bin(v)[2:]
    r = s.find("0")

    l = len(s) - r
    if (r == -1) or ((l - 1) < 0):
        return None

    return 1 << (l - 1)


def play_game_bool(task):
    """
    Solves one task for game
    :param task:
    :return:
    """

    win_games_count = 0
    while True:
        # looking for best solution for current task
        bst = find_best_step(task)
        if bst is None:
            break

        task -= bst
        win_games_count += 1

    return win_games_count % 2 == 1


def game_result_to_string(result):
    return "PAT" if result else "MAT"
