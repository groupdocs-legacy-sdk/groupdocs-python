####<i>This sample will show how to use <b>MoveFile</b> method from Storage Api to copy/move a file in GroupDocs Storage </i>

#Import of classes from libraries
import base64

from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.DocApi import DocApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

####Set variables and get POST data
def sample10(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    fileGuId = request.POST.get('fileId')
    email = request.POST.get('email')
    #Checking parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(fileGuId) == False or IsNotNull(email) == False:
        return render_to_response('__main__:templates/sample10.pt', 
                                  { 'error' : 'You do not enter all parameters' })
    ####Create Signer, ApiClient and Storage Api objects

    #Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    #Create apiClient object
    apiClient = ApiClient(signer)
    #Create Storage Api object
    api = StorageApi(apiClient)
    ####Make request to Storage
    try:
        #Geting all Entities from current user
        files = api.ListEntities(userId = clientId, path = '', pageIndex = 0)
        #Selecting file names
        for item in files.result.files:
           if item.guid == fileGuId:
               fileGuId = item.id
        ####Create DocApi object
        docApi = DocApi(apiClient)
        #Make request to user storage for sharing document
        docApi.ShareDocument(clientId, fileGuId, body = [ email, ])
    except Exception, e:
        return render_to_response('__main__:templates/sample10.pt', 
                                  { 'error' : str(e) })
    #If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample10.pt', 
                              { 'userId' : clientId, 
                               'privateKey' : privateKey, 
                               'fileId' : fileGuId, 
                               'email' : email }, 
                              request=request)
