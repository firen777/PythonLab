"""Author: Albert Chan

The "I don't know wtf I'm doing but pretend that I know because I took a security class" encryption script.

Also have a taste in string encoding/decoding in the process.

Required Module: PyNaCl
"""

import sys
import nacl.secret
import nacl.utils

import nacl.encoding
import nacl.hash

KEY = b'123456'
HASHER = nacl.hash.sha256

KEY_MD = HASHER(KEY, encoder=nacl.encoding.HexEncoder)  # b'abcdef' instead of b'\xab\xcd\xef' like wtf?
KEY_MD_DECODE = bytes(bytearray.fromhex(KEY_MD.decode("utf-8")))  # convert to actual bytes

print(KEY_MD)
print(bytearray.fromhex(KEY_MD.decode("utf-8")))
print(KEY_MD_DECODE)


string_test = "AYYLMAO_HELLOWORLD\n\n"

box = nacl.secret.SecretBox(KEY_MD_DECODE)

# msg = ''
# with open("./test_plain.txt") as fr:
#     msg = fr.read()
#     print(msg)

