from passlib.hash import argon2
import base64
hash = '$argon2id$v=19$m=65536,t=3,p=4$4Vzr3bvXWuvdmzMG4PxfCw$NWNunMWdo0ugkWWsL8Z+sdMKnDcJp0vDfMkr30Lmpd4'
hash_params = hash.split('$')[1:]
salt = base64.b64decode(hash_params[3].encode('ascii')+b'==')
hash_argon_specific_params = hash_params[2].split(',')
m = hash_argon_specific_params[0].split('=')[1]
t = hash_argon_specific_params[1].split('=')[1]
p = hash_argon_specific_params[2].split('=')[1]
for i in range(97,123):
    for j in range(97,123):
        password = chr(i)+chr(j)
        encoded = argon2.using(type = 'ID', memory_cost=m, time_cost=t, parallelism=p, salt=salt).hash(password)
        if encoded == hash:
            print(password)


# Dlugo dziala, haslo to wc
