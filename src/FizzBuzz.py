class FizzBuzz:
    FIZZ = 'Fizz'
    BUZZ = 'Buzz'
    FIZZ_BUZZ = 'FizzBuzz'

    def __init__(self):
        return

    def calc(self, arg):
        if arg % 3 == 0 and arg % 5 == 0:
            return self.FIZZ_BUZZ

        if arg % 3 == 0:
            return self.FIZZ

        if arg % 5 == 0:
            return self.BUZZ

        return arg
