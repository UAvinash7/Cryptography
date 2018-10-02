import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

random_generator = Random.new().read

# Bob generates a key pair which contains a public key and a private key
keyPair = RSA.generate(1024, random_generator)
publicKey = keyPair.publickey()

# Alice
plainText = "Hello World"
encryptedText = publicKey.encrypt(plainText, 32)
print "Encrypted Text: " + str(encryptedText)

# Bob
decryptedText = keyPair.decrypt(ast.literal_eval(str(encryptedText)))
print "Decrypted Text: " + decryptedText