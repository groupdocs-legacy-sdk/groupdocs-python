import os
from wsgiref.simple_server import make_server

from pyramid.renderers import render_to_response
from pyramid.config import Configurator

import inc_samples.sample01 as sample01
import inc_samples.sample02 as sample02
import inc_samples.sample03 as sample03
import inc_samples.sample04 as sample04
import inc_samples.sample05 as sample05
import inc_samples.sample06 as sample06
import inc_samples.sample07 as sample07
import inc_samples.sample08 as sample08
import inc_samples.sample09 as sample09
import inc_samples.sample10 as sample10
import inc_samples.sample11 as sample11
import inc_samples.sample12 as sample12
import inc_samples.sample13 as sample13
import inc_samples.sample14 as sample14
import inc_samples.sample15 as sample15
import inc_samples.sample16 as sample16
import inc_samples.sample17 as sample17
import inc_samples.sample18 as sample18
import inc_samples.sample19 as sample19
import inc_samples.sample20 as sample20
import inc_samples.sample21 as sample21
import inc_samples.sample22 as sample22
import inc_samples.sample23 as sample23
import inc_samples.sample24 as sample24
import inc_samples.sample25 as sample25
import inc_samples.annotation_callback as annotation_callback
import inc_samples.annotation_check_file as annotation_check_file
import inc_samples.convert_callback as convert_callback
import inc_samples.compare_callback as compare_callback
import inc_samples.signature_callback as signature_callback
import inc_samples.check_file as check_file
import inc_samples.download_file as download_file

def index(request):
    return {}

if __name__ == '__main__':
    config = Configurator()

    config.add_route('index', '/')
    config.add_route('sample01', '/sample01')
    config.add_route('sample02', '/sample02')
    config.add_route('sample03', '/sample03')
    config.add_route('sample04', '/sample04')
    config.add_route('sample05', '/sample05')
    config.add_route('sample06', '/sample06')
    config.add_route('sample07', '/sample07')
    config.add_route('sample08', '/sample08')
    config.add_route('sample09', '/sample09')
    config.add_route('sample10', '/sample10')
    config.add_route('sample11', '/sample11')
    config.add_route('sample12', '/sample12')
    config.add_route('sample13', '/sample13')
    config.add_route('sample14', '/sample14')
    config.add_route('sample15', '/sample15')
    config.add_route('sample16', '/sample16')
    config.add_route('sample17', '/sample17')
    config.add_route('sample18', '/sample18')
    config.add_route('sample19', '/sample19')
    config.add_route('sample20', '/sample20')
    config.add_route('sample21', '/sample21')
    config.add_route('sample22', '/sample22')
    config.add_route('sample23', '/sample23')
    config.add_route('sample24', '/sample24')
    config.add_route('sample25', '/sample25')
    config.add_route('annotation_callback', 'annotation_callback')
    config.add_route('annotation_check_file', 'annotation_check_file')
    config.add_route('convert_callback', 'convert_callback')
    config.add_route('compare_callback', 'compare_callback')
    config.add_route('signature_callback', 'signature_callback')
    config.add_route('check_file', 'check_file')
    config.add_route('download_file', 'download_file')

    config.add_view(index, route_name='index', renderer='__main__:templates/index.pt')
    config.add_view(sample01.sample01, route_name='sample01')
    config.add_view(sample02.sample02, route_name='sample02')
    config.add_view(sample03.sample03, route_name='sample03')
    config.add_view(sample04.sample04, route_name='sample04')
    config.add_view(sample05.sample05, route_name='sample05')
    config.add_view(sample06.sample06, route_name='sample06')
    config.add_view(sample07.sample07, route_name='sample07')
    config.add_view(sample08.sample08, route_name='sample08')
    config.add_view(sample09.sample09, route_name='sample09')
    config.add_view(sample10.sample10, route_name='sample10')
    config.add_view(sample11.sample11, route_name='sample11')
    config.add_view(sample12.sample12, route_name='sample12')
    config.add_view(sample13.sample13, route_name='sample13')
    config.add_view(sample14.sample14, route_name='sample14')
    config.add_view(sample15.sample15, route_name='sample15')
    config.add_view(sample16.sample16, route_name='sample16')
    config.add_view(sample17.sample17, route_name='sample17')
    config.add_view(sample18.sample18, route_name='sample18')
    config.add_view(sample19.sample19, route_name='sample19')
    config.add_view(sample20.sample20, route_name='sample20')
    config.add_view(sample21.sample21, route_name='sample21')
    config.add_view(sample22.sample22, route_name='sample22')
    config.add_view(sample23.sample23, route_name='sample23')
    config.add_view(sample24.sample24, route_name='sample24')
    config.add_view(sample25.sample25, route_name='sample25')
    config.add_view(annotation_callback.annotation_callback, route_name='annotation_callback')
    config.add_view(annotation_check_file.annotation_check_file, route_name='annotation_check_file')
    config.add_view(convert_callback.convert_callback, route_name='convert_callback')
    config.add_view(compare_callback.compare_callback, route_name='compare_callback')
    config.add_view(signature_callback.signature_callback, route_name='signature_callback')
    config.add_view(check_file.check_file, route_name='check_file', renderer = 'string')
    config.add_view(download_file.download_file, route_name = 'download_file')

    config.add_static_view(name='/', path='templates/')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', int(os.environ.get('PORT', '8080')), app)
    server.serve_forever()
   
