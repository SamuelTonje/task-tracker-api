from alembic import context

from app.shared.infrastructure.databases.base import Base
from app.shared.infrastructure.config.settings import settings

target_metadata = Base.metadata
config = context.config

config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)