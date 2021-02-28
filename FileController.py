from datetime import datetime
from utils import number_to_roman

class FileController:

  def __init__(self, fileName):
    f = open(fileName)
    self.data = []
    for l in f.readlines():
      self.data.append(l.rstrip("\n"))

def export(directory, data):
  directory = directory[:-1]
  f = open(directory + datetime.today().strftime('%Y-%m-%d-%H%M%S') + ".txt", "w+")
  for i in range(len(data)):
    f.write("=============================\n")
    f.write(data[i][0] + "\n")
    f.write("=============================\n")
    for sem in range(1, len(data[i][1]) + 1):
      f.write("Semester " + str(number_to_roman(sem)) + ":\n")
      for item in data[i][1][sem-1]:
        f.write(str(item) + "\n")