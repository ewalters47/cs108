import sys


class Fraction:
    def __init__(self, numerator=0, denominator=1):

        if denominator == 0:
            raise ValueError('Invalid denominator: 0')

        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return '{0}/{1}'.format(self.numerator, self.denominator)


if __name__ == '__main__':

    while True:
        try:
            f = Fraction(int(input('numerator: ')), int(input('denominator: ')))
            print(f)
        except ValueError:
            print('Bad Fraction')
    print('Thanks for your valid input...')
    print(f)

