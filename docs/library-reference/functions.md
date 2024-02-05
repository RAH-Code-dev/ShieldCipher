# Library Reference: Functions

This section provides detailed information about the functions available in the ShieldCipher Python Library for symmetric encryption.

## `ShieldCipher.encryption.symmetric.encrypt_aes(key, message)`

Encrypts a message using the AES encryption algorithm with a given key.

- **Parameters:**
  - `key`: The encryption key (byte string) of length 16, 24, or 32, corresponding to AES-128, AES-192, or AES-256 encryption.
  - `message`: The plaintext message (string) to be encrypted.

- **Returns:**
  - A byte string representing the encrypted password, including the nonce, ciphertext, and tag.

## `ShieldCipher.encryption.symmetric.decrypt_aes(key, ciphertext)`

Decrypts a ciphertext using the AES encryption algorithm with a given key.

- **Parameters:**
  - `key`: The encryption key (byte string) of length 16, 24, or 32, corresponding to AES-128, AES-192, or AES-256 encryption.
  - `ciphertext`: The encrypted message (byte string) to be decrypted.

- **Returns:**
  - The decrypted plaintext as a string if the decryption is successful. Returns `None` if the decryption fails.

## `ShieldCipher.encryption.symmetric.compute_key(secret, salt, length=32)`

Generates a key using the PBKDF2 algorithm with SHA512 as the HMAC hash module.

- **Parameters:**
  - `secret`: The password or passphrase (string) used to generate the key.
  - `salt`: A random value (byte string) added to the secret before hashing.
  - `length`: The desired length of the key in bytes (default is 32).

- **Returns:**
  - The generated key as a byte string.

## `ShieldCipher.encryption.symmetric.encrypt(secret, message, algorithm='AES', length=256)`

Encrypts a message using a specified algorithm and key length.

- **Parameters:**
  - `secret`: The string used as input to compute the encryption key.
  - `message`: The text or data to be encrypted.
  - `algorithm`: The encryption algorithm to be used (default is 'AES').
  - `length`: The length of the encryption key in bits (default is 256).

- **Returns:**
  - A tuple containing the algorithm used for encryption, the length of the encryption key, the salt used for encryption, and the encrypted text.

## `ShieldCipher.encryption.symmetric.decrypt(secret, ciphertext, salt, algorithm='AES', length=256)`

Decrypts a ciphertext using a secret key and specified encryption algorithm and key length.

- **Parameters:**
  - `secret`: The string used as input to compute the encryption key.
  - `ciphertext`: The encrypted text to be decrypted.
  - `salt`: A random value used as an additional input to the key derivation function.
  - `algorithm`: The encryption algorithm to be used for decryption (default is 'AES').
  - `length`: The length of the encryption key to be used (default is 256).

- **Returns:**
  - The decrypted text as a string.
