from Cryptodome.Cipher import AES
from itertools import *
from Cryptodome.Util.Padding import pad

f = open("security_ECB_encrypted.bmp","rb")
cryptogram = f.read()
cryptogram = pad(cryptogram,16)


for i in list(range(97, 123)):
    password = chr(i)*16
    cipher = AES.new(password.encode("latin1"), AES.MODE_ECB)
    decrypted = cipher.decrypt(cryptogram)
    decrypted_decoded = decrypted.decode("latin1")
    file = open('security_ECB_decrypted.bmp', 'wb')
    if decrypted_decoded.find("BM") == 0:
        print(chr(i)*16)
        file.write(decrypted)
        file.close()
        break
    

