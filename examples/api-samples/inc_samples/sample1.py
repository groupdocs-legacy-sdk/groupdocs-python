#<i>This sample will show how to use <b>Signer object</b> to be authorized at GroupDocs and how to get GroupDocs user infromation using PHP SDK</i>

#Import of classes from libraries
import base64
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.MgmtApi import MgmtApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

####Set variables and get POST data
def sample1(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')

    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample1.pt', 
                                  { 'error' : 'You do not enter you User id or Private key' })
####Create Signer, ApiClient and Management Api objects

#Create signer object
    signer = GroupDocsRequestSigner(privateKey)
#Create apiClient object
    apiClient = ApiClient(signer)
#Create Management Api object
    api = MgmtApi(apiClient)

    try:
        ####Make a request to Management API using clientId
		userInfo = api.GetUserProfile(clientId)
        
    except Exception, e:
        return render_to_response('__main__:templates/sample1.pt', 
                                  { 'error' : str(e) })
#If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample1.pt', 
                              { 'userId' : clientId, 
                               'privateKey' : privateKey, 
                               'userInfo' : userInfo.result.user
                              }, 
                              request=request)
