from base64 import decode, encode
from operator import mod
from Cryptodome.Cipher import ARC4
ARC4.key_size = range(3, 257)

text = "Bardzo tajny kod"
key = "OwO"

def prepare_to_permutation(key):
    d = len(key)
    S = [0] * 256
    for i in range(256):
        S[i] = i
    j = 0
    for i in range(256):
        j = (j + S[i] + ord(key[i % d])) % 256
        S[j], S[i] = S[i], S[j]
    return S

def my_encode(key, data):
    encoded_data = ""
    data_size_in_bytes = len(data)
    S = prepare_to_permutation(key)
    i = 0
    j = 0
    m = 0
    while m < data_size_in_bytes:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[j], S[i] = S[i], S[j]
        encoding_byte = S[(S[i] + S[j]) % 256]
        encoded_data += str(hex(ord(data[m]) ^ encoding_byte)) + " "
        m = m + 1
    return encoded_data

def my_decode(key, data):
    decoded_data = ""
    splitData = data.split()
    data_size_in_bytes = len(splitData)
    S = prepare_to_permutation(key)
    i = 0
    j = 0
    m = 0
    while m < data_size_in_bytes:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[j], S[i] = S[i], S[j]
        encoding_byte = S[(S[i] + S[j]) % 256]
        decoded_data += str(chr(int(splitData[m], 16) ^ encoding_byte))
        m = m + 1
    return decoded_data
    
encrypted = my_encode(key, text)
decrypted = my_decode(key, encrypted)
print("Moj algorytm")
print(encrypted)
print(decrypted)
arc4 = ARC4.new(key.encode())
encrypted = arc4.encrypt(text.encode())
arc4 = ARC4.new(key.encode())
decrypted = arc4.encrypt(encrypted)
print("Algorytm biblioteczny")
print(encrypted)
print(decrypted)