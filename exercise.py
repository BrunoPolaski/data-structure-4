
def add_to_list():
    noDupsList = []
    noDupsList = int(input("Enter a number: "))
    for i in range(9):
        value = int(input("Enter a number: "))
        duplicated = False
        for i in range(len(noDupsList)):
            if i == value:
                duplicated = True
        if duplicated == False:
            noDupsList += [value]
        else:
            print("No duplicates allowed")
            i -= 1
add_to_list()