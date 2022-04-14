#%%
from crypto import Cipher
from creds import key

class Card():
    def __init__(self, lastDigits: str) -> None:
        self.lastDigits = lastDigits
    
    def decrypt(self):
        c = Cipher(key)
        with open(f'./cards/{self.lastDigits}.encrypted', 'rb') as f:
            card = c.decrypt(f.read()).split('//')
            self.number = card[0]
            self.cvv = card[1]
            self.date = card[2]



    