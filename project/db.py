from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Session=None
session=None
db=None
Base = None

def init_db(secrets):
    """
    Lambda bootstrap init db
    request username/pwd and URI from AWS SecretManager services
    """

    db = create_engine(secrets.getDbURI().format(secrets.getDbUser(), secrets.getDbPwd()))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = declarative_base()

