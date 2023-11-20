from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, TIMESTAMP, Table, MetaData
from app.database import Base


metadata = MetaData()

referral = Table(
    'referral',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('referral_claimer_id', Integer),
    Column('referral_owner_id', Integer),
    Column('referral_code', String, unique=False),
    Column('used', Boolean, default=False),
    Column('created_at', TIMESTAMP, default=datetime.utcnow)
)


class Referral(Base):
    __tablename__ = 'referral'

    id = Column(Integer, primary_key=True, autoincrement=True)
    referral_claimer_id = Column(Integer, ForeignKey('user.id'))
    referral_owner_id = Column(Integer, ForeignKey('user.id'))
    referral_code = Column(String, unique=False)
    used = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
