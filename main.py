i = 1

# set screen
y1 = [1, 0, 0, 0, 0]
y2 = [0, 0, 0, 0, 0]
y3 = [0, 0, 0, 0, 0]
y4 = [0, 0, 0, 0, 0]
y5 = [0, 0, 0, 0, 0]

# setup x & y coardinates
x: int = 0
y = 0
old_x = 0
old_y = 0


# setup for screen movment
def update_screen():
    if y == 1:
        y1[x] = 1
    if y == 2:
        y2[x] = 1
    if y == 3:
        y3[x] = 1
    if y == 4:
        y4[x] = 1
    if y == 5:
        y5[x] = 1
    if not old_y == 0:
        y1[old_x] = 0
    if not old_y == 2:
        y2[old_x] = 0
    if not old_y == 3:
        y3[old_x] = 0
    if not old_y == 4:
        y4[old_x] = 0
    if not old_y == 5:
        y5[old_x] = 0
    print(y1)
    print(y2)
    print(y3)
    print(y4)
    print(y5)

# game loop
while i == 1:
    action = input("action (put help for actions): ")
    if action == "move down":
        old_y = y
        y += 1
        update_screen()
    if action == "move up":
        old_y = y
        y -= 1
        update_screen()
    if action == "move right":
        old_x = x
        x += 1
        update_screen()
    if action == "move left":
        old_x = x
        x -= 1
        update_screen()
    if action == "help":
        print("actions: move up, move down, move left, move right")
