# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# Hurdles
# def turn_right():
#     for turn in range(0, 3):
#         turn_left()
#
# def jump_hurdle():
#     move()
#     turn_left()
#     move()
#     for right in range(0, 2):
#         turn_right()
#         move()
#     turn_left()
#
# for jump in range(6):
#     jump_hurdle()

# Unknown number of hurdles
# def turn_right():
#     for turn in range(0, 3):
#         turn_left()
#
# def jump_hurdle():
#     move()
#     turn_left()
#     move()
#     for right in range(0, 2):
#         turn_right()
#         move()
#     turn_left()
#
# while at_goal() == False:
#     jump_hurdle()

# Unknown track
# def turn_right():
#     for turn in range(3):
#         turn_left()
#
# def jump_hurdle():
#     turn_left()
#     move()
#     for right in range(2):
#         turn_right()
#         move()
#     turn_left()
#
# while not at_goal():
#     if wall_in_front():
#         jump_hurdle()
#     else:
#         move()

# Unknown height
# def turn_right():
#     for turn in range(3):
#         turn_left()
#
# def jump_hurdle():
#     turn_left()
#     while wall_on_right():
#         move()
#     for right in range(2):
#         turn_right()
#         move()
#     while front_is_clear():
#         move()
#     turn_left()
#
# while not at_goal():
#     if wall_in_front():
#         jump_hurdle()
#     else:
#         move()

# Maze
# If the right is clear turn right and move
# If ahead is clear move
# if it can’t turn right, or move forwar turn left
# Infinite loop can occur at rows 4 & 5 and columns 2 & 3
# def turn_right():
#     for turn in range(3):
#         turn_left()
#
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
#         if at_goal():
#             move()