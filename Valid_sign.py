from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA    
import base64
 
 
 class Valid_sign:
    def valid_signs(message, signature):
        with open('files/public_key.pem') as r:
            key = r.read()
            rsakey = RSA.importKey(key)
            verifier_ = Signature_pkcs1_v1_5.new(rsakey)
            digest = SHA256.new()
    
            digest.update(message)
            print("Calculando hash del documento: ", digest.hexdigest())
            print("Descifrando la firma para extraer el hash original")
            is_verify = verifier_.verify(digest, base64.b64decode(signature))
    
            if is_verify:
                print("\033[1;92m"+"Los hashes coinciden"+"\033[0m")
                print("\033[92m"+"el documento no ha sido alterado"+"\033[0m")
            else:
                print("\033[93m"+"Los hashes no coinciden"+"\033[0m")
                print("\033[91m"+"Alerta es probable que el documento haya sido cambiado"+"\033[0m")
    
    