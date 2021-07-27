from math import sqrt


class Constructor:
    def __init__(self, numbers):
        self.numbers = numbers
        self.length = len(numbers)

    def check_count(self):
        check_dict = {1: self.square, 2: self.rectangle, 3: self.triangle, 4: self.polygon}
        if self.length in check_dict:
            check_dict[self.length](self.numbers)
        else:
            print('Invalid number!')

    def square(self, lines):
        a = int(lines[0])
        S = a ** 2
        P = 4 * a
        print('Area of square - {}, Perimeter - {}'.format(S, P))

    def rectangle(self, lines):
        a, b = int(lines[0]), int(lines[1])
        S = a * b
        P = (a + b) * 2
        print('Area of square - {}, Perimeter - {}'.format(S, P))

    def triangle(self, lines):
        a, b, c = lines
        if a + b > c and a + c > b and b + c > a:
            P = a + b + c
            p = P / 2
            S = sqrt(p * (p - a) * (p - b) * (p - c))

            print('Area of square - {}, Perimeter - {}'.format(S, P))
            return
        print('This triangle not exist!')

    def polygon(self, lines):
        a, b, c, d = lines

        m = max(lines)
        lines.pop(lines.index(m))


        if m < sum(lines):
            P = a + b + c + d
            p = P / 2
            S = sqrt((p - a) * (p - b) * (p - c) * (p - d))

            print('Area of square - {}, Perimeter - {}'.format(S, P))
            return
        print('This polygon not exist!')

    # def computation(self):
    #     pass


def ask():
    ret = []

    tempString = input('Paste numbers per space: ')
    tempString = tempString.split(' ')
    # print(type(tempString[0]))

    try:
        for i in tempString:
            ret.append(int(i))

    except Exception as e:
        print('You input string. Try again!')
        ask()

    # print(type(ret[0]))
    return ret


def main():
    lines = ask()
    c = Constructor(lines)
    c.check_count()


main()
