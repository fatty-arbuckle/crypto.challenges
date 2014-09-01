#! /usr/bin/python

import string
import util

INPUT = "YELLOW SUBMARINE"
EXPECTED = "YELLOW SUBMARINE\x04\x04\x04\x04"


input_bytes = bytearray(util.stringToByteArray(INPUT))

util.pkcs7PadByteArray(input_bytes, 20)

print input_bytes
print EXPECTED

if input_bytes == EXPECTED:
	print "Success"
