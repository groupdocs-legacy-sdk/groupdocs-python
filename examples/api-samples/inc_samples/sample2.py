####<i>This sample will show how to use <b>ListEntities</b> method from Storage  API  to list files within GroupDocs Storage</i>

#Import of classes from libraries
import base64
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

####Set variables and get POST data
def sample2(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample2.pt', 
                                  { 'error' : 'You do not enter you User id or Private key' })
####Create Signer, ApiClient and Storage Api objects

#Create signer object
    signer = GroupDocsRequestSigner(privateKey)
#Create apiClient object
    apiClient = ApiClient(signer)
#Create Storage Api object
    api = StorageApi(apiClient)

    try:
        ####Make a request to Storage API using clientId

        #Obtaining all Entities from current user
        files = api.ListEntities(userId = clientId, path = '', pageIndex = 0)
        #Obtaining file names
        names = ''
        for item in files.result.files:
        #selecting file names
           names += item.name + '<br>'

    except Exception, e:
        return render_to_response('__main__:templates/sample2.pt', 
                                  { 'error' : str(e) })
    #If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample2.pt', 
                              { 'userId' : clientId, 
                               'privateKey' : privateKey, 
                               'names' : names
                              }, 
                              request=request)
