from Crypto import Random
from Crypto.PublicKey import RSA


class generate_keys:
    
    def Keys_(self):
        modules = 256*4

        rsa = RSA.generate(modules, Random.new().read)
        
        private_pem = rsa.exportKey()
        
        with open('files/private_key.pem', 'wb') as f:
          f.write(private_pem)
        
        public_pem = rsa.publickey().exportKey()
        
        with open('files/public_key.pem', 'wb') as f:
          f.write(public_pem)
        
        print('GENERANDO CLAVES___')
        print("KPR:",private_pem)
        print("KPL:",public_pem)
