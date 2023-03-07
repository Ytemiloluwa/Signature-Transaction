# This is a simple Python script to sign and validate data using ellptic curve cryptography.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#PATH="/Library/Frameworks/Python.framework/Versions/3.7/bin:${PATH}"

from ecdsa import SigningKey, SECP256k1

sk = SigningKey.generate(curve=SECP256k1)

# public or verifying key
vk = sk.verifying_key

# signing a message
signature = sk.sign(b"Not your keys, not your coins")



