"""Author: Albert Chan

The "I don't know wtf I'm doing but pretend that I know because I took a security class" encryption script.

Also have a taste in string encoding/decoding in the process.

Required Module: PyNaCl

===========================

Usage:

Python3 crypt_lab.py <op> <input_file> <output_file> <key>

- <op>: 0: encode; 1: decode.
- <input_file>: file to be read.
- <output_file>: file to be written to.
- <key>: secret key.
"""

import sys
import base64

import nacl.secret
import nacl.utils
import nacl.encoding
import nacl.hash



############ encrypt/decrypt function #############
def isBase64(s):
    """Check if s is encoded in b64.

    credit to [id0](https://stackoverflow.com/a/45928164)
    
    Arguments:
    s: bytes -- bytes to be check
    
    Returns:
    boolean -- is Base64 or not.
    """
    try:
        if base64.b64encode(base64.b64decode(s)) == s:
            return True;
    except Exception:
        pass;
    return False;

def make_box(key):
    """give a string of key, make a secret box out of it
    
    Arguments:
    key: String -- string of arbitrary length.
    
    Returns:
    SecretBox -- object from pynacl library for crypto operation
    """

    HASHER = nacl.hash.sha256 #hash, to ensure a 32-bytes actual key to be used.
    KEY_MD = HASHER(key.encode(), encoder=nacl.encoding.HexEncoder)  # return somethin like b'abcdef' instead of b'\xab\xcd\xef'
    KEY_MD_DECODE = bytes(bytearray.fromhex(KEY_MD.decode("utf-8")))  # convert to actual bytes
    box = nacl.secret.SecretBox(KEY_MD_DECODE)
    return box

def enc(path_in, path_out, key):
    """Encryption operation
    
    Arguments:
    path_in: str -- path to input plaintext file
    path_out: str -- path to output cipher file
    key: str -- key
    """

    box = make_box(key)
    read_in = ''
    with open(path_in, 'rb') as fr:  #read, binary mode
        read_in = fr.read()

    nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE) #generate nonce
    encrypted = box.encrypt(read_in, nonce) 
    # print(encrypted)
    enc_b64 = base64.b64encode(encrypted)

    with open(path_out, 'wb') as fw:
        fw.write(enc_b64)

    
def dec(path_in, path_out, key):
    """Decryption operation
    
    Arguments:
    path_in: str -- path to input cipher file
    path_out: str -- path to output plaintext file
    key: str -- key
    """
    box = make_box(key)
    read_in = ''
    with open(path_in, 'rb') as fr:  #read, binary mode
        read_in = fr.read()
    if not isBase64(read_in):
        print("Cipher is not in base64 format!")
        return
    read_decoded = base64.b64decode(read_in) #translate from b64 to bytes
    decrypted = box.decrypt(read_decoded)
    # print(encrypted)

    with open(path_out, 'wb') as fw:
        fw.write(decrypted)

############ opcode ##############
if len(sys.argv) < 5:
    print("Usage:")
    print("Python3 crypt_lab.py <op> <input_file> <output_file> <key>")
    print("<op>: 0: encode; 1: decode.")
    print("<input_file>: file to be read.")
    print("<output_file>: file to be written to.")
    print("<key>: secret key.")
elif sys.argv[1] == '0':
    enc(sys.argv[2],sys.argv[3],sys.argv[4])
elif sys.argv[1] == '1':
    dec(sys.argv[2],sys.argv[3],sys.argv[4])
else:
    print('opcode need to be either 0 (encrypt) or 1 (decrypt)')


# box = nacl.secret.SecretBox(KEY_MD_DECODE)

# msg = ''
# with open("./test_plain.txt", 'rb') as fr:
#     msg = fr.read()
#     print(msg)

# with open("./test_crypt.txt", 'wb') as fw:
#     tempstr = b'\x40\x41\x42\x43\x44\x45'
#     fw.write(tempstr)


