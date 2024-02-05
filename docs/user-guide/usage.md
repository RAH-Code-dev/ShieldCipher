# User Guide

This section provides a guide on how to use the ShieldCipher Python Library for symmetric encryption. It covers the necessary steps for encryption and decryption, key generation, and usage examples.

## Encryption

To encrypt a message using the library, use the `encrypt` function from the `ShieldCipher.encryption.symmetric` module. Ensure that you have the required dependencies installed and handle the generated key, salt, and encrypted data securely.

Example:

```python
from ShieldCipher.encryption.symmetric import encrypt, decrypt

secret = "my_secret_key"
message = "SensitiveData"
algorithm = "AES"
length = 256

encrypted_result = encrypt(secret, message, algorithm, length)
print(encrypted_result)
```

## Decryption

To decrypt a ciphertext, use the `decrypt` function with the secret key, ciphertext, and other optional parameters.

Example:

```python
decrypted_result = decrypt(secret, *encrypted_result)
print(decrypted_result)
```

For more details, explore the functions provided in the library reference.
