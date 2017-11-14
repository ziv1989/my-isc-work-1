#! /bin/env python
#ncas-isc example 4 for reading and writing binary files

import struct

bin_data=struct.pack("bbbb",123,12,45,34)
with open('mybinary.dat','wb') as writer:
    writer.write(bin_data)

with open('mybinary.dat','r') as reader:
    bin_data2=reader.read()
    data=struct.unpack("bbbb",bin_data2)
    print data