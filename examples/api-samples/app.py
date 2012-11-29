from wsgiref.simple_server import make_server

from pyramid.renderers import render_to_response
from pyramid.config import Configurator

import inc_samples.sample1 as sample1
import inc_samples.sample2 as sample2
import inc_samples.sample3 as sample3
import inc_samples.sample4 as sample4
import inc_samples.sample5 as sample5    
import inc_samples.sample6 as sample6
import inc_samples.sample7 as sample7
import inc_samples.sample8 as sample8
import inc_samples.sample9 as sample9
import inc_samples.sample10 as sample10

def index(request):
    return {}

if __name__ == '__main__':
    config = Configurator()

    config.add_route('index', '/')
    config.add_route('sample1', '/sample1')
    config.add_route('sample2', '/sample2')
    config.add_route('sample3', '/sample3')
    config.add_route('sample4', '/sample4')
    config.add_route('sample5', '/sample5') 
    config.add_route('sample6', '/sample6')
    config.add_route('sample7', '/sample7')
    config.add_route('sample8', '/sample8')
    config.add_route('sample9', '/sample9')
    config.add_route('sample10', '/sample10')

    config.add_view(index, route_name='index', renderer='__main__:templates/index.pt')
    config.add_view(sample1.sample1, route_name='sample1')
    config.add_view(sample2.sample2, route_name='sample2')
    config.add_view(sample3.sample3, route_name='sample3')
    config.add_view(sample4.sample4, route_name='sample4')
    config.add_view(sample5.sample5, route_name='sample5')
    config.add_view(sample6.sample6, route_name='sample6')
    config.add_view(sample7.sample7, route_name='sample7')
    config.add_view(sample8.sample8, route_name='sample8')
    config.add_view(sample9.sample9, route_name='sample9')
    config.add_view(sample10.sample10, route_name='sample10')
        
    config.add_static_view(name='/', path='templates/')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
   
