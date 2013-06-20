from leaderboard.lib.session import ajax
from leaderboard.models.game_definitions import games_by_shortname

class GamesView:
    @ajax()
    def list_games(request):
        return games_by_shortname.keys()

    @ajax()
    def categories(request):
        game = request.matchdict['game']
        return games_by_shortname[game].category_data.keys()

    @ajax()
    def category_data(request):
        game = request.matchdict['game']
        category = request.matchdict['category']
        category_data = games_by_shortname[game].category_data[category]
        retval = {}
        for field, t in category_data.iteritems():
            retval[field] = t.description()
        return retval

    @ajax()
    def category_sort(request):
        game = request.matchdict['game']
        category = request.matchdict['category']
        game_data = games_by_shortname[game]
        return game_data.default_sort[category]
