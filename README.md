# ShieldCipher Python Library

The ShieldCipher Python Library provides a command-line interface for encrypting and decrypting text using the ShieldCipher algorithm. The ShieldCipher algorithm is a symmetric encryption algorithm designed to secure text data.

## Installation

To use the ShieldCipher Python Library from PyPi, you can follow these installation steps:

1. Install the library:

   ```bash
   pip install ShieldCipher
   ```

## Installation (latest)

To use the ShieldCipher Python Library from GitHub, you can follow these installation steps:

1. Install the library from github:

   ```bash
   pip install git+https://github.com/RAH-Code-dev/ShieldCipher.git
   ```

## Usage

The ShieldCipher Python Library offers the following command-line actions:

### Encrypt

Encrypts the provided text using the ShieldCipher algorithm.

```bash
ShieldCipher encrypt "text" <options>
```

Options:

- `-a, --algorithm`: Choose the encryption algorithm.
- `-l, --length`: Choose the encryption key length in bits.

Example:

```bash
ShieldCipher encrypt "Hello, World!" -a AES -l 256
```

### Decrypt

Decrypts the provided encrypted text using the ShieldCipher algorithm.

```bash
ShieldCipher decrypt "text"
```

Example:

```bash
ShieldCipher decrypt "AES$256$4a3b2c1d$1a2b3c4d"
```

### Version

Displays the version information for the ShieldCipher library.

```bash
ShieldCipher --version
```

### Help

Displays help information about using the ShieldCipher library.

```bash
ShieldCipher --help
```

## Examples

### Encrypt Example

```bash
ShieldCipher encrypt "SensitiveData" -a AES -l 128
```

This command encrypts the text "SensitiveData" using the DES algorithm with a key length of 128 bits.

### Decrypt Example

```bash
ShieldCipher decrypt "AES$128$4a3b2c1d$1a2b3c4d"
```

This command decrypts the provided encrypted text using the specified algorithm, key length, salt, and message.

## License

This ShieldCipher Python Library is licensed under the MIT License. See the `LICENSE` file for details.

---

**Note:** The ShieldCipher library must be installed before using the command-line interface. Ensure that you have the necessary dependencies and permissions to run the library.
