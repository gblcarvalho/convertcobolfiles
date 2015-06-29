import codecs
import convertcobolfiles as ccf
from bookfile import *

"""Simple Example"""

with codecs.open('MY.FILE.GENERATED.BY.COBOL','rb') as file_in, \
     codecs.open('OUTPUT_FILE.txt','w','utf-8') as file_out:
    
    for text_buffer in ccf.read_buffer(file_in, SIZE_BUFFER):
        line = u''
        field = ccf.handle_field(text_buffer, initial_byte=0, 
                                 field=REG_SIS099_1[0])
        
        if field == '1':
            line = ccf.handle_line(text_buffer, REG_SIS099_1)            
        elif field == '2':
            line = ccf.handle_line(text_buffer, REG_SIS099_2)        
            
        if line:
            line = ccf.remove_invalid_characters(line)
            file_out.write(line + '\n')
