__author__ = 'tracyrohlin'

import string, random

name_list = []

class Robot:
    def __init__(self):
        self.name = self.robot_name()
        self.reset()


    def robot_name(self):
        alphabet = string.ascii_uppercase
        digits = string.digits

        first_two = [random.choice(alphabet) for n in range(2)]
        last_bits = [random.choice(digits) for n in range(3)]
        self.name = "".join(first_two + last_bits)
        return self.name

    def reset(self):
        if self.name not in name_list:
            name_list.append(self.name)
        else:
            self.name = self.robot_name()
            self.reset()


robot = Robot()
print robot.name