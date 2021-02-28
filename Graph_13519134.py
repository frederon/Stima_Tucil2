class Graph:
    def __init__(self, data):
        # create graph
        # convert lines data to graph
        self.data = convertToGraph(data)
        self.count = len(data)


def topologicalSort(data, result):
    # base, if dictionary is empty, result
    if len(data) == 0:
        return result

    # local result, conquer this sub problem
    res = []
    # check for empty prerequisite node (we can register to this course in this semester)
    for key in data:
        # if empty
        if (len(data[key]) == 0):
            # add to local result
            res.append(key)

    # decrease dictionary
    # for every course in local result
    for key in res:
        # for every course available in the dictionary
        for item in data:
            # if the data is in local result and also a prerequisite in another course
            if key in data[item]:
                # remove the prerequisite node as we are taking the course this semester
                data[item].remove(key)
        # remove the key, as the course has been taken
        del data[key]

    # add local result to global result
    result.append(res)

    # recursive to every sub problem
    # with smaller data, and bigger global result
    return topologicalSort(data, result)


def convertToGraph(lines):
    # make dictionary
    result = {}
    for line in lines:
        # process every line, so there is no spaces, dot, and split to list
        line = processLine(line)
        # course
        node = line[0]
        # prerequisite course
        # set dictionary key to be course, and value list of prerequisite course
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
