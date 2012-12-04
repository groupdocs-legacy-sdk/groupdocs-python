from wsgiref.simple_server import make_server
from pyramid.config import Configurator
import os
from pyramid.renderers import render_to_response
from pyramid.view import view_config

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.FileStream import FileStream
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

def index(request):
    return {}

def upload(request):
	client_id = request.POST['client_id']
	private_key = request.POST['private_key']
	
	input_file = request.POST['file']

	
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
	
	signer = GroupDocsRequestSigner(private_key)
	apiClient = ApiClient(signer)
	api = StorageApi(apiClient)

	fs = FileStream.fromFile(file_path);
	response = api.Upload(client_id, input_file.filename, fs)
	fs.inputStream.close()
	os.remove(file_path)
	return render_to_response('__main__:viewer.pt',
                              {'guid':response.result.guid},
                              request=request)


if __name__ == '__main__':
    config = Configurator()

    config.add_route('index', '/')
    config.add_route('upload', '/upload')
    
    config.add_view(index, route_name='index', renderer='__main__:upload_form.pt')
    config.add_view(upload, route_name='upload')
        
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
   
