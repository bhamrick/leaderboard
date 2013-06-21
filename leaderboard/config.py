from leaderboard.views.games import GamesView
from leaderboard.views.times import TimesView
from leaderboard.views.web import WebView

def routes(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('root', '')
    config.add_view(WebView.home, route_name='root')

    config.add_route('home', '/home')
    config.add_view(WebView.home, route_name='home')

    config.add_route('ajax_test', '/ajax_test')
    config.add_view(WebView.ajax_test, route_name='ajax_test')

    config.add_route('list_games', '/games')
    config.add_view(GamesView.list_games, route_name='list_games')

    config.add_route('list_categories', '/categories/{game}')
    config.add_view(GamesView.categories, route_name='list_categories')

    config.add_route('category_data', '/category_data/{game}/{category}')
    config.add_view(GamesView.category_data, route_name='category_data')

    config.add_route('category_sort', '/category_sort/{game}/{category}')
    config.add_view(GamesView.category_sort, route_name='category_sort')

    config.add_route('get_times', '/times/{game}/{category}')
    config.add_view(TimesView.times, route_name='get_times')
