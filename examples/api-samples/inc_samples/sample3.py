import base64
import os
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.FileStream import FileStream
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 3
def sample3(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    inputFile = request.POST.get('file')

    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample3.pt', 
                                  { 'error' : 'You do not enter your User Id or Private Key' })

    signer = GroupDocsRequestSigner(privateKey)
    apiClient = ApiClient(signer)
    api = StorageApi(apiClient)
#    apiClient.setDebug(True)

    try:
        # a hack to get uploaded file size
        inputFile.file.seek(0, 2)
        fileSize = inputFile.file.tell()
        inputFile.file.seek(0)
        
        fs = FileStream.fromStream(inputFile.file, fileSize)
        #~ import pdb;  pdb.set_trace()

        response = api.Upload(clientId, inputFile.filename, fs)

        iframe = '<iframe src="https://apps.groupdocs.com/document-viewer/embed/' + response.result.guid + '" frameborder="0" width="720" height="600""></iframe>'
        massage = '<p>File was uploaded to GroupDocs. Here you can see your <strong>' + inputFile.filename + '</strong> file in the GroupDocs Embedded Viewer.</p>'
    except Exception, e:
        return render_to_response('__main__:templates/sample3.pt', 
                                  { 'error' : str(e) })

    return render_to_response('__main__:templates/sample3.pt', 
                              { 'userId' : clientId, 
                               'privateKey' : privateKey, 
                               'iframe' : iframe,
                               'massage' : massage}, 
                              request=request)
