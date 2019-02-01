"""
Simple Python progress bar utility that works in any type of loop.
"""
import sys


class ProgressBar:
    """
    Class for a simple unicode progress bar.
    """
    def __init__(self, iterations: int, **kwargs) -> None:
        if 'prefix' not in kwargs:
            kwargs['prefix'] = "Progress"
        if 'iteration' not in kwargs:
            kwargs['iteration'] = 0
        if 'fill_char' not in kwargs:
            kwargs['fill_char'] = '█'
        if 'length' not in kwargs:
            kwargs['length'] = 60

        self.__iterations = iterations
        self.__prefix = kwargs['prefix']
        self.__iteration = kwargs['iteration']
        self.__fill = kwargs['fill_char']
        self.__length = kwargs['length']

        if ('rank' in kwargs and 'size'
                not in kwargs) or ('size' in kwargs and 'rank' not in kwargs):
            raise Exception("If using MPI must pass rank and size.")

        if 'rank' in kwargs:
            self.__rank = kwargs['rank']
            self.__prefix += f" (process {self.__rank})"
            self.__size = kwargs['size']

    def reset(self):
        """
        Reset the number of iterations that have been performed to 0.
        """
        self.__iteration = 0

    def done(self):
        print()

    def update(self, increment: int = 1) -> None:
        """
        Updates the progress bar by incrementing the current iteration by
        increment. Requires increment >= 1.

        Params:
        -------
        increment: int
            The increment by which to increase the progress bar.
        """
        self.__iteration += increment
        percent = self.__iteration / float(self.__iterations) * 100
        fill_length = int(self.__length * self.__iteration // self.__iterations)

        self.__print_progress(percent, fill_length)

    def __print_progress(self, percent: float, filled_length: int) -> None:
        fill = self.__fill * filled_length + " " * (self.__length -
                                                    filled_length)

        pbar = f"\r{self.__prefix}: |{fill}| {percent: .1f}%"

        for _ in range(self.__rank):
            print()
        print(pbar, end="")
        sys.stdout.flush()

        for _ in range(self.__rank):
            sys.stdout.write('\x1b[1A')
            sys.stdout.flush()
