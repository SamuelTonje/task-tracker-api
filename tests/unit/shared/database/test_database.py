from app.shared.infrastructure.databases.session import engine
from app.shared.infrastructure.databases.session import SessionLocal

def test_database_engine_exists():
    assert engine is not None

def test_session_local_exists():
    session = SessionLocal()

    assert session is not None

    session.close()