from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

#Encriptando uma mensagem usando a chave pública

with open("arquivos/public_key.pem", "rb") as publi_file:
    public_key = serialization.load_pem_public_key(
        publi_file.read(),
        backend=default_backend()
    )

message = "Oiee, essa aqui é a minha mensagem original.".encode('utf-8')

# public_key.encrypt() usa a chave pública para cifrar a mensagem
encrypted_message = public_key.encrypt( 
    # OAEP é um esquema de preenchimento seguro que torna o RSA resistente a ataques
    # MGF1 é uma função geradora de máscara baseada em SHA-256
    # O hash SHA-256 é usando tanto no MGF1 quanto no próprio algoritmo de preenchimento
    message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                          algorithm=hashes.SHA256(), label=None)
)

with open("arquivos/mensagem_encriptada.bin", "wb") as encry_file:
    encry_file.write(encrypted_message)

