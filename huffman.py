import heapq
import string

class ByteString(bytes):
    """This is just to fix the fact that iterating through a bytes returns ints
    not more bytes"""
    def __iter__(self):
        for i in super().__iter__():
            yield ByteString([i])

    def __add__(self, other):
        return ByteString(super().__add__(other))

    def __mul__(self, other):
        return ByteString(super().__mul__(other))

    def __repr__(self):
        return f'ByteString{super().__repr__()[1:]}'

def encode(string):
    """Encodes a string into a huffman tree"""

    codes = {} # The binary tree which holds the codes
    queue = [] # The priority queue to build the tree

    # For each unique charcter in the string
    for char in set(string):
        # Add how many characters in the queue and the character into the heap
        # It is (count, label) so it is sortable by priority
        heapq.heappush(queue, (string.count(char), char))

    # While there are two values to merge in the priority queue
    while len(queue) > 1:
        # Get the count and the label for the two smallest elements in the tree
        c1, l1 = heapq.heappop(queue)
        c2, l2 = heapq.heappop(queue)

        # Push the combined character cound and label to the heap
        heapq.heappush(queue, (c1 + c2, l1 + l2))

        # Add the respective node to the binary tree
        codes[l1] = (l1+l2, '0')
        codes[l2] = (l1+l2, '1')

    out = '' # The output string
    str_map = {} # The map of characters to bits

    # For each unique character in the string
    for char in set(string):
        code = '' # The code of that character
        label = char # The current label

        # While the node is not the root
        while label in codes:
            # Add whether it is a left or the right child in front of the code
            code = codes[label][1] + code
            # Add do the same for the parent
            label = codes[label][0]

        # Add the code to the string map
        str_map[char] = code

    # For each character in the string, add it to the map
    for char in string:
        out += str_map[char]

    # Add some bits of padding to make it an integer number of bytes
    padding = '0'*((8-len(out))%8)
    out += padding

    # The output bytes
    out_byte = []

    # For each byte in the output
    for byte in range(0,len(out),8):
        # Print the progress
        print('\b'*100,f"{byte//8}/{len(out)//8}",end='',sep='')
        out_byte += [int(out[byte:byte+8],2)]

    # Turn the output into bytes
    out_byte = bytes(out_byte)
    print('\b'*100)
    return out_byte, len(padding), str_map

def escape_whitespace(char):

    # Turn it into a string
    if isinstance(char, bytes):
        try:
            char = char.decode()
        except UnicodeDecodeError:
            # If there is an issue with converting it to unicode, give the hex value
            return fr"""'\x{hex(ord(char))[2:].rjust(2,"0")}'"""

    # If you can see the char, return it. Otherwise give the hex value.
    if char in string.printable and char not in string.whitespace:
        return char
    else:
        return fr"""'\x{hex(ord(char))[2:].rjust(2,"0")}'"""

def main():
    # Get a file to open
    filename = input('Please enter the filename: ')

    # Open it
    with open(filename, 'rb') as f:
        text = f.read()

    # Uncomment this for test example
    # text = b'TESS SAW A RAT UP A TREE'

    # Compress it
    out_byte, padding_length, str_map = encode(ByteString(text))


    print('Conversion Table:')

    for char in sorted(list(str_map.keys())):
        print(f'\t{escape_whitespace(char)}:\t{str_map[char]}')


    print(f'Has {padding_length} bits of padding at the end.')

    print()
    print(f'{len(text)} bytes in original file.')
    print(f'{len(out_byte)} bytes ({len(out_byte)*8-padding_length} bits) in new file')
    # Not using f strings because I want floats to 1 d.p.
    # Compression efficiency is the percentage reduction in file size. The best possible for huffman is 87.5%
    print(f'%.1f%% compression efficiency.' % (100 - len(out_byte)/len(text)*100))
    print()

    outfilename = input('Please enter file to write to: ')

    with open(outfilename, 'wb') as f:
        f.write(out_byte)

if __name__ == '__main__':
    main()
