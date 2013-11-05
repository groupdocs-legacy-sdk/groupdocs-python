####<i>This sample will show how to reate folder in GroupDocs account</i>

#Import of classes from libraries
import re
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

####Set variables and get POST data
def sample34(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    folder = request.POST.get('folder')
    basePath = request.POST.get('server_type')
    # Checking clientId, privateKey and folder
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(folder) == False:
        return render_to_response('__main__:templates/sample34.pt',
                                  { 'error' : 'You do not enter all parameters' })
    #Remove tags and spaces from entered data
    clientId = re.sub('<[^>]*>', '', clientId.strip())
    privateKey = re.sub('<[^>]*>', '', privateKey.strip())
    folder = re.sub('<[^>]*>', '', folder.strip())
    if basePath == "":
        basePath = "https://api.groupdocs.com/v2.0"
    basePath = re.sub('<[^>]*>', '', basePath)
    ####Create Signer, ApiClient and Storage Api objects

    #Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    #Create apiClient object
    apiClient = ApiClient(signer)
    #Create Storage Api object
    storageApi = StorageApi(apiClient)
    storageApi.basePath = basePath
    ####Make a request to Storage API using clientId

    try:
        #Check entered path for propper slashes
        if folder.find("\\") != -1:
            folder = folder.replace("\\", "/")
        #Create folder
        createFolder = storageApi.Create(clientId, folder)
        #Check status
        if createFolder.status == "Ok":
            #If status Ok generate message with successful result
            message = '<span style="color:green">Folder was created ' + folder + '</span>';
        else:
			raise Exception(createFolder.error_message)
    except Exception, e:
        return render_to_response('__main__:templates/sample34.pt',
                                  { 'error' : str(e) })
    #If request was successfull - set message variable for template
    return render_to_response('__main__:templates/sample34.pt',
                              { 'userId' : clientId, 
                               'privateKey' : privateKey, 
                               'folder' : folder,
                               'message' : message },
                              request=request)
