import string
import base64
from Crypto.Cipher import AES



def b64ToByteString(b64):
	return base64.b64decode(b64)

def hexStringToByteArray(hexString):
	return stringToByteArray(hexString, 2, lambda x: int(x, 16))

def stringToByteArray(s, byteSize=1, convert=lambda x: ord(x)):
	for i in xrange(0, len(s), byteSize):
		yield convert(s[i:i+byteSize])

def pkcs7PadByteArray(s, block_size):
	while len(s) % block_size != 0:
		s.append(0x04)

