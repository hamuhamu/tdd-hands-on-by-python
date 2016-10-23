class FizzBuzz:
    FIZZ = 'Fizz'
    BUZZ = 'Buzz'
    FIZZ_BUZZ = 'FizzBuzz'

    def __init__(self):
        return

    def calc(self, arg):
        if arg % 3 == 0 and arg % 5 == 0:
            return self.FIZZ_BUZZ

        if self.__isFizz(arg):
            return self.FIZZ

        if self.__isBuzz(arg):
            return self.BUZZ

        return arg

    def __isFizz(self, arg):
        return arg % 3 == 0;

    def __isBuzz(self, arg):
        return arg % 5 == 0;
