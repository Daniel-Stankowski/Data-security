from math import log2

entropy = 32*log2(2**8)
password_entropy = entropy/log2(26)
print ("Password should have at least " + str(int(password_entropy)+1) + " characters.")
print (password_entropy)

# from Cryptodome.Cipher import ARC4
# from Cryptodome.Protocol.KDF import PBKDF2
# from Cryptodome.Hash import SHA512
# from Cryptodome.Random import get_random_bytes


# def shannon_entropy(string):
#     entropy = 0.0
#     size = len(string)
#     for i in range(256):
#         prob = string.count(chr(i))/size
#         if prob > 0.0:
#             entropy += prob * log2(prob)
#     return -entropy

# password = PBKDF2("bardzotajnehaslo", get_random_bytes(16), 32, count=10000000, hmac_hash_module=SHA512).decode('latin1');
# entropy = shannon_entropy(password)
# print(entropy)
# print(32*log2(26))