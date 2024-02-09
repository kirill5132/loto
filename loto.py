import random



def generate_barrels():
    barrels = list(range(1, 91))
    random.shuffle(barrels)
    return barrels



def play_lotto():
    barrels = generate_barrels()

    while barrels:
        input("Нажмите Enter для вытягивания бочонка...")
        barrel = barrels.pop()
        print(f"Вытянут бочонок: {barrel}")

    print("Все бочонки вытянуты!")


if __name__ == "__main__":
    play_lotto()