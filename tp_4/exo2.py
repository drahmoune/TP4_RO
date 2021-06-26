import numpy as np

#11111111111111111


def check_v_stochatique(v):
    if sum(v) == 1:
        return True
    else:
        return False

#  2


def check_mtr_caree(mtr):
    for v in mtr:
        if len(v) != len(mtr):
            return False
        else:
            continue
    return True


def check_mtr_stochatique(mtr):
    caree = check_mtr_caree(mtr)
    if caree == False:
        return IndexError("Matrice n'est pas carée")
    for v in mtr:
        if check_v_stochatique(v) == False:
            return False
        else:
            continue
    return True

# question 3


def power_of_mtr(mtr, power):
    if check_mtr_caree(mtr) == False:
        return IndexError("Matrice non carée")
    if check_mtr_stochatique(mtr) == False:
        return IndexError("Matrice non stochatique")

    np_matrice = np.array(mtr)
    powered = np.linalg.matrix_power(np_matrice, power)

    return powered