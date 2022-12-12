from client import Client
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

client = Client('http://localhost:5000')

# key_deadbeef = RSA.import_key(client.get_key("deadbeef"))
# cipher = PKCS1_OAEP.new(key_deadbeef)
# encrypted = cipher.encrypt(b'Top secret')
# decrypted = client.send_binary_message('deadbeef', encrypted)

isSigned = True

# send key
public_key_file = open('keys/client2.pub', 'rb')
public_key = public_key_file.read()
public_key_class = RSA.import_key(public_key)
client.send_key('client2', public_key)

# get client1 key

client1_public_key = RSA.import_key(client.get_key('client1'))
cipher_client1 = PKCS1_OAEP.new(client1_public_key)

#get client2 priv key
private_key_file = open('keys/client2.priv', 'rb')
private_key = private_key_file.read()
private_key_class = RSA.import_key(private_key)

# send client1 msg
encrypted_client1 = cipher_client1.encrypt(b'Do client1')
if isSigned:
    hash = SHA256.new("Do client1".encode())
    sig = pkcs1_15.new(private_key_class).sign(hash)
    encrypted_client1 += b"......" +  sig
client.send_binary_message('client1', encrypted_client1)

#get client2 msg
cipher_client2 = PKCS1_OAEP.new(private_key_class)
encrypted_client2 = client.get_binary_message('client2')

if isSigned:
    splitted = encrypted_client2.split(b"......")
    encrypted_client2 = splitted[0]
    decrypted_client2 = cipher_client2.decrypt(encrypted_client2)
    sig = splitted[1]
    hash = SHA256.new(decrypted_client2)
    print(pkcs1_15.new(client1_public_key).verify(hash, sig))

decrypted_client2 = cipher_client2.decrypt(encrypted_client2)
print(decrypted_client2)