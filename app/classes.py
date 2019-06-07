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
    def __init__(self, author='Some author', book_name='Some book', year=2019, genre='CS', review_list=[]):
        self.author = author
        self.book_name = book_name
        self.year = year
        self.genre = genre
        self.review_list = review_list

    def __repr__(self):
        return f'<author: {self.author}, book_name: {self.book_name}>'

    # def __str__(self):
    #     comments = '\n'.join(map(str, self.review_list))
    #     return f'This is {self.book_name}\nreview: {self.review_list}' + comments

    def __str__(self):
        comments = []
        for i in self.review_list:
            comments.append(i.review_author)
            comments.append(i.review_text)
        return f'This is {self.book_name}\nreview: {str(comments)}'

    def __eq__(self, other):
        return self.year == other.year or self.book_name == other.book_name

    def __ne__(self, other):
        return not self.__eq__(other)


class ReviewBook(object):
    def __init__(self, review_author='some author', review_text='some review text'):
        self.review_author = review_author
        self.review_text = review_text

    def __str__(self):
        return f'review author: {self.review_author}\nreview text: {self.review_text}'


class Temperature(object):
    def __init__(self):
        self._temperature_value = 20

    def get_temperature_value(self):
        return self._temperature_value

    def set_temperature_value(self, value=20):
        self._temperature_value = value

    def del_temperature_value(self):
        del self._temperature_value


class TemperatureWithProperties(object):
    def __init__(self):
        self._temperature_value = 20

    @property
    def temperature_value(self):
        return self._temperature_value

    @temperature_value.setter
    def temperature_value(self, value):
        self._temperature_value = value

    @temperature_value.deleter
    def temperature_value(self):
        del self._temperature_value

    def to_fahr(self):
        return (self.temperature_value * 1.8) + 32

    def to_celcius(self):
        return (self.temperature_value - 32) / 1.8
