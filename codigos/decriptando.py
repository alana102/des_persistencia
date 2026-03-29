from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

# Decriptando com chave privada

with open("arquivos/private_key.pem", "rb") as priv_file:
    private_key = serialization.load_pem_private_key(
        priv_file.read(),
        password=b"senha_forte",
        backend=default_backend()
    )

encrypted_message = open("arquivos/mensagem_encriptada.bin", "rb").read()

decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf = padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(f"Mensagem decriptada: {decrypted_message.decode()}")