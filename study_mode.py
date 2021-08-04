import random

string = ""


f = []
k = []
l = []
q = []


def j(letters, length):
    return ''.join(random.choice(letters) for i in range(length))


def get_random_string(letters):
    s = ""

    c = 200
    d = 50
    length = 1
    first_letters = letters[0:2]
    second_letters = letters[2:4]

    dict_ = {
        0: (f, first_letters),
        1: (k, second_letters),
        2: (l, letters)
    }
    for i in range(3):
        while c:
            dict_[i][0].append(j(dict_[i][1], length))

            c -= 1
            if c % 50 == 0:
                length += 1
        length = 1
        c = 200

    for i in range(3):
        while d:
            index = random.randint(1, len(dict_[i][0]))
            if d == 1:
                s += dict_[i][0][index - 1] + "."
                if i != 2:
                    s += " "

            else:
                s += dict_[i][0][index - 1] + " "
            d -= 1
        d = 100
    return s


