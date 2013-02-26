# Import of classes from libraries
from pyramid.renderers import render_to_response
import os

def annotation_callback(request):

    file = open(os.getcwd() + '/temp/annotation_add.txt', 'w+')
    for item in request.GET:
        file.write(item + ' => ' + request.GET.get(item) +  ';')
    return render_to_response('__main__:templates/callbacks/annotation_callback.pt', {}, request=request)