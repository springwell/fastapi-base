import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://%(db_user)s:%(db_password)s@" \
                          "%(db_host)s/%(db_name)s?charset=utf8" % {
                               "db_user": os.getenv("MYSQL_USER"),
                               "db_password": os.getenv("MYSQL_PASSWORD"),
                               "db_host": os.getenv("MYSQL_HOSTNAME"),
                               "db_name": os.getenv("MYSQL_DATABASE")
                          }

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

Base = declarative_base()
