#%%
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class Cipher():
    def __init__(self, key) -> None:
        self.key = key

    def encrypt(self, toEncode: str):
        cipher = AES.new(bytes.fromhex(self.key), AES.MODE_CBC)
        cdata = cipher.encrypt(pad(toEncode.encode('utf-8'), AES.block_size))
        self.iv = cipher.iv
        cdata = cipher.iv + cdata
        return cdata

    def decrypt(self, eninput: bytes):
        cipher = AES.new(bytes.fromhex(self.key), AES.MODE_CBC, iv=eninput[:16])
        ddata = unpad((cipher.decrypt(eninput[16:])), AES.block_size).decode('utf-8')
        return ddata