from BMPcrypt import encrypt_data
from BMPcrypt import encrypt_full

encrypt_data("demo24.bmp", "CBC", b"x" * 16) 
encrypt_data("demo24.bmp", "ECB", b"x" * 16)

# różnice ECB vs CBC: w ECB można się domyślić jaki był mniej więcej kształt w niektórych przypadkach, w CBC nie
# dzieje się tak dlatego, że ECB szyfruje tylko na podstawie klucza przez co bloki wyglądające tak samo wyglądają tak 'samo'(po zaszyfrowaniu)
#w CBC do szyfrowania używa się też poprzedniego bloku przez co takie same bloki nie zostają zaszyfrowane w taki sam sposób