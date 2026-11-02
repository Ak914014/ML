from pathlib import Path 
import os
def readFileAndFolder():
    path = Path('')
    items = list(path.rglob('*'))

    for i , items in enumerate(items):
        print(f"{i+1} : {items}") 


def createFile():
    try:
        readFileAndFolder()
        name = input("please tell your file name :-")
        p = Path(name)
        if not p.exists():

          with open (p, "w") as fs:
             data = input("what you want to write in this file :-")
             fs.write(data)
          print(F"File CreatedSuccesfully")
        else: 
          print("this file already exist")
    except Exception as err :
        print(f'An error ocured as {err}')



def readfile ():
    try:
        readFileAndFolder()
        name = input("please tell your file name you wanna read :-")
        p = Path(name)
        if p.exists() and p.is_file():

            with open (p, "r") as fs:
                #  data = input("what you want to write in this file :-")
                r = fs.read(p)
                print(r)
            print("readed successfully")

        else: 
            print("this file not exist")
    except Exception as err :
        print(f'An error ocured as {err}')


def updateFile():
    try:
        readFileAndFolder()
        name = input("please tell your file name :-")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file: - ")

            print("press 2 for overwriting the data of your file: - ")

            print("press 3 for appending some content in your file: - ")
            button = int(input(" give the number :-"))
            if button == 1: 
                    data = input("Tell you new file name :-")
                    p2 = Path(data)
                    p.rename(p2)
                    print(F"File updated sucessfully")
            elif button == 2:
                with open (p, "w") as fs:
                    data = input("what you wanted to overwrite on the")
                    fs.write(data)
                    print(F"File updated sucessfully")
            elif button == 3: 
                 with open (p, "a") as fs:
                    data = input("what you wanted to overwrite on the")
                    fs.write(data)
                    print(F"File updated sucessfully")
       
        else: 
          print("this file already exist")
    except Exception as err :
        print(f'An error ocured as {err}')


def deleteFIle():
    try:
        readFileAndFolder()
        name = input("Tell me your file name which you wanted to delete :- ")
        p = Path(name)
        if p.exists() and  p.is_file: 
         os.remove(name)
         print("File is removed")
        else: 
            print("this file not exist")
    except Exception as err :
        print(f'An error ocured as {err}')

print('press 1 for createing file')

print('press 2 for Reading file')

print('press 3 for edit file')

print('press 4 for deleteing file')

check = int(input("plese tell your response :-"))

if check == 1:
    createFile()

if check == 2:
    readfile()

if check == 3:
    updateFile()

if check == 4:
    deleteFIle()