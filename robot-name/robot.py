__author__ = 'tracyrohlin'

import string, random


class Robot:
    name_list = None


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
        if self.name not in self.name_list:
            self.name_list += self.name
        else:
            self.name = self.robot_name()
            self.reset()


robot = Robot()
print robot.name