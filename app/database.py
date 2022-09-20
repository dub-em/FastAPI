#from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Dumsquared97@localhost/FastAPI'

#engine = create_engine(SQLALCHEMY_DATABASE_URL)

import psycopg2
from psycopg2.extras import RealDictCursor
from .config import settings
import time

while True:
    try:
        conn = psycopg2.connect(host=settings.database_hostname, database=settings.database_name, 
                                user=settings.database_user, password=settings.database_password, cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Database connection was successful!')
        break
    except Exception as error:
        print('Connecting to Database failed!')
        print('Error:', error)
        time.sleep(2)
