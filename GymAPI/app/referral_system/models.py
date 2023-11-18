from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, TIMESTAMP, Table, MetaData
from sqlalchemy.orm import relationship
from datetime import datetime
from app.auth.models import user
metadata = MetaData()

referral = Table(
    'referral',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('referring_user_id', Integer),
    Column('referred_user_id', Integer),
    Column('referral_code', String, unique=True),
    Column('used', Boolean, default=False),
    Column('created_at', TIMESTAMP, default=datetime.utcnow)
)


class Referral(Base):
    __tablename__ = 'referral'

    id = Column(Integer, primary_key=True, autoincrement=True)
    referring_user_id = Column(Integer)
    referred_user_id = Column(Integer)
    referral_code = Column(String, unique=True)
    used = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
