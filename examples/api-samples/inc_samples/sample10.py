import base64

from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.DocApi import DocApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 10
def sample10(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    fileGuId = request.POST.get('fileId')
    email = request.POST.get('email')

    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(fileGuId) == False or IsNotNull(email) == False:
        return render_to_response('__main__:templates/sample10.pt', 
                                  { 'error' : 'You do not enter all parameters' })

    signer = GroupDocsRequestSigner(privateKey)
    apiClient = ApiClient(signer)
    api = StorageApi(apiClient)

    try:
        files = api.ListEntities(userId = clientId, path = '', pageIndex = 0)
        name = ''
        for item in files.result.files: #selecting file names
           if item.guid == fileGuId:
               name = item.name
               fileGuId = item.id
        docApi = DocApi(apiClient)
        docApi.ShareDocument(clientId, fileGuId, body = [ email.encode(), ])
    except Exception, e:
        return render_to_response('__main__:templates/sample10.pt', 
                                  { 'error' : str(e) })

    print dir(shared_document_url)
    return render_to_response('__main__:templates/sample10.pt', 
                              { 'userId' : clientId, 
                               'privateKey' : privateKey, 
                               'fileId' : fileGuId, 
                               'email' : email }, 
                              request=request)
