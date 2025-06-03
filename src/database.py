from sqlalchemy import Float, create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session, declarative_base

Base = declarative_base()

# Database setup
DATABASE_URL = "sqlite:///./csn.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy Model
class GeoAddress(Base):
    __tablename__ = "GeoAddress"
    
    id: int = Column(Integer, primary_key=True, index=True)
    lat: float = Column(Float)
    lon: float = Column(Float)
    city: str = Column(String)
    district: str = Column(String)
    number: str = Column(String)
    zip_code: str = Column(String)
    streetname: str = Column(String)
    state: str = Column(String)

# Database helper
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


