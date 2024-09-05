from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv


load_dotenv()


# SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_PRIVATE_URL")
SQLALCHEMY_DATABASE_URL = "sqlite:///local_database.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# import os
# from dotenv import load_dotenv


# load_dotenv()


# SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_PRIVATE_URL")

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()
