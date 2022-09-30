#  $$$$$$\  $$\       $$\      $$\ $$$$$$\
# $$  __$$\ $$ |      $$ | $\  $$ |\_$$  _|
# $$ /  $$ |$$ |      $$ |$$$\ $$ |  $$ |
# $$$$$$$$ |$$ |      $$ $$ $$\$$ |  $$ |
# $$  __$$ |$$ |      $$$$  _$$$$ |  $$ |
# $$ |  $$ |$$ |      $$$  / \$$$ |  $$ |
# $$ |  $$ |$$$$$$$$\ $$  /   \$$ |$$$$$$\
# \__|  \__|\________|\__/     \__|\______|

import queue

def buatmap():
    map = []
    map.append(["#", "#", "#", "#", "#", "#", "#", "#", "#"])
    map.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    map.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
    map.append(["#", "A", "#", " ", " ", " ", " ", " ", "#"])
    map.append(["#", " ", "#", " ", "#", "#", "#", "#", "#"])
    map.append(["#", " ", "#", " ", " ", " ", " ", " ", "#"])
    map.append(["#", "#", "#", "#", "#", "#", "#", " ", "#"])
    map.append(["#", " ", " ", " ", " ", " ", "Z", " ", "#"])
    map.append(["#", "#", "#", "#", "#", "#", "#", "#", "#"])


    return map

def validMove(map, langkah):
    for j, isi_map in enumerate(map):
        for i,col in enumerate(isi_map):
            if col == "A":
                x1 = i
                y1 = j
                break

    x = x1
    y = y1

    for i in langkah:
        if i == "U":
            y -= 1
        elif i == "R":
            x += 1
        elif i == "D":
            y += 1
        elif i == "L":
            x -= 1


    if not ( 0<= x < len(map[0]) and 0 <= y < len(map)):
        return False
    elif map[y][x] == "#":
        return False

    return True

def titikakhir(map, langkah):
    for j, isi_map in enumerate(map):
        for i,col in enumerate(isi_map):
            if col == "A":
                x1 = i
                y1 = j
                break

    x = x1
    y = y1


    for i in langkah:
        if i == "U":
            y -= 1
        elif i == "R":
            x += 1
        elif i == "D":
            y += 1
        elif i == "L":
            x -= 1

    if map[y][x] == "Z":
        locatePath(map,langkah)
        print("langkah kesini " + langkah)
        print("U= atas, R= kanan, D= bawah, L= kiri")

        printMap(map)
        return True

    return False

def locatePath(map, langkah):
    for j, isi_map in enumerate(map):
        for i,col in enumerate(isi_map):
            if col == "A":
                x1 = i
                y1 = j
                break

    x = x1
    y = y1

    for i in langkah:
        if i == "U":
            y -= 1
        elif i == "R":
            x += 1
        elif i == "D":
            y += 1
        elif i == "L":
            x -= 1
        if map[y][x] != "Z":
            map[y][x] = "+"


    return map

def printMap(map):
    for j, isi_map in enumerate(map):
        for i, col in enumerate(isi_map):
            print(col + " ",end="")
        print()

def stepscount(map):
    steps = 0
    for j, isi_map in enumerate(map):
        for i,col in enumerate(isi_map):
            if col == " ":
                steps +=1
    steps+=4
    return steps

print("Tunggu bentar . . .")
#RUN
map = buatmap()
bfs = queue.Queue()
bfs.put("")
posstep = ""
totstep = stepscount(map)

while not titikakhir(map,posstep):
    if len(posstep) > totstep:
        print("Jalur tidak valid")
        exit(2)

    posstep = bfs.get()
    for direction in ["U","R","D","L"]:
        choice = posstep + direction
        if validMove(map,choice):
            bfs.put(choice)

exit(0)