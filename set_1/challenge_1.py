#! /usr/bin/python

INPUT="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
EXPECT="SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
BASE64_TABLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# bytes generator
def byteStringToByteArray(byteString, byteSize=2):
	for i in xrange(0, len(byteString), byteSize):
		yield int(byteString[i:i+byteSize], 16)

# b64 generator
def byteArrayToBase64(bytes):
	for i in xrange(0, len(bytes), 3):
		bits = "{:08b}".format(int(bytes[i]))
		try:
			bits += "{:08b}".format(int(bytes[i+1]))
			bits += "{:08b}".format(int(bytes[i+2]))
		except IndexError:
			print "IndexError: " + str(len(bits))
			if len(bits) == 8:
				bits += "0000"
			if len(bits) == 16:
				bits += "00"
		for j in xrange(0, len(bits), 6):
			yield BASE64_TABLE[int(bits[j:j+6], 2)]
		if len(bits) == 12:
			yield '='
			yield '='
		if len(bits) == 18:
			yield '='

bytes = bytearray(byteStringToByteArray(INPUT))
b64 = "".join(list(byteArrayToBase64(bytes)))

print b64
print EXPECT


if b64 == EXPECT:
	print "Success!"
