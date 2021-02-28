romans = [
    ["I", 1],
    ["IV", 4],
    ["V", 5],
    ["IX", 9],
    ["X", 10],
    ["XL", 40],
    ["L", 50],
    ["XC", 90],
    ["C", 100],
    ["CD", 400],
    ["D", 500],
    ["CM", 900],
    ["M", 1000],
]


def number_to_roman(n):
    # change integer to roman
    result = ''
    i = len(romans) - 1
    while (n > 0):
        for k in range(n // romans[i][1]):
            result += romans[i][0]
            n -= romans[i][1]
        i -= 1
    return result


def get_row(arr, n):
    # get nth row from data
    column = len(arr)
    row = []
    for i in range(column):
        # check if the data is available, if not, empty string
        if len(arr[i]) < n+1:
            row.append("")
        else:
            row.append(arr[i][n])
    return row


def get_max_rows(arr):
    # get max rows in the data
    column = len(arr)
    m = len(arr[0])
    for i in range(1, column):
        if (m < len(arr[i])):
            m = len(arr[i])
    return m
