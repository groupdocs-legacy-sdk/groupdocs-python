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
def sample05(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    srcPath = request.POST.get('srcPath')
    destPath = request.POST.get('destPath')
    copy = request.POST.get('copy')
    move = request.POST.get('move')

    ####Check clientId, privateKey and file Id
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(srcPath) == False or IsNotNull(destPath) == False:
        return render_to_response('__main__:templates/sample05.pt',
                                  { 'error' : 'You do not enter all parameters' })

    ####Create Signer, ApiClient and Storage Api objects

    #Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    #Create apiClient object
    apiClient = ApiClient(signer)
    #Create Storage Api object
    api = StorageApi(apiClient)
    # import pdb;pdb.set_trace() # debug
####Make a request to Storage API using clientId
    try:
        #Create DocApi object
        docApi = DocApi(apiClient)
        #Make a request to Doc API using clientId
        srcFile = docApi.GetDocumentMetadataByPath(clientId, srcPath)
        #Obtaining file name
        fileID = int(srcFile.result.id)
        ####Make request for file copying/movement

        #If user choose copy
        if copy:
           file = api.MoveFile(clientId, destPath, Groupdocs_Copy = fileID)
        #If user choose move
        if move:
           file = api.MoveFile(clientId, destPath, Groupdocs_Move = fileID)

    except Exception, e:
        return render_to_response('__main__:templates/sample05.pt',
                                  { 'error' : str(e) })
    #If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample05.pt',
                              { 'userId' : clientId, 
                               'privateKey' : privateKey, 
                               'destPath' : destPath, 
                               'srcPath' : srcPath }, 
                              request=request)
