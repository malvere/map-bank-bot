#%%
import email
import imaplib
import creds

class Mail():
    def __init__(self) -> None:
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
        self.mail.login(creds.username, creds.passwd)
        self.mail.select('INBOX')

    def listMailBox(self):
        print(self.mail.list())

    def searchAll(self):
        self.result, self.data = self.mail.search(None, creds.ALL)
        return self.data

    def searchUnseen(self):
        self.result, self.data = self.mail.search(None, creds.UNSEEN)
        return self.data

    def getCode(self):
        ids = self.data[0].split()
        result, data = self.mail.fetch(ids[-1], '(RFC822)')
        raw = data[0][1]
        emsg = email.message_from_bytes(raw)
        for part in emsg.walk():
            if (part.get_content_type() == "text/plain"):
                msg = part.get_payload(decode=True)
                msg = msg.decode().split(' ').pop(0)
                print(msg)
                return msg

    def close(self):
        self.mail.close()

    def logout(self):
        self.mail.logout()

