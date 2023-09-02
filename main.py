# TODO hacer un programa en terminal para guardar claves,
# usara una clave maestra para encriptar las claves,
# copiara la clave al portapaeles para no mostrarla en la terminal,
# podra generar claves aleatorias

import utils

def createPassword(secret):
    while 1:
        print("\nCreate password options:")
        print("(1) add password")
        print("(2) generate random password")
        print("(99) return\n")

        option = input(":")

        if option == '1':
            utils.addPassword(secret, utils.askData(), utils.askPassword("Password: "))
        elif option == '2':
            utils.addPassword(secret, utils.askData(), utils.newPassword())
        elif option == '99':
            break

def readPassword(secret):
    while 1:
        print("\nRead password options:")
        print("(1) show all passwords")
        print("(2) search password")
        print("(99) return\n")

        option = input(":")

        if option == '1':
            utils.getPassword(secret, [])
        elif option == '2':
            utils.getPassword(secret, utils.askData())
        elif option == '99':
            break

def main():
    db = utils.dbconfig()
    secret = utils.checkMaster()

    while 1:
        print("\nChoose an option:")
        print("(c)reate password")
        print("(r)ead password")
        print("(u)pdate password")
        print("(d)elete password")
        print("(q)uit\n")

        option = input(":")

        if option == 'c':
            createPassword(secret)
        elif option == 'r':
            readPassword(secret)
        elif option == 'q':
            break

main()
