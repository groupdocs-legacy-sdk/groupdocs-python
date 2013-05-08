import os
import re
import urllib2
from pyramid.response import Response

def download_file(request):
	url = request.application_url
	currentDir = os.path.dirname(os.path.realpath(__file__))
	downloadFolder = currentDir + '/../downloads/'
	file = downloadFolder + request.GET.get('FileName')
	size = os.path.getsize(file)
	response = Response(content_type='application/force-download', content_disposition='attachment; filename=' + request.GET.get('FileName'))
	response.app_iter = open(file, 'rb')
	response.content_length = size
	return response