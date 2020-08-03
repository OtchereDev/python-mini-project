from random import choice

def egg(r):
    for i in range(-r,r):
        c=choice(['#', '*', 'X', '+','='])
        for j in range(-r,r):
            if ((i*i+j*j < (r-2)*(r-2))):
                print(c, end='')

            else:
                print('.',end='')

            print('')

        print('..Happy Easter Pythonistas')

egg(15)