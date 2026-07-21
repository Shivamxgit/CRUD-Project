
from pathlib import Path

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")


def createfile():
    try:
        readfileandfolder()
        name = input("enter the file name: ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as file:
                data = input("enter your content: ")
                file.write(data)

            print(f"FILE CREATED SUCCESSFULLY")

        else:
            print("this file already exists.")
    except Exception as err:
        print(f"an error occured as {err}")


def readfile():
    try:
        readfileandfolder()
        name = input("enter the file name to read: ")
        p =Path(name)
        if p.exists() and p.is_file():
            with open(p, "r") as file:
                content= file.read()
                print(content)
            print("\n END")
        else:
            print("this file does not exists.")

    except Exception as err:
        print(f"an error occured as {err}")


def updatefile():
    try:
        readfileandfolder()
        name = input("enter the file name: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the file name : ")
            print("press 2 for overwriting the file data :")
            print("press 3 for appending the file data :")
            choice = int(input("enter your choice = "))

            if choice == 1:
                new_name = input("enter the new name of the file = ")
                p_new = Path(new_name)
                p.rename(p_new)

            if choice ==2 :
                with open(p, "w") as file:
                    data = input("enter your content and it will be ""overwritten"": ")
                    file.write(data)

            if choice == 3:
                with open(p, "a") as file:
                    data = input("enter your content to append : ")
                    file.write(" " + data + "\n")

            print(f"FILE UPDATED SUCCESSFULLY")

        else:
            print("this file does not exist.")
    except Exception as err:
        print(f"an error occured as {err}")


def updatefile2():
    try:
        readfileandfolder()
        name = input("enter the file name: ")
        p = Path(name)
        if p.exists():
            # Step 1: Read existing content
            with open(p, "r") as file:
                content = file.read()

            print("Current content:")
            print(content)

            # Step 2: Ask user what to replace
            old_text = input("Enter the text you want to replace: ")
            new_text = input("Enter the new text: ")

            # Step 3: Modify content
            updated_content = content.replace(old_text, new_text)

            # Step 4: Write back to file
            with open(p, "w") as file:
                file.write(updated_content)

            print("FILE UPDATED SUCCESSFULLY")
        else:
            print("This file does not exist.")
    except Exception as err:
        print(f"An error occurred: {err}")


def deletefile():
    try:
        readfileandfolder()
        name = input("which file you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink() # DELETES THE FILE
        else:
            print("the file does not exists.")
    except Exception as err:
        print(f"exception occured as {err}.")

    


print("press 1 for creating a file.")
print("press 2 for reading a file.")
print("press 3 for updating a file.")
print("press 4 for deleting a file.")
print("press 5 to replace the file content.")

check = int(input("enter your choice: "))

if check == 1:
    createfile()

if check ==2:
    readfile()

if check ==3:
    updatefile()

if check == 4:
    deletefile()

if check == 5:
    updatefile2()