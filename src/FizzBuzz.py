class FizzBuzz:

    def __init__(self):
        return

    def calc(self, arg):
        if arg % 3 == 0 and arg % 5 == 0:
            return 'FizzBuzz'

        if arg % 3 == 0:
            return 'Fizz'

        if arg % 5 == 0:
            return 'Buzz'

        return arg
