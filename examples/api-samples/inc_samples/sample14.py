### This sample will show how to check the list of shares for a folder

# Import of classes from libraries
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.DocApi import DocApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Set variables and get POST data
def sample14(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    path = request.POST.get('path')

    # Checking required parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(path) == False:
        return render_to_response('__main__:templates/sample14.pt',
                { 'error' : 'You do not enter all parameters' })

    ### Create Signer, ApiClient, StorageApi and Document Api objects

    # Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    # Create apiClient object
    apiClient = ApiClient(signer)
    # Create StorageApi object
    storageApi = StorageApi(apiClient)
    # Create DocApi object
    docApi = DocApi(apiClient)

    # initialization some variables
    folderId = None
    users = ""

    # parse input path
    pathList = path.split('/')
    if len(path) > 1:
        last = pathList[-1]
        del pathList[-1]
        newPath = "/".join(pathList)
    else:
        last = pathList.pop(0)
        newPath = ""

    try:
        #### Get folder ID by path

        # Make a request to Storage API
        list = storageApi.ListEntities(clientId, newPath)
        if list.status == "Ok":
            for folder in list.result.folders:
                if (folder.name == last):
                    folderId = folder.id

        ### Get list of shares
        if folderId is not None:
            # Make a request to Document API
            shares = docApi.GetFolderSharers(clientId, int(folderId))
            if shares.status == "Ok" and len(shares.result.shared_users) > 0:
                for x in xrange(len(shares.result.shared_users)):
                    # construct users list
                    users += str(shares.result.shared_users[x].nickname)
                    if x != len(shares.result.shared_users) - 1:
                        users += ", "

    except Exception, e:
        return render_to_response('__main__:templates/sample14.pt',
                { 'error' : str(e) })

    # If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample14.pt',
            {
            'userId' : clientId,
            'privateKey' : privateKey,
            'path' : path,
            'users' : users
        },
        request=request)