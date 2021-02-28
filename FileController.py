from datetime import datetime
from utils import number_to_roman


class FileController:

    def __init__(self, fileName):
        # load file
        f = open(fileName)
        # data for saving file content
        self.data = []
        for l in f.readlines():
            # remove new line
            self.data.append(l.rstrip("\n"))


def export(directory, data):
    # remove the last character (dot)
    directory = directory[:-1]
    # create new file in the selected directory
    f = open(directory + datetime.today().strftime('%Y-%m-%d-%H%M%S') + ".txt", "w+")

    # for every data available
    for i in range(len(data)):
        f.write("=============================\n")
        # print file name
        f.write(data[i][0] + "\n")
        f.write("=============================\n")
        # for every semester
        for sem in range(1, len(data[i][1]) + 1):
            # print semester
            f.write("Semester " + str(number_to_roman(sem)) + ":\n")
            for item in data[i][1][sem - 1]:
                # print course
                f.write(str(item) + "\n")
