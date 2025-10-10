import os
from dotenv import load_dotenv

load_dotenv()


#---------------------- Banco de Dados ----------------------#
db_url = os.getenv('DATABASE_URL')