#! /usr/bin/python
import string
import sys

INPUT="Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
XOR_STRING="ICE"
EXPECT="0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

# hex string generator
def byteArrayToHexString(byteArray):
	hex = []
	for i in xrange(0, len(byteArray)):
		hex.append(format(byteArray[i], '02x'))
	return "".join(hex)

# byte array generator
def hexStringToByteArray(hexString, byteSize=2):
	for i in xrange(0, len(hexString), byteSize):
		yield int(hexString[i:i+byteSize], 16)

# xor generator
def xorByteArrays(first, second):
	assert len(first) == len(second)
	for i in range(0, len(first)):
		yield first[i] ^ second[i]


key = XOR_STRING
while len(key) < len(INPUT):
	key += XOR_STRING

extra = 0 - (len(key) - len(INPUT))
if (extra < 0):
	key = key[:extra]

input_bytes = bytearray(INPUT)
key_bytes = bytearray(key)

cipher_bytes = bytearray(xorByteArrays(input_bytes, key_bytes))

cipher = byteArrayToHexString(cipher_bytes)
print cipher

if cipher == EXPECT:
	print "Success!"
