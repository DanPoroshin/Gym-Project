from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, Boolean, MetaData, ForeignKey

from app.database import Base

auth_metadata = MetaData()


user = Table(
    "user",
    auth_metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("full_name", String, nullable=False),
    Column("is_subscribed", Boolean, default=False, nullable=False),
    # Column('referral_id', Integer, ForeignKey(referral.c.id), nullable=True),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    is_subscribed = Column(Boolean, default=False, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)