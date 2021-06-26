import random as ra



def throw_dice():
    return ra.randint(1, 6)



def throw_dice_times(n):
    throws = []
    for time in range(n):
        throw = throw_dice()
        throws.append(throw)
    return throws



def count_six(throws):
    return throws.count(6)


def throw_coin():
    return ra.randint(0, 1)


def throw_coin_times(n):
    throws = []
    for time in range(n):
        throw = throw_coin()
        throws.append(throw)
    return throws


def count_heads(throws):
    return throws.count(0)



def random_exp():
    throws = 0

    while True:
        throw = throw_dice()
        print(throw)
        throws += 1
        if throw == 6:
            break

    print('on a obtenu un 6 après ' + str(throws) + ' tentatives')


def main():
    running = True

    while (running):

        question = 0
        while question not in [1, 2, 3, 4]:
            print(
                "\nPour un simple lancer, choisir 1.\nPour multiple lancer, choisir 2.\nPour Une expérience aléatoire, choisir 3.\nPour un tirage de pile ou face, choisir 4.\n")
            try:
                question = int(input())
                if question not in [1, 2, 3, 4]:
                    raise Exception('invalid choice')
            except:
                print('Choix invalide\n')
                question = 0

        if question == 1:
            print("\n")
            print("On a obtenu : ", throw_dice())
        elif question == 2:
            try:
                times = int(input('\nCombien de fois voulez-vous lancer le dé ? '))
            except:
                times = 1

            throws = throw_dice_times(times)
            print(throws)

            print("\nnombre de fois où on obtient le nombre 6 : ", count_six(throws))

        elif question == 3:
            print('\nles résultats obtenu : ')
            random_exp()
        else:
            try:
                times = int(input('Combien de fois voulez-vous lancer la pièce ?\n'))
            except:
                times = 1

            throws = throw_coin_times(times)

            print('les résultats obtenu : ')
            print(throws)

            print("\nnombre de fois où on obtient face (pile -> 1, face ->0) : ", count_heads(throws))

        print('\nRéesayer ? [O/N]')
        x = input()
        running = x in ['o', 'O']


main()