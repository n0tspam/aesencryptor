from base64 import b64encode, b64decode
import sys
from Crypto.Cipher import AES
from os import urandom
import hashlib
import chardet

KEY = urandom(16)

def pad(s):
    #print(s)
    #print("type of s: ", type(s))
    #print("AES Blocksize: ", str(AES.block_size))
    #print("length of param: ", len(s))
    #print("first half: ", type(AES.block_size - len(s) % AES.block_size))
    #print("second half ", type(AES.block_size - len(s) % AES.block_size))
    return s + ((AES.block_size - (len(s) % AES.block_size)) * bytes(chr(AES.block_size - (len(s) % AES.block_size)), 'utf-8' ))

def aesenc(plaintext, key):
    k = hashlib.sha256(key).digest()
    iv = 16 * b'\x00'
    #print("type of key: ", type(k))
    #print("type of iv: ", type(iv))
    plaintext = pad(plaintext)
    #print(plaintext)
    #print("printing type before encrypting", type(plaintext))
    #print("length of plaintext: ", len(plaintext))
    cipher = AES.new(k, AES.MODE_CBC, iv)
    return cipher.encrypt(plaintext)


try:
    plaintext = open(sys.argv[1], "rb").read()
except Exception as e:
    print(e)
    print("File argument needed! %s <raw payload file>" % sys.argv[0])
    sys.exit()

ciphertext = aesenc(plaintext, KEY)
#print('key: ', KEY)
#print('ciphertext: ', ciphertext)
print('AESkey[] = { 0x' + ', 0x'.join(hex(x)[2:] for x in KEY) + ' };')
print('payload[] = { 0x' + ', 0x'.join(hex(x)[2:] for x in ciphertext) + ' };')
