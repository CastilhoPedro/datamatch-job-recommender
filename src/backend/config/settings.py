import os
from dotenv import load_dotenv

load_dotenv()


#---------------------- Banco de Dados ----------------------#
db_url = os.getenv('DATABASE_URL')


#---------------------- Acessos aos Portais -----------------#

linkedin_email = os.getenv('linkedin_email')
linkedin_pwd = os.getenv('linkedin_pwd')