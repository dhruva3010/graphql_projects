from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic.config import Config
from alembic import command
from models.models import Base

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:Myaccount321$@localhost/db_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables() -> None:
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    try:
        session.commit()  # Commit the changes
        print('Creating Table(s)')
    except Exception as e:
        session.rollback()  # Rollback the changes in case of an error
        raise e
    finally:
        session.close()

def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
