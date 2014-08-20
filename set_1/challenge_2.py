#! /usr/bin/python

INPUT="1c0111001f010100061a024b53535009181c"
XOR="686974207468652062756c6c277320657965"
EXPECT="746865206b696420646f6e277420706c6179"

# byte string generator
def byteArrayToByteString(byteArray):
	for i in xrange(0, len(byteArray)):
		yield format(byteArray[i], 'x')

# byte array generator
def byteStringToByteArray(byteString, byteSize=2):
	for i in xrange(0, len(byteString), byteSize):
		yield int(byteString[i:i+byteSize], 16)

# xor generator
def xorByteArrays(first, second):
	assert len(first) == len(second)
	for i in range(0, len(first)):
		yield first[i] ^ second[i]

input_bytes = bytearray(byteStringToByteArray(INPUT))
xor_bytes = bytearray(byteStringToByteArray(XOR))
result = "".join(list(byteArrayToByteString(bytearray(xorByteArrays(input_bytes, xor_bytes)))))

print result
print EXPECT


if result == EXPECT:
	print "Success!"
