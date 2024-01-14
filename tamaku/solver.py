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


def bohdan_solve_task(number: int) -> data_types.WinnerType:
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


def agobeaux_solve_task(number: int) -> data_types.WinnerType:
    '''
    Observations:
    1. To subract a number with only one '1' in its binary representation
    without changing the number of '1's in the original number,
    we need to find '10' patterns, as substracting '1' from them
    will give result '01'. This is the only possible pattern
    where we can get this.
    2. Thanks to 1, we see that there is no "smart" way to play.
    All operations will simply "move" the '1's to the right
    until it is not possible anymore.
    It is not possible anymore when we get a single stack of 1s
    with no 0 after it. In other words, when we get (2^k) - 1

    Solution:
    Count, for each one, how much it can move to the right
    0b001000 -> 3
    0b000001 -> 0
    0b010010 -> right '1' can move once, left '1' can move 3 times (3 zeroes).
    Sum all of those counts, and based on whether the number is even
    or odd, return the right answer.
    '''
    cnt_zeroes = 0
    ans = 0
    while number > 0:
        if number & 1 > 0:
            ans += cnt_zeroes
        else:
            cnt_zeroes += 1
        number >>= 1  # 'fancy' version of number /= 2
    if ans % 2 == 1:
        return data_types.WinnerType.PAT
    return data_types.WinnerType.MAT


def solve_task(number: int) -> data_types.WinnerType:
    """
    Takes a number and then computes which player would win for it.

    :param number: number which need to be tested.
    :return: name of a player who would win.
    """
    return agobeaux_solve_task(number)