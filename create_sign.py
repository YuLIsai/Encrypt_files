from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5 as Signature_PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64

class create_sign:
    def sign_doc(message):
        with open('files/private_key.pem') as f:
            key = f.read()
            RSAKey = RSA.import_key(key)
            signer = Signature_PKCS1_v1_5.new(RSAKey)
    
            digest = SHA256.new()
            
            digest.update(message)
            print("Mensaje original:", message)
            print("Hash calculado:", digest)
    
            sign = signer.sign(digest)
            signature = base64.b64encode(sign)
    
            with open('files/sign_gen.pem','wb') as fp:
                fp.write(signature)
                fp.close()
            print("La firma ha sido creada: ", signature)
            print(" la firma se guardo en : sign_gen.pem")
    
            return signature
    
    