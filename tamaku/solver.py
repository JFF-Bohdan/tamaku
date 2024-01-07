from tamaku import data_types


def find_best_response(value: int) -> int:
    """
    Returns best solution for a given value. For example for 17=b10001 it would respond with 8=b1000.
    If not response available it would return zero.

    :param value: a value which need to be a tested
    :return: the best response or 0 when no response available.
    """

    # Above algorithm would have use of bits manipulation. And can be represented on high level as
    #
    #     bin_value = bin(value)[2:]  # noqa
    #     zero_position = bin_value.find("0")  # noqa
    #     if zero_position == -1:  # noqa
    #         return 0  # noqa
    #
    #     return 1 << len(bin_value) - zero_position - 1  # noqa
    #
    # Considering bits manipulation to calculate shift value, it would be approximately
    # two times faster than implementation used as example

    # Calculating bit length of given value to generate mask.
    # For example for 11010 bit length would be 5.
    bit_length = value.bit_length()

    # Now calculating bit mask, which would have every bit set
    # for bits length of initial value.
    # For example if bits length is 5 mask would be 11111 (exactly five set bits).
    mask = (1 << bit_length) - 1

    # Xoring initial value with provided mask. By doing this we would invert all
    # bits in initial value.
    # For example, if initial value is 11010 mask would be 11111 and result
    # would be 00101 which basically is 101
    value = value ^ mask

    # Computing bits length of inverted value which for 101 would be 3
    max_bit = value.bit_length()

    # If we don't have any 1 in inverted value, this would mean that there
    # was no 0s in initial value. In this case we just need to exit
    if max_bit == 0:
        return 0

    # Computing result as single bit set for bits length of inverted initial value
    # For example, if initial value was 11010 here we would return 100
    return 1 << max_bit - 1


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
