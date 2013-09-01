####<i>This sample will show how to use <b>Delete</b> method from Storage Api to download a file from GroupDocs Storage</i>

#Import of classes from libraries
import base64
import os
import shutil
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.FileStream import FileStream
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

####Set variables and get POST data
def sample30(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    
    file_id = request.POST.get('fileId')
    # Checking clientId, privateKey and file_Id
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(file_id) == False:
        return render_to_response('__main__:templates/sample30.pt',
                                  { 'error' : 'You do not enter all parameters' })

    ####Create Signer, ApiClient and Storage Api objects

    #Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    #Create apiClient object
    apiClient = ApiClient(signer)
    #Create Storage Api object
    api = StorageApi(apiClient)

    ####Make a request to Storage API using clientId

    try:
#        Delete file from GroupDocs account
        delete = api.Delete(clientId, file_id);
# Check delete dtatus.
        if delete.status == "Ok":
#            If status Ok return successful message
            message = '<font color="green">File was deleted</font> <br />';
        else:
			raise Exception(delete.error_message)
    except Exception, e:
        return render_to_response('__main__:templates/sample30.pt',
                                  { 'error' : str(e) })
    #If request was successfull - set message variable for template
    return render_to_response('__main__:templates/sample30.pt',
                              { 'userId' : clientId, 
                               'privateKey' : privateKey, 
                               'file_Id' : file_id, 
                               'message' : message },
                              request=request)
