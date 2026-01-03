from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_url ="mysql://mysql:123455@localhost:3306/fastapi"
engine= create_engine(database_url)

session =sessionmaker(autoflush=False, autocommit=False,bind=engine)