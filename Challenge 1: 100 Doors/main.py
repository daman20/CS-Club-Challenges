'''
See README.md for challenge info

'''


def generateDoorsDict():
    """ This function generates a dictionary of doors, with their position closed, and their keys 1-100"""
    doors = []
    for i in range(100):
        doors.append(i)
        doors[i] = False
    return doors


def toggleDoor(door: str, doors: dict):
    """ This function changes the status of the door from open to closed or vise versa, returning the new dict"""
    print(not doors[door])
    doors[door] = not doors[door]
    return doors


def toggleAllDoors(doors: dict):
    """ This function toggles every door in the "doors" input, returning the doors dict
    """
    for door in doors:
        toggleDoor(door=door, doors=doors)
    return doors


def toggleEvenDoors(doors: dict):
    """ This function toggles every even door in the "doors" input, returning the doors dict
    """
    dictKeys = doors.keys()
    for door in doors:
        index = dictKeys.index(doors[door])
        if index % 2 == 0:
            toggleDoor(door=door)
    return doors


def toggleThirdDoors(doors: dict):
    """ This function toggles every third door in the "doors" input, returning the doors dict
    """
    dictKeys = doors.keys()
    for door in doors:
        index = dictKeys.index(doors[door])
        if index % 3 == 0:
            toggleDoor(door=door)
    return doors


def main():
    doors = generateDoorsDict()
    #print(doors)
    for i in range(1):
        doors = toggleAllDoors(doors)
        '''
        doors = toggleEvenDoors(doors)
        doors = toggleThirdDoors(doors)
        '''
    #print(doors)


main()
