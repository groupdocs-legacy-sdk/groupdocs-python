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
    basePath = request.POST.get('server_type')
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
    if basePath == "":
        basePath = 'https://api.groupdocs.com/v2.0'
    storage.basePath = basePath
    # Upload file to current user storage using entere URl to the file
    upload = storage.UploadWeb(clientId, url)
    # Check if file uploaded successfully
    if upload.status == "Ok":
        # Generation of Embeded Viewer URL with uploaded file GuId
    # Generation of iframe URL using pageImage.result.guid
        if basePath == "https://api.groupdocs.com/v2.0":
            iframe = 'https://apps.groupdocs.com/document-viewer/embed/' + upload.result.guid
        elif basePath == "https://dev-api.groupdocs.com/v2.0":
            iframe = 'https://dev-apps.groupdocs.com/document-viewer/embed/' + upload.result.guid
        elif basePath == "https://stage-api.groupdocs.com/v2.0":
            iframe = 'https://stage-apps.groupdocs.com/document-viewer/embed/' + upload.result.guid
        iframe = signer.signUrl(iframe)


    # If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample24.pt',
        {
            'userId' : clientId,
            'privateKey' : privateKey,
            'url' : url,
            'iframe' : iframe,
        },
        request=request)