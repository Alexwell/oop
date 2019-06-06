from app.classes import Automobile, Salon


def main():
    my_auto_1 = Automobile('red', 5)
    my_auto_2 = Automobile(doors=7)

    # print(my_auto_1)
    # print(my_auto_2)

    # print(Salon.auto_list)

    Salon.view_list()

    sealed = Salon.sell_auto('PORSCHE')

    print(sealed)


if __name__ == '__main__':
    main()
