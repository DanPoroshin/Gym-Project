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
    Column('referring_user_id', Integer, ForeignKey(user.c.id)),
    Column('referred_user_id', Integer, ForeignKey(user.c.id)),
    Column('referral_code', String, unique=True),
    Column('used', Boolean, default=False),
    Column('created_at', TIMESTAMP, default=datetime.utcnow)
)

class Referral(Base):
    __tablename__ = 'referral'
    
    id = Column(Integer, primary_key=True)
    referring_user_id = Column(Integer, ForeignKey(user.c.id))
    referred_user_id = Column(Integer, ForeignKey(user.c.id))
    referral_code = Column(String, unique=True)
    used = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    
    referring_user = relationship("user", foreign_keys=[referring_user_id], backref="referrals_made")
    referred_user = relationship("user", foreign_keys=[referred_user_id], backref="referrals_received")