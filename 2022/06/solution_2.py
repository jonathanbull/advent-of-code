max_buffer_length = 14

def find_first_marker(data):
    buffer = []
    char_pos = 1
    for char in data:
        buffer.append(char)
        if len(buffer) == (max_buffer_length + 1):
            buffer.pop(0)

            if len(set(buffer)) == len(buffer):
                # List is of length max_buffer_length and contains unique chars
                return char_pos

        char_pos += 1


with open('input.txt') as input_file:
    data = input_file.read().strip()
    first_marker = find_first_marker(data)

    print('First marker: {}'.format(first_marker))
