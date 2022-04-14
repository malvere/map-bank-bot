import os

username = os.getenv('IMAP_USER')
passwd = os.getenv('IMAP_PWD')
key = os.getenv('ENC_KEY')

ALL = '(OR FROM "support@stripe.com" FROM "notifications@stripe.com")'
UNSEEN = '(OR FROM "support@stripe.com" FROM "notifications@stripe.com" UNSEEN)'