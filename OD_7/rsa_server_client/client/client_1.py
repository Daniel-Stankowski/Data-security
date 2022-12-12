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

public_key_file = open('keys/client1.pub', 'rb')
public_key = public_key_file.read()
public_key_class = RSA.import_key(public_key)
client.send_key('client1', public_key)

# get client2 key

client2_public_key = RSA.import_key(client.get_key('client2'))
cipher_client2 = PKCS1_OAEP.new(client2_public_key)

#get client1 priv key
private_key_file = open('keys/client1.priv', 'rb')
private_key = private_key_file.read()
private_key_class = RSA.import_key(private_key)

# send client2 msg
encrypted_client2 = cipher_client2.encrypt(b'Do client2')
if isSigned: # polega na wysłaniu sygnatury wiadomości, która jest hashem zakodowanym przy pomocy klucza publicznego
    hash = SHA256.new("Do client2".encode())
    sig = pkcs1_15.new(private_key_class).sign(hash)
    encrypted_client2 += b"......" +  sig
client.send_binary_message('client2', encrypted_client2)



#get client1 msg
cipher_client1 = PKCS1_OAEP.new(private_key_class)
encrypted_client1 = client.get_binary_message('client1')


if isSigned: #sprawdzenie polega na porównanie odkodowanej sygnatury i odkodowanej wiadomości
    splitted = encrypted_client1.split(b"......")
    encrypted_client1 = splitted[0]
    decrypted_client1 = cipher_client1.decrypt(encrypted_client1)
    sig = splitted[1]
    hash = SHA256.new(decrypted_client1)
    print(pkcs1_15.new(client2_public_key).verify(hash, sig))

decrypted_client1 = cipher_client1.decrypt(encrypted_client1)
print(decrypted_client1)