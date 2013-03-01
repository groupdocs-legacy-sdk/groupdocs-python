####<i>This sample will show how to use <b>MoveFile</b> method from Storage Api to copy/move a file in GroupDocs Storage </i>

#Import of classes from libraries
import base64
import os

from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.MgmtApi import MgmtApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

####Set variables and get POST data
def sample07(request):
    clientId = request.POST.get("client_id")
    privateKey = request.POST.get("private_key")
    #Checking parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample07.pt',
                                  { 'error' : 'You do not enter you User id or Private key' })
    ####Create Signer, ApiClient and Storage Api objects

    #Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    #Create apiClient object
    apiClient = ApiClient(signer)
    #Create Storage Api object
    storageApi = StorageApi(apiClient)
    ####Make a request to Storage API using clientId

    try:
        #Obtaining all Entities from current user
        files = storageApi.ListEntities(clientId, "", extended = True);
    except Exception, e:
        return render_to_response('__main__:templates/sample07.pt',
                                  { 'error' : str(e) })
    #Obtaining all thumbnails
    thumbnail = '';
    name = '';
    currentDir = os.path.dirname(os.path.realpath(__file__))
    for i in range(len(files.result.files)):
        #Check is file have thumbnail
        if files.result.files[i].thumbnail != None:
            #Placing thumbnails to local folder
            fp = open(currentDir + '/../templates/thumbnail' + str(i) + '.jpg', 'wb')
            fp.write(base64.b64decode(files.result.files[i].thumbnail))
            fp.close()
            #Geting file names for thumbnails
            name = files.result.files[i].name
            #Create HTML representation for thumbnails
            thumbnail += '<img src="thumbnail' + str(i) + '.jpg", width="40px", height="40px">' + files.result.files[i].name + '</img> <br />'
    #If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample07.pt',
                              { 'thumbnailList' : thumbnail, 'userId' : clientId, 'privateKey' : privateKey }, 
                              request=request)
