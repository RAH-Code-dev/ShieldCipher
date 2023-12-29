from Crypto.Cipher import AES
from Crypto.Hash import SHA512
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

def encrypt_aes256(key, message):
    """
    The function encrypts a message using the AES encryption algorithm with a given key.
    
    :param key: The key parameter is the encryption key used to encrypt the message. It should be a byte
    string of length 16, 24, or 32, corresponding to AES-128, AES-192, or AES-256 encryption
    respectively
    :param message: The `message` parameter is the plaintext message that you want to encrypt. It should
    be a string
    :return: the encrypted password, which includes the nonce, ciphertext, and tag.
    """
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
    return nonce + ciphertext + tag

def decrypt_aes256(key, ciphertext):
    """
    The function `decryptPassword` takes a key and a ciphertext as input, decrypts the ciphertext using
    AES encryption, and returns the plaintext password if the decryption is successful, otherwise it
    returns None.
    
    :param key: The key parameter is the encryption key used to encrypt the plaintext. It should be a
    byte string of length 16, 24, or 32, corresponding to AES-128, AES-192, or AES-256 encryption
    respectively
    :param ciphertext: The `ciphertext` parameter is the encrypted message that needs to be decrypted.
    It is a byte string that contains the encrypted data
    :return: the decrypted plaintext as a string if the decryption is successful. If the decryption
    fails, it returns None.
    """
    nonce = ciphertext[:16]
    tag = ciphertext[-16:]
    ciphertext = ciphertext[16:-16]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('utf-8')
    except ValueError:
        return None

def compute_key(secret, salt):
    password = secret.encode()
    key = PBKDF2(password, salt, 32, count=1000000, hmac_hash_module=SHA512)
    return key

def encrypt(secret, message):
    salt = get_random_bytes(16)
    key = compute_key(secret, salt)
    encrypted_text = encrypt_aes256(key, message)

    return salt + encrypted_text

def decrypt(secret, ciphertext):
    salt = ciphertext[:16]
    key = compute_key(secret, salt)

    decrypted_text = decrypt_aes256(key, ciphertext[16:])

    return decrypted_text
