import base64

from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.MgmtApi import MgmtApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 7
def sample7(request):
    clientId = request.POST.get("client_id")
    privateKey = request.POST.get("private_key")
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample7.pt', 
                                  { 'error' : 'You do not enter you User id or Private key' })

    signer = GroupDocsRequestSigner(privateKey)
    apiClient = ApiClient(signer)
    mgmtApi = MgmtApi(apiClient)
    api = StorageApi(apiClient)
    try:
        files = api.ListEntities(clientId, "", extended = True); # geting all Entities from curent user
    except Exception, e:
        return render_to_response('__main__:templates/sample7.pt', 
                                  { 'error' : str(e) })

    thumbnail = '';
    name = '';
    for i in range(len(files.result.files)):
        if files.result.files[i].thumbnail != None:
            fp = open('examples/api-samples/templates/thumbnail' + str(i) + '.jpg', 'wb')
            fp.write(base64.b64decode(files.result.files[i].thumbnail))
            fp.close()
            name = files.result.files[i].name
            thumbnail += '<img src= "thumbnail' + str(i) + '.jpg", width="40px", height="40px">' + files.result.files[i].name + '</img> <br />'

    return render_to_response('__main__:templates/sample7.pt', 
                              { 'thumbnailList' : thumbnail, 'userId' : clientId, 'privateKey' : privateKey }, 
                              request=request)
