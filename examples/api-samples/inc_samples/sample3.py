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

    try:
        currentDir = os.path.dirname(os.path.realpath(__file__))
        # Using the filename like this without cleaning it is very
        # insecure so please keep that in mind when writing your own
        # file handling.
        filePath = os.path.join(currentDir, inputFile.filename)
        outputFile = open(filePath, 'wb')

        inputFile.file.seek(0)
        while 1:
            data = inputFile.file.read(2<<16)
            if not data:
                break
            outputFile.write(data)
        outputFile.close()    

        fs = FileStream.fromFile(filePath);
        #~ import pdb;  pdb.set_trace()

        response = api.Upload(clientId, inputFile.filename, fs)

        os.remove(filePath)
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
