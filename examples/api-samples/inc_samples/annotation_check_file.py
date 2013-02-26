# Import of classes from libraries
from pyramid.renderers import render_to_response
import os

def annotation_check_file(request):

    file = open(os.getcwd() + '/temp/annotation_add.txt', 'r')
    lines = file.readlines()

    return render_to_response('__main__:templates/callbacks/annotation_check_file.pt', {'lines' : lines}, request=request)