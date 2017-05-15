"""
Stopwatch class implementation
"""
import time


class Stopwatch:
    """
    Calculates work time
    """

    def __init__(self,
                 auto_start=False,
                 interval_print=False,
                 reset_timer_on_interval_print=False):
        """
        :param auto_start: if True when need start time measure immediately
        :param interval_print: True when time-interval print available
        :param reset_timer_on_interval_print: True when need reset timer on interval print
        """
        self.start_at = 0
        self.stop_at = 0
        self.interval_print = interval_print
        self.prefix = "DONE at "
        self.reset_timer_on_interval_print = reset_timer_on_interval_print

        if auto_start:
            self.start()

    def running(self):
        """
        Returns True when stopwatch running
        :return: True when running, otherwise False
        """
        return self.start_at > 0

    def stopped(self):
        """
        Returns True when timer stopped
        :return: True when stopped, otherwise False
        """
        return self.stop_at > 0

    def start(self):
        """
        Starts timer
        :return: None
        """
        self.start_at = time.time()
        self.stop_at = 0

    def stop(self):
        """
        Stops timer
        :return: None
        """
        self.stop_at = time.time()

    def secs(self):
        """
        Returns elapsed seconds count from previous timer start
        :return:
        """
        return round(self.stop_at - self.start_at, 2)

    def interval_sec(self):
        """
        Returns elapsed seconds count from start to CURRENT moment
        :return:
        """
        ret_value = round((time.time() - self.start_at), 2)
        if self.reset_timer_on_interval_print:
            self.start()

        return ret_value

    @staticmethod
    def print_seconds_nice(seconds, prefix=""):
        """
        Static method for interval print in human readable format
        :param seconds: seconds count
        :param prefix: prefix for print
        :return: string which contains human readable representation of interval
        """
        if seconds < 60:
            return "{}{}s".format(prefix, seconds)

        minutes = seconds // 60
        seconds -= minutes * 60

        if minutes < 60:
            seconds = round(seconds, 2)
            return "{}{}m {}s".format(prefix, minutes, seconds)

        hours = minutes // 60
        minutes -= hours * 60

        if hours < 24:
            minutes = int(minutes)
            seconds = round(seconds, 2)
            return "{}{}h {}m {}s".format(prefix, hours, minutes, seconds)

        days = hours // 24
        hours -= days * 24

        seconds = round(seconds, 2)
        return "{}{}d {}h {}m {}s".format(prefix, days, hours, minutes, seconds)

    def __str__(self):
        if self.interval_print:
            seconds = round(self.interval_sec(), 2)
        else:
            seconds = round(self.secs(), 2)

        return Stopwatch.print_seconds_nice(seconds)
