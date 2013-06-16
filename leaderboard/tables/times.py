from sqlalchemy import (
    Column,
    MetaData,
    Table,
    )

metadata = MetaData()

times = Table('times', metadata,
    Column('id', Integer, primary_key=True),
    Column('player', String(40)),
    Column('data', Text),
    Column('comment', String(200)),
    # Look into doing country
)

metadata.create_all(DBEngine)
