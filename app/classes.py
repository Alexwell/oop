class Automobile(object):
    def __init__(self, color='black', doors=5):
        self.color = color
        self.doors = doors

    label = 'BMW'
    wheels = 4
    engine = 'gas'

    def __repr__(self):
        return f'color: {self.color},\ndoors: {self.doors},\nlabel: {self.label},\n' \
            f'wheels: {self.wheels},\nengine: {self.engine}'


class Salon(object):
    auto_list = [
        'BMW',
        'AUDI',
        'PORSCHE'
    ]

    @classmethod
    def view_list(cls):
        print(cls.auto_list)

    @classmethod
    def sell_auto(cls, label='BMW'):
        if label in cls.auto_list:
            return f'{label} sold'
        else:
            return 'Wrong model'

    @staticmethod
    def convert_price(price=100, tax=2.2):
        return price * tax


class Book(object):
    def __init__(self, author='Some author', book_name='Some book', year=2019, genre='CS'):
        self.author = author
        self.book_name = book_name
        self.year = year
        self.genre = genre

    def __repr__(self):
        return f'<author: {self.author}, book_name: {self.book_name}>'

    def __str__(self):
        return f'This is {self.book_name}'

    def __eq__(self, other):
        return self.year == other.year or self.book_name == other.book_name

    def __ne__(self, other):
        return not self.__eq__(other)


