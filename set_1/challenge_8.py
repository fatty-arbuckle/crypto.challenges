#! /usr/bin/python
import sys
import util

hams = []
line = 0
with open(sys.argv[1], 'r') as fin:
	for input in fin:
		line += 1
		input_bytes = bytearray(util.hexStringToByteArray(input.rstrip()))
		key_size = 16
		h = util.ham_n_blocks(input_bytes, 8, key_size)
		hams.append({'line': line, 'bytes': input.rstrip(), 'ham': h})

sorted_keys = sorted(hams, key=lambda x: x['ham'])

print "Line " + str(sorted_keys[0]['line']) + " (" + str(sorted_keys[0]['bytes']) + ")"

