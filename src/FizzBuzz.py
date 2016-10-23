class FizzBuzz:
    FIZZ = 'Fizz'
    BUZZ = 'Buzz'
    FIZZ_BUZZ = 'FizzBuzz'

    def __init__(self):
        return

    def calc(self, arg):
        if self.__isFizzBuzz(arg):
            return self.FIZZ_BUZZ

        if self.__isFizz(arg):
            return self.FIZZ

        if self.__isBuzz(arg):
            return self.BUZZ

        return arg

    def __isFizz(self, arg):
        return arg % 3 == 0

    def __isBuzz(self, arg):
        return arg % 5 == 0

    def __isFizzBuzz(self, arg):
        return self.__isFizz(arg) and self.__isBuzz(arg)
