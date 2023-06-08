from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.models import Base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/db_test"

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
