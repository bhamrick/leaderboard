from sqlalchemy import (
    Column,
    MetaData,
    Table,
    )
from sqlalchemy.types import (
    Integer,
    String,
    Text,
    )
#from leaderboard import DBEngine

metadata = MetaData()

Times = Table('times', metadata,
    Column('id', Integer, primary_key=True),
    Column('game', String(8)),
    Column('category', String(40)),
    Column('player', String(40)),
    Column('data', Text),
    Column('comment', String(200)),
    Column('country', String(3)),
)

metadata.create_all(DBEngine)
