import sys
from ShieldCipher.encryption.symmetric import encrypt as sc_encrypt, decrypt as sc_decrypt
from getpass import getpass
import binascii

def msc():
    print("                     .                    .                           ")
    print("                :-:--=:-:::.             :=-**##*=:                   ")
    print("                 :=----------.         .-%@@@@@@@@@%:                 ")
    print("                :-------------:        :@@@@@@@@@@@@%.                ")
    print("               :-=-----------==:       +@@@@@@@@@@@@@#                ")
    print("              :=-=-------===-=--      .+%@@@@@@@@@@@#=                ")
    print("             .------------=------.     =@@@@@@@@@@@@@#                ")
    print("               --=--------==-=-.       -*%@@@@@@@@@*-.                ")
    print("                  ::----===+-             .#%@@@@*.                   ")
    print("                     -+++=: .               :+##+                     ")
    print("                    -+=====.              .=%@@%%%#=                  ")
    print("                 :-----------:.        :+#%%%@@@@@%@%+-               ")
    print("               -----------------      -%%%%%@@@%@@%%@%%*              ")
    print("              .-==----------==--:     #%%%@%@@@@@@@@@@%%.             ")
    print("              :-=+----------*=---    =%%%@@%%@@@%%@@@%%%=             ")
    print("              ---=----------*----:  .#%%%@@%%@@@%@%@@%%%%             ")
    print("             :-===----------+=---=  -#%%%@@%%@%@%@%@@%%%%=            ")
    print("               --=----------=#==+.   ==+%@@%%@@@%@%@@*++.             ")
    print("               --=-----------*=---  :===#@@%%@@@%@%%%--=              ")
    print("               -==-----------++--=  ---:#@%@@@%%%@@@%--=              ")
    print("               -=------------=:--=. =-- %@%%%%%%@%%%@=-=              ")
    print("              .-+-------------.:---.--: %%%%%%%%@%%@@+==              ")
    print("              :-++*++++++*+***. --=+--  *###########**-=              ")
    print("              --*+++++++++*+++: :--*-: :------=------*-=              ")
    print("              =-*++++++++*+***- .--*-. :-------------+-=              ")
    print("             .--*+++=+*++*+***+ :==*=: -------=------===:             ")
    print("             :=+++++==+++*++**+ -*++=. -------+-------+=:             ")
    print("              -++++=+==**+++***  :-:   -------+-------+.              ")
    print("               -+++=++=****+**#        -------+=------=               ")
    print("               .++==*=---=*+**+        =------+*------=               ")
    print("                ----=    :---=          ====-.::+====                 ")
    print("           :**#==---=:   ----= ..   .:::=--=+*%#*--=+***. .--:..      ")
    print("           .=+**#=--==   :=--=%@*:.-=+%%*--=: ::+=--+***+=#@%*-=-::.  ")
    print("               :+=--=. :::=--=:.-*#%*--=*---+-+**=--=--=+**+*=**%@%=  ")
    print("                 =--= .#%%=--=.  +*#%#= +---#%++#=---.+%@%+  .+++*+-  ")
    print("                 ====   .:+===:   -==+= :===*+: -==== .--:.      ..   ")
    print("                 =--=     ----:         .----   :=---                 ")
    print("                 ----     :---:         .=---   .=---                 ")
    print("                 ----     :---:         .=---    =---                 ")
    print("                 ---:     :---:         .=---    +---                 ")
    print("                 +##%.    =*##-         -%%#:    %%%#                 ")
    print("                :@@@@-    #@@@+         %@@@*   :@@@%:                ")
    print("                .====.    -++=:         =+==-    --==.                ")
    print("\n@milosnowcat\n")

def encrypt(args):
    if not args:
        msc()
        return "Usage: ShieldCipher crypt \"text\""
        
    secret = getpass()
    encrypted_text = sc_encrypt(secret, args[0])

    encrypted_text_algorithm = encrypted_text[0]
    encrypted_text_length = str(encrypted_text[1])
    encrypted_text_salt = binascii.hexlify(encrypted_text[2]).decode('utf-8')
    encrypted_text_msg = binascii.hexlify(encrypted_text[3]).decode('utf-8')

    return encrypted_text_algorithm + '$' + encrypted_text_length + '$' + encrypted_text_salt + '$' + encrypted_text_msg

def decrypt(args):
    if not args:
        msc()
        return "Usage: ShieldCipher crypt \"text\""
        
    secret = getpass()
    encrypted_text = args[0]

    encrypted = encrypted_text.split('$')
    algorithm = encrypted[0]
    length = int(encrypted[1])
    salt = binascii.unhexlify(encrypted[2].encode('utf-8'))
    hashed = binascii.unhexlify(encrypted[3].encode('utf-8'))

    decrypted_text = sc_decrypt(secret, hashed, salt, algorithm, length)

    return decrypted_text

def main():
    if len(sys.argv) < 2:
        msc()
        print("Usage: --help")
        sys.exit(1)

    action = sys.argv[1]

    if action == "--version":
        msc()
        print("ShieldCipher Version 1.0.0")
        sys.exit(0)
    elif action == "--help":
        msc()
        print("Usage: ShieldCipher <action> [args]")
        print("Actions:")
        print("  encrypt        Encrypts the provided text")
        print("  decrypt      Decrypts the provided text")
        print("  --version    Displays the version information")
        print("  --help       Displays this help message")
        sys.exit(0)

    args = sys.argv[2:]

    if action == "encrypt":
        result = encrypt(args)
        print(result)
    elif action == "decrypt":
        result = decrypt(args)
        print(result)
    else:
        print("Invalid action. Use '--help'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
