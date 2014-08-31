#! /usr/bin/python
import sys
from Crypto.Cipher import AES
import util


def decrypt_AES128_ECB(ciphertext, password):
	assert len(ciphertext) % 16 == 0
	assert len(password) == 16
	bs = AES.block_size
	cipher = AES.new(password, AES.MODE_ECB)
	plaintext = cipher.decrypt(str(ciphertext))
	return plaintext

input_bytes = bytearray()

with open(sys.argv[1], 'r') as fin:
	for input in fin:
		input_bytes += util.b64ToByteString(input.rstrip())
	print decrypt_AES128_ECB(input_bytes, "YELLOW SUBMARINE")
