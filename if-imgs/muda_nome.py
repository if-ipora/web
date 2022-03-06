import os

path = os.getcwd()

i = 0
for file in os.listdir(path):
    if file[-2:] != 'py':
        i+=1

        nome = "img" + str(i) + ".png"
        print(nome)
        os.rename(file, nome)
