from pyramid.config import Configurator
from sqlalchemy import engine_from_config
import os

from .config import routes

if settings['sqlalchemy.url'][0] == '%':
    settings['sqlalchemy.url'] = os.environ[settings['sqlalchemy.url'][1:]]
DBEngine = engine_from_config(settings, 'sqlalchemy.')

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include(routes)
    return config.make_wsgi_app()

