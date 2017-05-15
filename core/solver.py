from system.shared import LastErrorHolder
import codecs


class ProblemSolver(LastErrorHolder):
    """
    Problem solver for GoRoKu game
    """
    def __init__(self):
        super().__init__()

        # input file name
        self.file_name = None

        # total games count which must be processed
        self.games_count = None

        # file object
        self._file = None

        # program can print some output in verbose mode
        self.verbose_mode = False

        # if True program will not print result, it's can be useful for time measurement
        self.not_print_result = False

        # limit for output
        self.limit_output = None

    def _read_games_count(self):
        """
        Reads games count
        :return: True when success, otherwise False
        """
        s = self._file.readline()
        if s is None:
            return self.setError("can't read tasks count: empty input")

        s = str(s).strip()
        if not str(s).isnumeric():
            return self.setError("wrong format for games count, value '{}' is incorrect".format(s))

        self.games_count = int(s)

        return True

    def _scan_lines(self):
        """
        Scans lines from input file and returns for further processing
        :return:
        """
        qty = self.games_count
        while qty:
            s = self._file.readline()
            s = s.strip()

            if not str(s).isnumeric():
                self.setError("Error converting '{}' to int".format(s))
                return

            yield int(s)
            qty -= 1

    def _play_game_fast(self, task):
        """
        Solves one task for game
        :param task:
        :return:
        """

        winned_games_count = 0
        while True:
            # looking for best solution for current task
            bst = self.__find_best(task)
            if bst is None:
                break
            task = task - bst
            winned_games_count += 1

        return winned_games_count % 2 == 1

    def _process_games(self):
        if self.limit_output is not None:
            index = 0

        for task in self._scan_lines():
            # looking for game result (PAT vs MAT)
            res = self._play_game_fast(task)

            if not self.not_print_result:
                if res:
                    print("PAT")
                else:
                    print("MAT")

            # checking for output limitations
            if self.limit_output is not None:
                index += 1

                if index >= self.limit_output:
                    break

        return True

    def __find_best(self, v):
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

    def process(self):
        """
        Processes file and solves all problems
        :return: True if processing was successful, otherwise False
        """
        assert self.file_name is not None
        assert self.__find_best(17) == 8

        try:
            self._file = codecs.open(self.file_name, "r", "utf-8")

            try:
                if not self._read_games_count():
                    return False

                assert self.games_count is not None

                super().clearError()

                if self.verbose_mode:
                    print("solving tasks")

                if not self._process_games():
                    return False

            finally:
                self._file.close()

        except Exception as e:
            return self.setError(e)

        return True
