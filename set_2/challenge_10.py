#! /usr/bin/python

import sys
import util

expected = bytearray()

with open(sys.argv[1], 'r') as fin:
	for input in fin:
		expected += util.b64ToByteString(input.rstrip())

plaintext = util.decrypt_AES128_CBC(expected, "YELLOW SUBMARINE", [0] * 16)
ciphertext = util.encrypt_AES128_CBC(plaintext, "YELLOW SUBMARINE", [0] * 16)

if ciphertext == expected:
	print "SUCCEEDED"

