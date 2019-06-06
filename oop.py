from app.classes import Automobile, Salon, Book


def main():
    # my_auto_1 = Automobile('red', 5)
    # my_auto_2 = Automobile(doors=7)
    #
    # print(my_auto_1)
    # print(my_auto_2)
    # Salon.view_list()
    #
    # sold = Salon.sell_auto('PORSCHE')
    # price = Salon.convert_price(200, 27)
    # print(price)
    # print(sold)

    b1 = Book()
    b2 = Book('Pushkin', 'Onegin', 1845, 'Poetry')
    b3 = Book('Lermontov', 'Hero of our time', 1845, 'Poetry')

    print(b1)
    print(b1.__repr__())

    print(b2)
    print(b2.__repr__())

    print(b2.__eq__(b1), b2.__ne__(b1))
    print(b2.__eq__(b3), b2.__ne__(b3))


if __name__ == '__main__':
    main()
