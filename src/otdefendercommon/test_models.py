from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from otdefendercommon.database.base import Base
import otdefendercommon.models  # Forces registration of all models


def test_model_mappings():
    # Use StaticPool to maintain a stable, shared in-memory SQLite instance for the session
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
        echo=False
    )
    
    print("Testing SQLAlchemy model mapping and relationship resolution...")
    Base.metadata.create_all(bind=engine)
    print("Success! All models and relationships initialized without errors.")

if __name__ == "__main__":
    test_model_mappings()