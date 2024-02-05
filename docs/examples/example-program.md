# Example Program

This section provides an example program showcasing the usage of the ShieldCipher Python Library for symmetric encryption. The example demonstrates how to encrypt and decrypt a message using the library functions.

```python
from ShieldCipher.encryption.symmetric import encrypt, decrypt

# Encryption Example
secret = "my_secret_key"
message = "SensitiveData"
algorithm = "AES"
length = 256

encrypted_result = encrypt(secret, message, algorithm, length)
print(encrypted_result)

# Decryption Example
decrypted_result = decrypt(secret, *encrypted_result)
print(decrypted_result)
```

Ensure that you have the required dependencies installed before running the example.
