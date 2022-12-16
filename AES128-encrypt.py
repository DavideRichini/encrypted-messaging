from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = bytes(input("prompt\n"),'UTF-8')
key = get_random_bytes(16)
file_out = open("E:\key.bin", "wb")
[ file_out.write(key) ]
file_out.close()


cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

file_out = open("encrypted.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
file_out.close()
