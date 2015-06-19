
class Garden:
    def __init__(self, garden_string, students=None):
        self.garden_string = garden_string
        if not students:
            self.students = ["Alice", "Bob",
                             "Charlie", "David",
                             "Eve", "Fred",
                             "Ginny", "Harriet",
                             "Ileana", "Joseph",
                             "Kincaid", "Larry"]
        else:
            self.students = students
        self.plant_names = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}

    def plants(self, name):
        self.students.sort()
        plant_pos = dict((key, value) for (key, value) in zip(self.students, range(0, len(self.students)*2, 2)))
        windows = self.garden_string.split()


        w_sill = []
        i = plant_pos[name]
        for win in windows:
            w_sill.append(win[i])
            w_sill.append(win[i+1])


        result = []
        for plant in w_sill:
            result.append((self.plant_names[plant]))

        return result