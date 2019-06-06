from app.classes import Automobile, Salon


def main():
    my_auto_1 = Automobile('red', 5)
    my_auto_2 = Automobile(doors=7)

    print(my_auto_1)
    print(my_auto_2)
    Salon.view_list()

    sold = Salon.sell_auto('PORSCHE')
    price = Salon.convert_price(200, 27)
    print(price)
    print(sold)


if __name__ == '__main__':
    main()
