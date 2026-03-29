from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Geração das chaves públicas e privadas

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
) # Chave privada (decripta)
public_key = private_key.public_key() # Chave pública (encripta)

# Armazenamento das em arquivo .pem chaves usando senhas no caso da chave privada

with open("arquivos/private_key.pem", "wb") as priv_file:
    priv_file.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(b"senha_forte")
        )
    )

with open("arquivos/public_key.pem", "wb") as publi_file:
    publi_file.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

print("Chaves salvas com sucesso em 'private_key.pem' e 'public_key.pem'")

