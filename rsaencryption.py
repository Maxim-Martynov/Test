from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import base64
def generation():
    privatekey = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    publickey = privatekey.public_key()
    return privatekey, publickey
def shifr_message(publickey, message):
    shifr = publickey.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return shifr
def deshifr_message(privatekey, shifrmessage):
    deshifr = privatekey.decrypt(
        shifrmessage,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return deshifr.decode()
mes = input()
privatekey, publickey = generation()
shifrmessage = shifr_message(publickey, mes)
shifrmessage_base64 = base64.b64encode(shifrmessage).decode()
lenmessage = len(shifrmessage_base64)
deshifrmessage = deshifr_message(privatekey, shifrmessage)
print(f'Длина зашифрованного сообщения: {lenmessage}')
print(f"Зашифрованное сообщение (base64): {shifrmessage_base64}")
print(f"Расшифрованное сообщение: {deshifrmessage}")

