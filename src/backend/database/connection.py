from src.backend.config.settings import db_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

