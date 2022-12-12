from Crypto.PublicKey import RSA

public_key_name = "client2.priv"
private_key_name = "client2.pub"
rsa_keys = RSA.generate(2048)
pub_key = rsa_keys.public_key()



public_key = rsa_keys.exportKey()
private_key = pub_key.exportKey()
public_file = open(public_key_name, "wb")
private_file = open(private_key_name, "wb")

public_file.write(public_key)
private_file.write(private_key)

