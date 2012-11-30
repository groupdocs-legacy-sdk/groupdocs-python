import base64

from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.DocApi import DocApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 5
def sample5(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    srcPath = request.POST.get('srcPath')
    destPath = request.POST.get('destPath')
    copy = request.POST.get('copy')
    move = request.POST.get('move')


    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(srcPath) == False or IsNotNull(destPath) == False:
        return render_to_response('__main__:templates/sample5.pt', 
                                  { 'error' : 'You do not enter all parameters' })

    signer = GroupDocsRequestSigner(privateKey)
    apiClient = ApiClient(signer)
    api = StorageApi(apiClient)

    try:
        docApi = DocApi(apiClient)
        srcFile = docApi.GetDocumentMetadataByPath(clientId, srcPath)
        
        fileName = srcFile.result.last_view.document.name
        fileID = int(srcFile.result.last_view.document.id)

        if copy:
           file = api.MoveFile(clientId, destPath, Groupdocs_Copy = fileID)

        if move:
           file = api.MoveFile(clientId, destPath, Groupdocs_Move = fileID)

    except Exception, e:
        return render_to_response('__main__:templates/sample5.pt', 
                                  { 'error' : str(e) })

    return render_to_response('__main__:templates/sample5.pt', 
                              { 'userId' : clientId, 
                               'privateKey' : privateKey, 
                               'destPath' : destPath, 
                               'srcPath' : srcPath }, 
                              request=request)
