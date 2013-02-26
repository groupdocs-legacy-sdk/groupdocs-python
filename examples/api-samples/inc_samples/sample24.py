### This sample will show how to upload file from URL to GroupDocs account using Python SDK

# Import of classes from libraries
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.StorageApi import StorageApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Set variables and get POST data
def sample24(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    url = request.POST.get('url')

    # Checking required parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(url) == False:
        return render_to_response('__main__:templates/sample24.pt',
            { 'error' : 'You do not enter all parameters' })

    ### Create Signer, ApiClient and Storage Api objects

    # Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    # Create apiClient object
    apiClient = ApiClient(signer)
    # Create Storage Api object
    storage = StorageApi(apiClient)

    # Upload file to current user storage using entere URl to the file
    upload = storage.UploadWeb(clientId, url)
    # Check if file uploaded successfully
    if upload.status == "Ok":
        # Generation of Embeded Viewer URL with uploaded file GuId
        iframe = '<iframe src="https://apps.groupdocs.com/document-viewer/Embed/' + upload.result.guid + '" frameborder="0" width="720" height="600"></iframe>'


    # If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample24.pt',
        {
            'userId' : clientId,
            'privateKey' : privateKey,
            'url' : url,
            'iframe' : iframe,
        },
        request=request)