from sqlalchemy import Table, Column, Integer, String, Boolean, TIMESTAMP, MetaData


referral_metadata = MetaData()

# referral = Table(
#     "referral",
#     referral_metadata,
#     Column("id", Integer, primary_key=True),
#     Column("referral_code", String, unique=True),
#     Column("is_active", Boolean, default=False),
#     Column("times_used", Integer, default=0),
# )