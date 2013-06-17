from sqlalchemy import (
    Column,
    MetaData,
    Table,
    )
from leaderboard import DBEngine

metadata = MetaData()

Times = Table('times', metadata,
    Column('id', Integer, primary_key=True),
    Column('player', String(40)),
    Column('data', Text),
    Column('comment', String(200)),
    Column('country', String(3)),
)

metadata.create_all(DBEngine)
