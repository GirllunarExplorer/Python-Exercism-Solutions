__author__ = 'tracyrohlin'

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix.split("\n")
        self.rows = []
        for row in self.matrix:
            row_list = [int(n) for n in row.split()]
            self.rows.append(row_list)
        self.columns = []
        for i in range(len(self.rows[1])):
            result = [int(row[i]) for row in self.rows]
            self.columns.append(result)

