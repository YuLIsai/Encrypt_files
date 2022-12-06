from cryptography.fernet import Fernet
#from fpdf import FPDF
import os


class Encrypt_files:

    def generate_keys(self):
        os.makedirs("../files/keys", exist_ok=True)
        key = Fernet.generate_key()
        with open('../files/keys/key.key', 'wb') as keym:
            keym.write(key)

    def enc_files(self):
        with open('../files/keys/key.key', 'rb') as key:
            fernet_key = key.read()
        fernet_enc = Fernet(fernet_key)
        with open('../files/messages.txt', 'rb') as message_file:
            message = message_file.read()
        encrypted = fernet_enc.encrypt(message)

        os.makedirs("../files/enc", exist_ok=True)
        with open('../files/enc/enc_messages.enc', 'wb') as enc:
            enc.write(encrypted)

    def decypt_files(self):
        with open('../files/keys/key.key', 'rb') as key:
            fernet_key = key.read()
        fernet_enc = Fernet(fernet_key)
        with open('../files/enc/enc_messages.enc', 'rb') as dec_:
            encrypted = dec_.read()

        decrypted = fernet_enc.decrypt(encrypted)

        with open('../files/messages_dec.txt', 'wb') as backOriginal:
            message = backOriginal.write(decrypted)

#e = backOriginal.write(decrypted)

#

#    def to_pdf(self):

#        pdf = FPDF()

#        re = open('../files/enc/enc_messages.enc', 'r')

#        pdf.add_page()

#        pdf.set_font("Arial", size=15)

#        line =1

#        for linea in re:

#            pdf.cell(900,7,txt=linea, ln=line, align="L")

#            if linea[-1] == ("\n"):

#                linea = linea[:-1]

#            line=+1

#        pdf.output("..
def opc():
    enc = Encrypt_files()

    opcr = input(
        "Select the optionn that you needs\n opc 1: generar llaves (keys -g)\n opc 2: cifrar archivos (files -e)\n")
        
    if (opcr == "keys -g"):
        enc.generate_keys()
    elif (opcr =="files -e"):
        enc.enc_files()

  #  match opcr:
#        case "keys -g":
#            enc.generate_keys()
#        case "files -e":
#            enc.enc_files()
#        case "files -d":
#            enc.decypt_files()
#      #        case "files -d":

#            e
#        case _:
#            print("The option isn't here, please select an option available")


for i in range(3):
    opc()
