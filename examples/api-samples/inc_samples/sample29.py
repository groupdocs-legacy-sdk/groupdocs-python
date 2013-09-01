#####<i>This sample will show how to use <b>Filepicker.io</b> to upload file to GroupDocs using Python SDK</i>

#Import of classes from libraries
import base64, json
from pyramid.renderers import render_to_response
from pyramid.response import Response

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0


def sample29(request):
####Set variables and get POST data
    clientId = request.POST.get('clientId')
    url = request.POST.get('url')
    basePath = request.POST.get('basePath')
    if IsNotNull(clientId) == False or IsNotNull(url) == False:
        return render_to_response('__main__:templates/sample29.pt',
                                  { 'error' : 'You do not enter you User id or Private key' })
####Check base path
    if basePath == '':
        basePath = 'https://api.groupdocs.com/v2.0';
    ###Generate iframe url for chosen server

    if basePath == "https://api.groupdocs.com/v2.0":
        iframe = 'https://apps.groupdocs.com/document-viewer/embed?url=' + url + '&user_id=' + clientId
    ###iframe to dev server
    elif basePath == "https://dev-api.groupdocs.com/v2.0":
        iframe = 'https://dev-apps.groupdocs.com/document-viewer/embed?url=' + url + '&user_id=' + clientId

    ###iframe to test server
    elif basePath == "https://stage-api.groupdocs.com/v2.0":
        iframe = 'https://stage-apps.groupdocs.com/document-viewer/embed?url=' + url + '&user_id=' + clientId

    elif basePath == "http://realtime-api.groupdocs.com":
        iframe = 'http://realtime-apps.groupdocs.com/document-viewer/embed?url=' + url + '&user_id=' + clientId

    ###Create json string with result data
    result = json.dumps({ 'iframe' : iframe })
    return Response(body = result, content_type = 'application/json')
