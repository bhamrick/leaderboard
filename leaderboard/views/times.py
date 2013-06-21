from leaderboard.lib.session import ajax
from leaderboard.models.time_model import TimeModel

import simplejson as json

class TimesView:
    @ajax()
    def times(request):
        game = request.matchdict['game']
        category = request.matchdict['category']
        times = TimeModel.get_times(game, category)
        retval = []
        for row in times:
            time = dict(row)
            time['data'] = json.loads(time['data'])
            retval.append(time)
        return retval
