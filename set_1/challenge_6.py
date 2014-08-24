#! /usr/bin/python
import sys
import util

### ======================================
###
### load the input data

input_bytes = bytearray()

with open(sys.argv[1], 'r') as fin:
	for input in fin:
		input_bytes += util.b64ToByteString(input.rstrip())

### ======================================
###
### Find the likely key sizes

hams = []
for key_size in range(2, 40):
	h = util.ham_n_blocks(input_bytes, 4, key_size)
	hams.append({'key_size': key_size, 'ham': h})

sorted_keys = sorted(hams, key=lambda x: x['ham'])

### ======================================
###
### Try the likely key sizes

best_result = { 'chi': 1000000.0, 'plaintext': "error", 'key': "error" }
limiter = 0
for key in sorted_keys:
	limiter += 1
	if limiter > 10:
		break
		
	key_size = key['key_size']

	## Create blocks of key_size stripes

	block = []
	for i in range(0, key_size):
		block.append([])

	b = 0
	while b < len(input_bytes):
		for i in range(0, key_size):
			if b < len(input_bytes):
				block[i].append(input_bytes[b])
				b += 1

	## Find the best single byte key for each block

	final_key = []
	for i in range(0, key_size):
		k = util.bestSingleXorByte(block[i])
		final_key.append(k)

	## construct a long key to xor against

	xor_bytes = bytearray()
	while len(xor_bytes) < len(input_bytes):
		for l in final_key:
			if len(xor_bytes) < len(input_bytes):
				xor_bytes.append(l)

	## calculate the xor and test the plaintext
	
	tmp = bytearray(util.xorByteArrays(xor_bytes, input_bytes))
	freq = util.letterFrequency(tmp)
	chi = util.chiSquare(freq)
	if (chi < best_result['chi']):
		best_result['chi'] = chi
		best_result['plaintext'] = tmp
		best_result['key'] = final_key

print "Best key: " + str(bytearray(best_result['key'])) + "; plaintext: "
print best_result['plaintext']

