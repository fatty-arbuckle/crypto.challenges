#! /usr/bin/python
import string
import sys

# from http://en.wikipedia.org/wiki/Letter_frequency
ENGLISH_LETTER_FREQUENCY = [ 
	 .8167,  .1492,  .2782,  .4253, 1.2702,
	 .2228,  .2015,  .6094,  .6966,  .0153,
	 .0772,  .4025,  .2406,  .6749,  .7507,
	 .1929,  .0095,  .5987,  .6327,  .9056,
	 .2758,  .0978,  .2360,  .0150,  .1974,
	 .0074,  .0001 ]

NON_PRINTABLE_INDEX=26

# hex string generator
def byteArrayToHexString(byteArray):
	for i in xrange(0, len(byteArray)):
		yield format(byteArray[i], 'x')

# byte array generator
def hexStringToByteArray(hexString, byteSize=2):
	for i in xrange(0, len(hexString), byteSize):
		yield int(hexString[i:i+byteSize], 16)

# xor generator
def xorByteArrays(first, second):
	assert len(first) == len(second)
	for i in range(0, len(first)):
		yield first[i] ^ second[i]


# get letter frequency (plus non-printables and average work length
def letterFrequency(input):
	count = len(input)
	freq = [ 0.0 ] * len(ENGLISH_LETTER_FREQUENCY)
	for i in range(0, len(input)):
		if chr(input[i]).isalpha():
			freq[ord(chr(input[i]).lower()) - ord('a')] += 1.0
		if chr(input[i]) not in string.printable:
			freq[NON_PRINTABLE_INDEX] += count*10000
	for i in range(0, len(freq)):
		freq[i] /= count
	return freq

# chiSquare compare
def chiSquare(observed, expected):
	assert len(observed) == len(expected)
	sum = 0.0
	for i in range(0, len(observed)):
		sum += ( (observed[i] - expected[i])**2 ) / expected[i]
	return sum


winner = { 'input': 'none', 'key': 'none', 'text': 'empty', 'freq': [], 'chi': 10000 }

with open(sys.argv[1], 'r') as fin:
	for input in fin:

		input_bytes = bytearray(hexStringToByteArray(input.rstrip()))

		chiMap = {}
		for xorByte in range(0, 256):
			key = bytearray()
			while (len(key) < len(input_bytes)):
				key.append(xorByte)
			tmp = bytearray(xorByteArrays(input_bytes, key))
			freq = letterFrequency(tmp)
			chi = chiSquare(freq, ENGLISH_LETTER_FREQUENCY)
			chiMap[xorByte] = {'input': input.rstrip(), 'key': xorByte, 'text': tmp, 'freq': freq, 'chi': chi }

		results = sorted(chiMap.iteritems(), key=lambda kvt: kvt[1]['chi'])
		contender = results[0][1]
		if contender['chi'] < winner['chi']:
			winner = contender

print "INPUT: " + winner['input'] + "; KEY: " + str(winner['key']) + "; YIELDS: " + winner['text']
		
