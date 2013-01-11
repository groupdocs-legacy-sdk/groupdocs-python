####<i>This sample will show how to use <b>Upload</b> method from Storage Api to upload file to GroupDocs Storage </i>

####Set variables and get POST data

#Import of classes from libraries
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

####Set variables and get POST data
def sample3(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    inputFile = request.POST.get('file')
    # Checking clientId and privateKey
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample3.pt', 
                                  { 'error' : 'You do not enter your User Id or Private Key' })
####Create Signer, ApiClient and Storage Api objects

#Create signer object
    signer = GroupDocsRequestSigner(privateKey)
#Create apiClient object
    apiClient = ApiClient(signer)
#Create Storage Api object
    api = StorageApi(apiClient)

    try:
        #A hack to get uploaded file size
        inputFile.file.seek(0, 2)
        fileSize = inputFile.file.tell()
        inputFile.file.seek(0)
        
        fs = FileStream.fromStream(inputFile.file, fileSize)
        ####Make a request to Storage API using clientId

        #Upload file to current user storage
        response = api.Upload(clientId, inputFile.filename, fs)
        #Generation of Embeded Viewer URL with uploaded file GuId
        iframe = '<iframe src="https://apps.groupdocs.com/document-viewer/embed/' + response.result.guid + '" frameborder="0" width="720" height="600""></iframe>'
        message = '<p>File was uploaded to GroupDocs. Here you can see your <strong>' + inputFile.filename + '</strong> file in the GroupDocs Embedded Viewer.</p>'
    except Exception, e:
        return render_to_response('__main__:templates/sample3.pt', 
                                  { 'error' : str(e) })
    #If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample3.pt', 
                              { 'userId' : clientId, 
                               'privateKey' : privateKey, 
                               'iframe' : iframe,
                               'message' : message},
                              request=request)
