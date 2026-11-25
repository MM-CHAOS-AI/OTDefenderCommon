# otdefendercommon/database.py
from sqlalchemy.orm import declarative_base

# Standard declarative base shared across all OTDefender services
Base = declarative_base()
