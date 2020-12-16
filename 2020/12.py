from enum import Enum
from math import cos, sin, radians
import sympy

class Orientation(Enum):
    NORTH, EAST, SOUTH, WEST, = ('N', 0), ('E', 90), ('S', 180), ('W', 270)


commands = open('input-12.txt').readlines()

def apply_command(command, orientation, east, north):
    command_num = int(command[1:])
    if command[0] == 'N':
        north += command_num
    elif command[0] == 'S':
        north -= command_num
    elif command[0] == 'E':
        east += command_num
    elif command[0] == 'W':
        east -= command_num
    elif command[0] == 'F':
        _, east, north = apply_command(orientation.value[0] + str(command_num), orientation, east, north)
    elif command[0] == 'L':
        orientation, _, _ = apply_command('R' + str(360 - command_num), orientation, east, north)
    elif command[0] == 'R':
        command_num += orientation.value[1]
        command_num = command_num % 360
        orientation = [o for o in Orientation if o.value[1] == command_num][-1]
    return orientation, east, north

orientation, east, north = Orientation.EAST, 0, 0
for command in commands:
    orientation, east, north = apply_command(command, orientation, east, north)

print(orientation, east, north)
print('manhatten distance: ', abs(east) + abs(north))

# applying with rotation matrix (need to convert angle to radians)
def apply_command2(command, east, north, x, y):
    command_num = int(command[1:])
    if command[0] == 'N':
        y += command_num
    elif command[0] == 'S':
        y -= command_num
    elif command[0] == 'E':
        x += command_num
    elif command[0] == 'W':
        x -= command_num
    elif command[0] == 'F':
        east += command_num * x
        north += command_num * y
    elif command[0] in ('L', 'R'):
        if command[0] == 'R':
            command_num = -command_num
        theta = radians(command_num % 360)
        x, y = x*cos(theta) - y*sin(theta), x*sin(theta) + y*cos(theta)
    return east, north, x, y

# using knowledge of quadrants to determine rotation
def apply_command3(command, east, north, x, y):
    command_num = int(command[1:])
    if command[0] == 'N':
        y += command_num
    elif command[0] == 'S':
        y -= command_num
    elif command[0] == 'E':
        x += command_num
    elif command[0] == 'W':
        x -= command_num
    elif command[0] == 'F':
        east += command_num * x
        north += command_num * y
    elif command[0] == 'L':
        east, north, x, y = apply_command3('R' + str(360 - command_num), east, north, x, y)
    elif command[0] == 'R':
        command_num = command_num % 360
        if command_num == 90:
            if x >= 0 and y>= 0: # we're in 1st quadrant
                x, y = y, -x
            elif x < 0 and y>= 0: # we're in 2ndt quadrant
                x, y = y, -x
            elif x < 0 and y < 0: # we're in 3rd quadrant
                x, y = y, -x
            elif x >= 0 and y < 0: # we're in 4th quadrant
                x, y = y, -x
        else:
            east, north, x, y = apply_command3('R90', east, north, x, y)
            east, north, x, y = apply_command3('R'+str(command_num - 90), east, north, x, y)

    return east, north, x, y

# applying with rotation matrix (need to convert angle to radians)
def apply_command4(command, east, north, x, y):
    command_num = int(command[1:])
    if command[0] == 'N':
        y += command_num
    elif command[0] == 'S':
        y -= command_num
    elif command[0] == 'E':
        x += command_num
    elif command[0] == 'W':
        x -= command_num
    elif command[0] == 'F':
        east += command_num * x
        north += command_num * y
    elif command[0] in ('L', 'R'):
        if command[0] == 'R':
            command_num = -command_num
        theta = (command_num % 360) * sympy.pi/180
        x, y = x*sympy.cos(theta) - y*sympy.sin(theta), x*sympy.sin(theta) + y*sympy.cos(theta)
    return east, north, x, y

east, north, waypoint_east, waypoint_north = 0, 0, 10, 1
for command in commands:
    east, north, waypoint_east, waypoint_north = apply_command2(command, east, north, waypoint_east, waypoint_north)

print(east, north, waypoint_east, waypoint_north)
print('manhatten distance using rotation matrix: ', abs(east) + abs(north))

east, north, waypoint_east, waypoint_north = 0, 0, 10, 1
for command in commands:
    east, north, waypoint_east, waypoint_north = apply_command3(command, east, north, waypoint_east, waypoint_north)

print(east, north, waypoint_east, waypoint_north)
print('manhatten distance using quadrants: ', abs(east) + abs(north))

east, north, waypoint_east, waypoint_north = 0, 0, 10, 1
for command in commands:
    east, north, waypoint_east, waypoint_north = apply_command3(command, east, north, waypoint_east, waypoint_north)

print(east, north, waypoint_east, waypoint_north)
print('manhatten distance using rotation matrix, sympy version: ', abs(east) + abs(north))
