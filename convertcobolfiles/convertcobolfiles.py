import codecs
import string
from operator import attrgetter


# Inspired by: 
# http://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch34s05.html


class Field(object):
    def __init__(self, index, lenght, comp3=False, strip=False):
        self.index = index
        self.comp3 = comp3
        self.strip = strip
        if comp3:
            self.lenght = (lenght // 2) + 1
        else:
            self.lenght = lenght


cp037 = codecs.getdecoder('cp037')


def normal(word):
    return cp037(word)[0]


def comp3( bytes ):
    n= [ '' ]
    for b in bytes[:-1]:
        hi, lo = divmod( ord(b), 16 )
        n.append( str(hi) )
        n.append( str(lo) )
    digit, sign = divmod( ord(bytes[-1]), 16 )
    n.append( str(digit) )
    if sign in (0x0b, 0x0d ):
        n[0]= '-'
    else:
        n[0]= '+'
    return "".join(n)


def remove_invalid_characters(word):
    res = ''
    for c in word:
        if c in string.printable:
            res += c
    return res


def read_buffer(file, buffer_size):
    buffer_text = file.read(buffer_size)
    while buffer_text:
        yield buffer_text
        buffer_text = file.read(buffer_size)


def handle_line(buffer, fields, field_delimiter=';'):
    fields = sorted(fields, key=attrgetter('index'))
    initial = 0
    line = u''
    for field in fields:
        _field = handle_field(buffer, initial, field)        

        if line:
            line += field_delimiter + _field
        else:
            line = _field
            
        initial += field.lenght
    return line
    

def handle_field(buffer, initial_byte, field):    
    if field.comp3:
        _field = comp3(buffer[initial_byte:initial_byte + field.lenght])
    else:
        _field = normal(buffer[initial_byte:initial_byte + field.lenght])

    if field.strip:
        _field = _field.strip()

    return _field


















