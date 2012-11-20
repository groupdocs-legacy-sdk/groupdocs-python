from wsgiref.simple_server import make_server
from pyramid.config import Configurator

from pyramid.renderers import render_to_response
    
import inc_samples.sample7 as sample7

def index(request):
    return {}

if __name__ == '__main__':
    config = Configurator()

    config.add_route('index', '/')
    config.add_route('sample7', '/sample7')

    config.add_view(index, route_name='index', renderer='__main__:templates/index.pt')
    config.add_view(sample7.sample7, route_name='sample7')
        
    config.add_static_view(name='/', path='templates/')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
   
