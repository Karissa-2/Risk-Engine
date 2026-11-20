import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

load_dotenv()

# Load Database URL
DATABASE_URL = os.environ["DATABASE_URL"]

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, 
                       connect_args={"sslmode": "require"},
                       pool_pre_ping=True)

# Create a session factory
Session = sessionmaker( bind=engine, autoflush=False)

# Test the database connection
try:
    with engine.connect() as connection:
        print("Database connection successful!")
except Exception as e:
    print(f"Database connection failed: {e}")

# Base class for declarative models
class Base(DeclarativeBase):
    pass
