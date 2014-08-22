#! /usr/bin/python
import string
import sys
import base64

def b64ToByteString(b64):
	return base64.b64decode(b64)

def hexStringToByteArray(hexString):
	return stringToByteArray(hexString, 2, lambda x: int(x, 16))

def stringToByteArray(s, byteSize=1, convert=lambda x: ord(x)):
	for i in xrange(0, len(s), byteSize):
		yield convert(s[i:i+byteSize])

def calcHamming(a, b):
	assert len(a) == len(b)
	ham = 0
	for i in xrange(0, len(a)):
		v = a[i] ^ b[i]
		while v > 0:
			ham += 1
			v &= v - 1
	return ham

input_bytes = bytearray()

with open(sys.argv[1], 'r') as fin:
	for input in fin:
		input_bytes += b64ToByteString(input.rstrip())

hams = []
for key_size in range(2, 40):
	block_a = input_bytes[0:key_size]
	block_b = input_bytes[key_size:2 * key_size]
	nHam = calcHamming(block_a, block_b) / key_size
	hams.append({'key_size': key_size, 'ham': nHam})

s = sorted(hams, key=lambda x: x['ham'])
best_key_size = s[0]['key_size']

print best_key_size

