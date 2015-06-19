__author__ = 'tracyrohlin'

class Phone:
    def __init__(self, phonenum):
        from re import sub
        self.phonenum = sub(r'[\D+]', "", str(phonenum))

        if len(self.phonenum) < 10 or len(self.phonenum) > 11:
            self.phonenum = "0"*10
        if len(self.phonenum) == 11:
            if self.phonenum[0] == str(1):
                self.phonenum = self.phonenum[1:]
            else:
                self.phonenum = "0"*10

    def number(self):
        return self.phonenum

    def area_code(self):
        return self.phonenum[0:3]

    def pretty(self):
        return "({0}) {1}-{2}".format(self.area_code(), self.phonenum[3:6], self.phonenum[6:])


