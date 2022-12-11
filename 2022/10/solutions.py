# CPU has a single register (X) that starts at 1.
# It supports two instructions:
# 1. `addx V` takes two cycles to complete. After two cycles, X is increased by the value V (V can be negative)
# 2. `noop` takes one cycle to complete and has no other effect.

import numpy as np
from colorama import Cursor

class Device:
    x_register_value = 1
    cur_cycle_counter = 0
    summed_signal_strengths = 0
    sprite = []

    # initialize a "flat" index of display 
    display_matrix = np.arange(0,240).reshape((6,40))

    # update sprite position based on current X register value
    def set_sprite(self):
        self.sprite = [self.x_register_value -1, self.x_register_value, self.x_register_value + 1]

    # when called, calculate and return the current cycle's signal strength 
    def get_signal_strength(self):
        return self.x_register_value * self.cur_cycle_counter

    # Given a number, add the number to the current value of register X. takes 2 cycle counts.
    def addx(self,addend):
        self.process_cycle()
        self.process_cycle()
        self.x_register_value += int(addend)
        self.set_sprite()

    # Do nothing ("no operation") for 1 cycle count
    def noop(self):
        self.process_cycle()

    def process_cycle(self):
         # Checks if the current cycle is a valid target to check signal strength
        if self.cur_cycle_counter == 20 or (self.cur_cycle_counter - 20) % 40 == 0:
            self.summed_signal_strengths += self.get_signal_strength()

        # Checks if current sprite position overlaps with the pixel currently being written and updates the display if so
        # reshape display matrix to a 1D array, get the values of self.sprite, and set the corresponding matrix values accordingly
        vertical_slice = self.display_matrix[0:,self.sprite[0]:(self.sprite[0]+3)]
        if self.cur_cycle_counter in vertical_slice:
            if (self.cur_cycle_counter + 1) % 40 != 0:
                print('#', end="")
            else:
                print('#')
        else: 
            if (self.cur_cycle_counter + 1) % 40 != 0:
                print('.', end="")
            else:
                print('.')

        # mark the end of the cycle
        self.cur_cycle_counter += 1

# open input file and return formatted output
def format_input(input_filename):
    with open(input_filename, 'r') as file:
        unformatted_input = file.read().splitlines()
        formatted_input = [i.split() for i in unformatted_input]

        return formatted_input

""" def p1():

    input = format_input('input.txt')

    # instantiate the device
    my_device = Device()

    # process the input commands
    for command in input:
        match command[0]:
            case 'addx':
                my_device.addx(command[1])
            case 'noop':
                my_device.noop()

    return my_device.summed_signal_strengths """

# X register = horizontal position of a sprite
# sprite = 3 pixels wide, X = middle pixel's horizontal position
# grid is a 40p (0 -> 39) x 6p (0 -> 5) display, 
# with 1p drawn per cycle

# if any one of the sprite's 3 pixels is the pixel currently being drawn,
# the screen produces a lit lit pixel (#); 
# otherwise, the screen leaves the pixel dark (.)

def p2():

    input = format_input('input.txt')

    # instantiate the device
    my_device = Device()
    my_device.set_sprite()

    for command in input:
        match command[0]:
            case 'addx':
                my_device.addx(command[1])
            case 'noop':
                my_device.noop()


#print(p1())
print(p2())