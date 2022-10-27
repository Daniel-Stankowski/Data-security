from passlib.hash import sha1_crypt, sha256_crypt, sha512_crypt, bcrypt, md5_crypt, argon2
import base64
#Wykorzystując nagłówki i przeszukując dokumentację biblioteki odnalazłem odpowiedne algorytmy

file = open('./hashes.txt')
lines = file.readlines()

#1 sha1
sha1_line = lines[0][1:-2]
sha1_param = sha1_line.split('$')[1:]
sha1_encrypted = sha1_crypt.hash("password", salt=sha1_param[2], rounds=int(sha1_param[1]))
if sha1_encrypted == sha1_line:
    print(sha1_encrypted + " <- sha1")
#2 sha256
sha256_line = lines[1][1:-2]
sha256_param = sha256_line.split('$')[1:]
sha256_encrypted = sha256_crypt.hash("password", salt=sha256_param[2], rounds=int(sha256_param[1].split('=')[1]))
if sha256_encrypted == sha256_line:
    print(sha256_encrypted + " <-sha256")
#3 sha512
sha512_line = lines[2][1:-2]
sha512_param = sha512_line.split('$')[1:]
sha512_encrypted = sha512_crypt.hash("password", salt=sha512_param[2], rounds=int(sha512_param[1].split('=')[1]))
if sha512_encrypted == sha512_line:
    print(sha512_encrypted + " <-sha512")
#4 bcrypt 2y
bcrypt_2y_line = lines[3][1:-2]
bcrypt_2y_param = bcrypt_2y_line.split('$')[1:]
bcrypt_2y_encrypted = bcrypt.hash("password", salt=bcrypt_2y_param[2][:22], rounds=int(bcrypt_2y_param[1]), ident="2y")
if bcrypt_2y_encrypted == bcrypt_2y_line:
    print(bcrypt_2y_line + " <-bycrypt in 2y mode")
#5 bcrypt 2b
bcrypt_2b_line = lines[4][1:-2]
bcrypt_2b_param = bcrypt_2b_line.split('$')[1:]
bcrypt_2b_encrypted = bcrypt.hash("password", salt=bcrypt_2b_param[2][:22], rounds=int(bcrypt_2b_param[1]), ident="2b")
if bcrypt_2b_encrypted == bcrypt_2b_line:
    print(bcrypt_2b_line + " <-bycrypt in 2b mode")
#6 md_5 #1
md5_1_line = lines[5][1:-2]
md5_1_param = md5_1_line.split('$')[1:]
md5_1_encrypted = md5_crypt.hash("password", salt=md5_1_param[1])
if md5_1_encrypted == md5_1_line:
    print(md5_1_line + " <-md5_1")
#7 md_5 #2
md5_2_line = lines[6][1:-2]
md5_2_param = md5_2_line.split('$')[1:]
md5_2_encrypted = md5_crypt.hash("password", salt=md5_2_param[1])
if md5_2_encrypted == md5_2_line:
    print(md5_2_line + " <-md5_2")
#8 argon2
argon2_line = lines[7][1:-1]
argon2_param =argon2_line.split('$')[1:]
argon2_specific_params = argon2_param[2].split(',')
salt = base64.b64decode(argon2_param[3].encode('ascii')+b'==')
argon2_encrypted =argon2.using(type='ID', memory_cost=int(argon2_specific_params[0].split('=')[1]), time_cost=int(argon2_specific_params[1].split('=')[1]), parallelism = int(argon2_specific_params[2].split('=')[1]), salt=salt).hash("password")
if argon2_encrypted == argon2_line:
    print( argon2_line + " <-argon2")

# biblioteki: passlib, bcrypt, argon2_cffi (base64 powinno byc basicowo).
# $sha1$4294967$OOUilDcFFMLNREMDzF8j$KzWuoXraHudEvpjlcnAZu51Oe5bh <- sha1
# $5$rounds=535454$HqGH/NKcuIcQnTat$XTYMrolDMlq0jTvE2M5HlEvRcpABiDEj0W1OOhWvwV5 <-sha256
# $6$rounds=645656$WvRRFY4mM9EalwJ1$CaR3PCwL5avpBFWVbIj8jsYmVN3fdDDflOprSYdcDyUHO3uJjuOoZppaulWs.vr1UdVTOqU6MvCSSyQBtmuVq1 <-sha512
# $2y$09$dLHDaBvnZcjNkt7CluXkvedRjqxufJFXcKhRxSZeWJiErlA12Fq1G <-bycrypt in 2y mode
# $2b$13$e9NUzhfBF1.QHnvORw5S6.WHEagqTLcXbazCIKnBxuYR6bBynkD4S <-bycrypt in 2b mode
# $1$A/Fz53gT$XaFVcCJGiwMqiEP.Jqfv61 <-md5_1
# $1$NOj3d3M$sDSgbCpgQK.5ey9mMjFnk/ <-md5_2
# $argon2id$v=19$m=1654,t=5,p=2$zJnTeg/BmHOOMaYU4hxjDA$wrCvr93+Ba/cl119NAic2lX5usaKCCdlsNVZHsoRmtE <-argon2