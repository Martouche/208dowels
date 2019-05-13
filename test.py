#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from math import *


def usage():
    _h = open("h_file.txt", "r")
    _array = _h.read().split('\n')
    for _line in _array:
        print (_line)


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def check_input():
    check_total = 0
    for i in range(1, len(sys.argv)):
        if is_int(sys.argv[i]) is False and is_float(sys.argv[i]) is False:
            print("Error: {} is not a number.".format(sys.argv[i]))
            exit(84)
        if int(sys.argv[i]) < 0:
            print("Error: All values must be 0 when number of values is Zero.")
            exit(84)
        check_total += int(sys.argv[i])
    if check_total != 100:
        print("Error: All values does not equal to 100.")
        exit(84)
    return 0


def param_loi_binomial(valeur_observer):
    res = 0
    for i in range(0, len(valeur_observer)):
        res += (i * valeur_observer[i])
    res /= 100 * 100
    return res


def total_from_tab(tab):
    res = 0
    for i in tab:
        res += i
    return res


def facto(lim):
    result = 1
    i = 2

    while i <= lim:
        result *= i
        i += 1
    return result


def combinaison(n, k):
    num = facto(k)
    denum1 = facto(n)
    denum2 = facto(k - n)
    denum1 *= denum2
    return num / denum1


def sum_square(ox, tx):
    res = 0
    for i in range(0, len(ox)):
        # ((Effectif observer - theorique) ^ 2) / theorique
        res += pow(ox[i] - tx[i], 2) / tx[i]
    return res

# return string
def fit_validity(sum, degr):
    fit_array = [[0, 99, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 3, 1],
      [1, 0.00, 0.02, 0.06, 0.15, 0.27, 0.45, 0.71, 1.07, 1.64, 2.71, 3.84, 5.41, 6.63],
      [2, 0.02, 0.21, 0.45, 0.71, 1.02, 1.39, 1.83, 2.41, 3.22, 4.61, 5.99, 7.82, 9.21],
      [3, 0.11, 0.58, 1.01, 1.42, 1.87, 2.37, 2.95, 3.66, 4.64, 6.25, 7.81, 9.84, 11.34],
      [4, 0.30, 1.06, 1.65, 2.19, 2.75, 3.36, 4.04, 4.88, 5.99, 7.78, 9.49, 9.84, 11.34],
      [5, 0.55, 1.61, 2.34, 3.00, 3.66, 4.35, 5.13, 6.06, 7.29, 9.24, 11.07, 11.67, 13.28],
      [6, 0.7, 2.20, 3.07, 3.83, 4.57, 5.35, 6.21, 7.23, 8.56, 10.64, 12.59, 15.03, 16.81],
      [7, 1.24, 2.83, 3.82, 4.67, 5.49, 6.35, 7.28, 8.38, 9.80, 12.02, 14.07, 16.62, 18.48],
      [8, 1.65, 3.49, 4.59, 5.53, 6.42, 7.34, 8.35, 9.52, 11.03, 13.36, 15.51, 18.17, 20.09],
      [9, 2.09, 4.17, 5.38, 6.39, 7.63, 8.34, 9.41, 10.66, 12.24, 14.68, 16.92, 19.68, 21.67],
      [10, 2.56, 4.87, 6.18, 7.27, 8.30, 9.34, 10.47, 11.78, 13.44, 15.99, 18.31, 21.16, 23.21]]

    i = 1
    found = False
    while i != 13:
        if fit_array[degr][i] <= sum <= fit_array[degr][i + 1]:
            max = fit_array[0][i]
            min = fit_array[0][i + 1]
            found = True
            break
        i += 1
    if not found:
        if fit_array[degr][1] <= sum:
            max = fit_array[0][13]
            ret = 'P<' + str(max) + '%'
            return ret
        if fit_array[degr][13] >= sum:
            max = fit_array[0][1]
            ret = 'P>' + str(max) + '%'
            return ret

    ret = str(min) + '%<P<' + str(max)+'%'
    return ret


def dowel():
    valeur_observer = []
    newX = []
    newTX = []
    newOX = []

    for i in sys.argv[1:]:
        valeur_observer.append(int(i))
    p = param_loi_binomial(valeur_observer)
    # valeur theorique
    r = 0
    for count in range(0, len(valeur_observer) - 1):
        result = 100 * combinaison(count, 100) * pow(p, count) * pow((1 - p), 100 - count)
        r += result
        newTX.append(result)
    newTX.append(100 - r)
    print(newTX)
    count = 0

    inc = 0
    while count < len(valeur_observer):
        newX.append(str(inc))

        if count - 1 >= 0 and count + 1 < len(valeur_observer) and valeur_observer[count] < 10:
            if valeur_observer[count - 1] + valeur_observer[count] < valeur_observer[count + 1] + valeur_observer[
                count]:
                valeur_observer[count] += valeur_observer[count - 1]
                valeur_observer.pop(count - 1)
                newX[count - 1] += '-' + str(inc)
                inc += 1
                newX[count] = str(inc)
                newTX[count] += newTX[count - 1]
                newTX.pop(count - 1)
                while valeur_observer[count - 1] < 10:
                    print(newX)
                    valeur_observer[count] += valeur_observer[count - 1]
                    valeur_observer.pop(count - 1)
                    if count < len(newTX) - 1:
                        newTX[count] += newTX[count - 1]
                        newTX.pop(count - 1)
                    newX[count - 1] += '-' + str(inc)
                    inc += 1
                    if inc < 9:
                        newX.append(str(inc))
                    newX.pop(count)

            else:
                newTX[count] += newTX[count + 1]
                newTX.pop(count+1)

        count += 1
        inc += 1
    
    if valeur_observer[len(valeur_observer) - 1] < 10:
        valeur_observer[count - 1] += valeur_observer[count - 2]
        valeur_observer.pop(count - 2)
        newX[count - 2] += '-' + str(inc - 1)
        newX.pop(count - 1)
        inc += 1
        while valeur_observer[count - 2] < 10:
            valeur_observer[count] += valeur_observer[count - 1]
            valeur_observer.pop(count - 1)
            newX[count - 1] += '-' + str(inc)
            inc += 1
            newX.pop(count)
    # get all the 1-2-3 fix in newX
    # and fix the + at end
    for i in range(0, len(newX)):
        tmp = newX[i].split('-')
        if len(tmp) != 1:
            newX[i] = tmp[0] + '-' + tmp[len(tmp) - 1]
        if i + 1 == len(newX):
            newX[i] = tmp[0] + '+'

    # dump section array
    print(" x\t| ", end="")
    for i in newX:
        print(i + '\t| ', end="")
    print(" total")

    for i in valeur_observer:
        newOX.append(i)
    print(" Ox\t| ", end="")
    for count in range(0, len(newOX)):
        print(str(newOX[count]) + "\t| ", end="")
    print(" 100")
    print(" Tx\t| ", end="")
    for count in range(0, len(newTX)):
        print("%.1f" % newTX[count] + "\t| ", end="")
    print(" 100")

    # end print section array
    # dump rest
    print("distribution:\t\t\tB(100, %.4f)" % p)
    sum = sum_square(newOX, newTX)
    print("sum of the square differences:\t%.3f"%sum)
    degr = len(newOX) - 2
    print("freedom degrees:\t\t{}".format(degr))
    print("fit validity:\t\t\t" + fit_validity(sum, degr))
    return 0


def main():
    try:
        if len(sys.argv) == 2 and sys.argv[1] == "-h":
            usage()
            return 0
        if len(sys.argv) < 10:
            print("Error: Not enough argument.")
            usage()
            exit(84)
        if len(sys.argv) is 10:
            check_input()
            dowel()
            return 0
        else:
            print("Error: To much arguments.")
            usage()
            exit(84)
    # except IndexError:
    #     print("Error: List index out of range.")
    #     exit(84)
    # except ValueError:
    #     print ("Could not convert data to an integer.")
    #     exit(84)
    # except OverflowError:
    #     print("Math range error.")
    #     exit(84)
    # except ZeroDivisionError:
    #     print("Error: Division by Zero.")
    #     exit(84)
    except KeyboardInterrupt:
        print("\nKeyboard Interuption.")
        exit(0)


if __name__ == '__main__':
    main()
