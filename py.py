import os, tempfile
from PIL import Image
inpng = './inpng/'
pngs = './pngs/' 
injpg = './injpg/'
jpgs = './jpgs/'
mode = input("Какой режим выбираем?\n Jpg2png-1 \n Png2jpg-2\n")
if mode == "1": #Jpg2png
    for file in os.listdir(inpng): #Есть ли файлы в папке
        if file:
            pngsname = file + ".png"
            print(file)
            imagejpg = Image.open(inpng + file)
            os.chdir(pngs)
            imagejpg.save(pngsname)
        print("Всё сохранилось в " + pngs)
        if not file: #Если нет, ошибка
            print("В папке inpng не обнаружено файлов!")
            print(file)
elif mode == "2": #Png2jpg
    for file in os.listdir(injpg): #Есть ли файлы в папке
        if file:
            jpgsname = file + ".jpg"
            print(file)
            imagejpg = Image.open(injpg + file)
            os.chdir(jpgs)
            imagejpg.save(jpgsname)
        print("Всё сохранилось в " + jpgs)
        if not file: #Если нет, ошибка
            print("В папке injpg не обнаружено файлов!")
            print(file)
input()