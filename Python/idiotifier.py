import random
import math

def idiotify(args):
    array = [char for char in args.text]

    for i in range(0, len(array)):
        rand = math.floor(random.randint(1,10))

        if((rand % 2) == 0):
            array[i] = array[i].upper()
        else:
            array[i] = array[i].lower()

    frase = ''
    print(frase.join(array))

