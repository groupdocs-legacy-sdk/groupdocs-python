import base64

from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 2
def sample2(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample2.pt', 
                                  { 'error' : 'You do not enter you User id or Private key' })

    signer = GroupDocsRequestSigner(privateKey)
    apiClient = ApiClient(signer)
    api = StorageApi(apiClient)

    try:
        files = api.ListEntities(userId = clientId, path = '', pageIndex = 0)
        names = ''
        for item in files.result.files: #selecting file names
           names += item.name + '<br>'
        #~ import pdb; pdb.set_trace()
    except Exception, e:
        return render_to_response('__main__:templates/sample2.pt', 
                                  { 'error' : str(e) })

    return render_to_response('__main__:templates/sample2.pt', 
                              { 'userId' : clientId, 
                               'privateKey' : privateKey, 
                               'names' : names
                              }, 
                              request=request)
