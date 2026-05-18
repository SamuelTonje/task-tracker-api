from sqlalchemy import text

from app.shared.infrastructure.databases.session import SessionLocal

def test_database_connection():
    session = SessionLocal()

    try:
        result = session.execute(text("SELECT 1"))
        assert result.scalar() == 1
    finally:
        session.close()