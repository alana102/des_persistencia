import zlib
import hashlib

string = "oiee, eu queria não ter prova de persistência na terça"

byte = string.encode("utf-8")

checksum = sum(byte)
crc32 = zlib.crc32(byte)
md5 = hashlib.md5(byte).hexdigest()
sha1 = hashlib.sha1(byte).hexdigest()
sha256 = hashlib.sha256(byte).hexdigest()

print ("String de entrada:", string)
print("Checksum:", checksum)
print("CRC32:", format(crc32, '08x'))
print("MD5:", md5)
print("SHA1:", sha1)
print("SHA256:", sha256)
