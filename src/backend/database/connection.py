from backend.config.settings import db_url
from sqlalchemy import create_engine

engine = create_engine(db_url)