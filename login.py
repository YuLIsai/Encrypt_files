import sys
from getpass import getpass

def login():
    user1 = "yul"
    password1 = "2521160032"
    
    for i in range(2):
        user = input("Usuario: ")
        if user == user1:
            for i in range(2):
                password = getpass("Acceso")
                if password == password1:
                    print("\033[1;92m"+"Acceso concedido"+"\033[0m")
                    options()
                else:
                    print("\033[1;91m"+"Error \n No coinciden las credenciales"+"\033[0m")
    
        else:
            print("\033[4;91m"+"Error no existe el usuario"+"\033[0m") 
            
def options():
    print("opciones: \n cifrar mensaje \n crear firma \n validar firma \n decifrar mensaje \n")
    opc = input("elije una opción: \n")
    if (opc == 1):
        encrypt = Encrypt_Files()
        encrypt.generate_keys()
        encrypt.enc_files()
    elif (opc == 2):
        sign_message = generate_keys()
        sign_message.Keys_()
        
        with open("files/enc/enc_messages.enc", 'r') as r:
            message = r.read()
    
        message = message.encode()
        sign_message.sign_doc(message)
        
login()     