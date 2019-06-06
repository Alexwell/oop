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

    @staticmethod
    def sell_auto(label='BMW'):
        return f'{label} sealed'