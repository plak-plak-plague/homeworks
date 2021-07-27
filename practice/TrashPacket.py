class Trash:
    def __init__(self, capacity):
        self.MYNAME = 'Trash'
        self.capacity = capacity
        self.insiders = []

    def add(self, obj):
        if self.capacity - obj.length < 0:
            print('In {} no free space to this. Free space - {}'.format(self.MYNAME, self.capacity))
        else:
            self.insiders.append(obj)
            self.capacity -= obj.length
            print(obj.name, 'add to {}. Free space in trash box - {}'.format(self.MYNAME, self.capacity))

    def show(self):
        print('In {} box: '.format(self.MYNAME), end='')
        for i in self.insiders:
            print(i.name, end=', ')
        print()

class Packet(Trash):
    def __init__(self, capacity):
        super(Packet, self).__init__(capacity)
        self.MYNAME = 'Packet'

class Bottle:
    def __init__(self, name, length):
        self.name = name
        self.length = length
class Papers(Bottle):
    pass


t1 = Trash(20)
t1.add(Bottle('Coca-cola 1l', 5))
t1.add(Papers('Fashion Magazines', 8))
t1.add(Bottle('Sprite 1.5l', 7))
t1.add(Bottle('Fanta 0.5', 3))
t1.show()

p1 = Packet(10)
p1.add(Bottle('Sprite 2L', 9))
p1.add(Papers('Science Book', 4))
p1.show()

