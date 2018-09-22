def get_line_number(index):
    if index == 25:
        return 5
    else:
        return index // 5 + 1


def get_line_borders(index):
    line_number = get_line_number(index)
    start = 5 * line_number - 5
    end = start + 5
    return [start, end]


def shift_array(array):
    return array[1:] + array[:1]


def shift_horizontally(index, array):
    line_borders = get_line_borders(index)
    line = shift_array(array[line_borders[0]:line_borders[1]])
    array[line_borders[0]:line_borders[1]] = line
    return array


def get_vertical_line(index):
    start = index % 5
    return [start, start + 5, start + 10, start + 15, start + 20]


def shift_vertically(index, array):
    vertical_line = get_vertical_line(index)
    tmp = array[vertical_line[0]]
    for i in range(len(vertical_line)-1):
        array[vertical_line[i]] = array[vertical_line[i+1]]
    array[vertical_line[len(vertical_line)-1]] = tmp
    return array

# Using one-dimensional-array
arr_letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

input = input()

result = []
for letter in input:
    letterPosition = arr_letters.index(letter)
    result.append(str(letterPosition+1))
    arr_letters = shift_horizontally(letterPosition, arr_letters)
    letterPosition = arr_letters.index(letter)
    arr_letters = shift_vertically(letterPosition, arr_letters)

print(' '.join(result))
