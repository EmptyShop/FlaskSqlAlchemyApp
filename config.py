from dotenv import load_dotenv
import os

# carga el archivo .env y usa su contenido como variables de ambiente
load_dotenv()

user = os.environ["MARIADB_USER"]
password = os.environ["MARIADB_PWD"]
host = os.environ["MARIADB_HOST"]
database = os.environ["MARIADB_DATABASE"]

DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}/{database}'
SECRET_KEY = os.environ["SECRET_KEY"]