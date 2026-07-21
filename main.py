
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





print("press 1 for creating a file.")
print("press 2 for reading a file.")
print("press 3 for updating a file.")
print("press 4 for deleting a file.")

check = int(input("enter your choice: "))

if check == 1:
    createfile()
