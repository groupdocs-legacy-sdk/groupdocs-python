import base64
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.MgmtApi import MgmtApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 1
def sample1(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')

    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample1.pt', 
                                  { 'error' : 'You do not enter you User id or Private key' })

    signer = GroupDocsRequestSigner(privateKey)
    apiClient = ApiClient(signer)
    api = MgmtApi(apiClient)

    try:
		userInfo = api.GetUserProfile(clientId)
        
    except Exception, e:
        return render_to_response('__main__:templates/sample1.pt', 
                                  { 'error' : str(e) })

    return render_to_response('__main__:templates/sample1.pt', 
                              { 'userId' : clientId, 
                               'privateKey' : privateKey, 
                               'userInfo' : userInfo.result.user
                              }, 
                              request=request)
