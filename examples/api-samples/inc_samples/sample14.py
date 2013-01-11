from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.DocApi import DocApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 14
def sample14(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    path = request.POST.get('path')

    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(path) == False:
        return render_to_response('__main__:templates/sample14.pt',
                { 'error' : 'You do not enter all parameters' })

    signer = GroupDocsRequestSigner(privateKey)
    apiClient = ApiClient(signer)
    storageApi = StorageApi(apiClient)
    docApi = DocApi(apiClient)

    folderId = None
    users = ""

    pathList = path.split('/')
    if len(path) > 1:
        last = pathList[-1]
        del pathList[-1]
        newPath = "/".join(pathList)
    else:
        last = pathList.pop(0)
        newPath = ""

    try:
        # get folder ID by path
        list = storageApi.ListEntities(clientId, newPath)
        if list.status == "Ok":
            for folder in list.result.folders:
                if (folder.name == last):
                    folderId = folder.id

        # get list of shares
        if folderId is not None:
            shares = docApi.GetFolderSharers(clientId, int(folderId))
            if shares.status == "Ok" and len(shares.result.shared_users) > 0:
                for x in xrange(len(shares.result.shared_users)):
                    users += str(shares.result.shared_users[x].nickname)
                    if x != len(shares.result.shared_users) - 1:
                        users += ", "

    except Exception, e:
        return render_to_response('__main__:templates/sample14.pt',
                { 'error' : str(e) })

    return render_to_response('__main__:templates/sample14.pt',
            {
            'userId' : clientId,
            'privateKey' : privateKey,
            'path' : path,
            'users' : users
        },
        request=request)