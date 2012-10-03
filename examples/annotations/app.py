from wsgiref.simple_server import make_server
from pyramid.config import Configurator

from pyramid.renderers import render_to_response
from pyramid.view import view_config

from groupdocs.api.APIClient import APIClient
from groupdocs.api.StorageAPI import StorageAPI
from groupdocs.api.AntAPI import AntAPI
import groupdocs.model
	

def index(request):
    return {}

def upload(request):
	session = request.session
	session['client_id'] = request.POST['client_id']
	session['private_key'] = request.POST['private_key']
	
	input_file = request.POST['file']

	import os
	current_dir = os.path.dirname(os.path.realpath(__file__))

	# Using the filename like this without cleaning it is very
	# insecure so please keep that in mind when writing your own
	# file handling.
	file_path = os.path.join(current_dir, input_file.filename)
	output_file = open(file_path, 'wb')

	input_file.file.seek(0)
	while 1:
		data = input_file.file.read(2<<16)
		if not data:
			break
		output_file.write(data)
	output_file.close()	

	apiClient = APIClient(session['private_key'], "https://api.groupdocs.com/v2.0")
	response = StorageAPI(apiClient).Upload(session['client_id'], input_file.filename, "uploaded from python client library", 'file://' + str(file_path))
	session['guid'] = response.result.guid

	os.remove(file_path)
	return render_to_response('__main__:annotation.pt',
                              {'guid':session['guid']},
                              request=request)

def annotation(request):
	session = request.session
	apiClient = APIClient(session['private_key'], "https://api.groupdocs.com/v2.0")
	try:
		response = AntAPI(apiClient).ListAnnotations(session['client_id'], session['guid'])
	except Exception: 
		return "Server error or no annotations"
		
	output = ''
	for annotation in response.result.annotations:
		replies = []
		for reply in annotation.replies:
			replies.append(reply.userName + ": " + reply.text)
		output += "Annotation Type: " +  str(annotation.type) + " -- Replies: " + str(replies) + "<br/>"
	
	return output

if __name__ == '__main__':
    config = Configurator()

    config.include("pyramid_beaker")
    config.add_route('index', '/')
    config.add_route('upload', '/upload')
    config.add_route('annotation', '/annotation')
    
    config.add_view(index, route_name='index', renderer='__main__:upload_form.pt')
    config.add_view(upload, route_name='upload')
    config.add_view(annotation, route_name='annotation', renderer='string')
    
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
   
