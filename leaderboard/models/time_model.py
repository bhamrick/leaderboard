from leaderboard.tables.times import (
    Times,
    )
from leaderboard.models.game_definitions import (
    games_by_shortname,
    )
#from leaderboard import DBEngine

import simplejson as json

from sqlalchemy.sql import (
    select,
    )

class TimeModel:
    @staticmethod
    def add_time(data):
        if isinstance(data, basestring):
            data = json.loads(data)
        shortname = data['game']
        category = data['category']
        player = data['player']
        comment = data['comment']
        country = data['country']
        del data['game']
        del data['category']
        del data['player']
        del data['comment']
        del data['country']
        game = games_by_shortname[shortname]
        schema = game.category_data[category]
        TimeModel._prepare(schema, data)
        data_string = json.dumps(data)

        ins = Times.insert().values(game=shortname,
                                    category=category,
                                    player=player,
                                    data=data_string,
                                    comment=comment,
                                    country=country)
        conn = DBEngine.connect()
        result = conn.execute(ins)
        return result.inserted_primary_key

    @staticmethod
    def _prepare(schema, data):
        for key, t in schema.iteritems():
            data[key] = t(data[key])

    @staticmethod
    def get_times(game, category):
        """ Gets the times for a category. Will actually pull all times
        """
        query = select([Times]).where(and_(
            Times.c.game == game,
            Times.c.category == category,
            ))
        conn = DBEngine.connect()
        return conn.execute(query).fetchall()
