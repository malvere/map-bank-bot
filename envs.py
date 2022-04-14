import os

""" !Add PROJECT_NAME in heroku Vars! """
API_TOKEN = os.getenv('API_TOKEN')
PROJECT_NAME = os.getenv('PROJECT_NAME')
WEBHOOK_HOST = f'https://{PROJECT_NAME}.herokuapp.com'  # Enter here your link from Heroku project settings
WEBHOOK_URL_PATH = '/' + API_TOKEN
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_URL_PATH}'
WEBAPP_HOST = os.getenv('localhost')
WEBAPP_PORT = os.getenv('PORT')

