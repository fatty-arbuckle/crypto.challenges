#! /usr/bin/python
import sys
import util


input_bytes = bytearray()

with open(sys.argv[1], 'r') as fin:
	for input in fin:
		input_bytes += util.b64ToByteString(input.rstrip())
	print util.decrypt_AES128_ECB(input_bytes, "YELLOW SUBMARINE")
