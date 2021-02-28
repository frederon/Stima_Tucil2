class Graph:
    def __init__(self, data):
        self.data = convertToGraph(data)
        self.count = len(data)
        self.e = [[]]

def conquer(data):
    result = []

    for key in data:
        if (len(data[key]) == 0):
            result.append(key)
    
    return result

def topologicalSort(data, result):
    if len(data) == 0:
        return result

    res = conquer(data)

    for key in res:
        for item in data:
            if key in data[item]:
                data[item].remove(key)
        del data[key]

    result.append(res)

    return topologicalSort(data, result)


def convertToGraph(lines):
    # make dictionary
    result = {}
    for line in lines:
        line = processLine(line)
        node = line[0]
        result[node] = line[1:]

    return result


def processLine(line):
    # remove spaces
    line = line.replace(" ", "")
    # remove .
    line = line.replace(".", "")
    # convert to list
    line = line.split(",")
    return line
