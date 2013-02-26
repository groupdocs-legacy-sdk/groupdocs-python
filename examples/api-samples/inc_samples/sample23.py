### This sample will show how to View Document pages as images using Python SDK

# Import of classes from libraries
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.DocApi import DocApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Set variables and get POST data
def sample23(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    fileId = request.POST.get('fileId')
    basePath = request.POST.get('server_type')

    # Checking required parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(fileId) == False:
        return render_to_response('__main__:templates/sample23.pt',
            { 'error' : 'You do not enter all parameters' })

    ### Create Signer, ApiClient and Doc Api objects

    # Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    # Create apiClient object
    apiClient = ApiClient(signer)
    # Create DocApi object
    doc = DocApi(apiClient)
    # Set url to choose whot server to use
    doc.basePath = basePath

    # Make request yo the Api to get images for all document pages
    pageImage = doc.ViewDocument(clientId, fileId, pageNumber=0, pageCount=-1, width=100)

    # Check the result of the request
    if pageImage.status == "Ok":
        # Generation of iframe URL using pageImage.result.guid
        if basePath == "https://api.groupdocs.com/v2.0":
            iframe = '<iframe src="https://apps.groupdocs.com/document-viewer/embed/' + pageImage.result.guid + ' frameborder="0" width="720" height="600"><iframe>'
        elif basePath == "https://dev-api.groupdocs.com/v2.0":
            iframe = '<iframe src="https://dev-apps.groupdocs.com/document-viewer/embed/' + pageImage.result.guid + ' frameborder="0" width="720" height="600"><iframe>'
        elif basePath == "https://stage-api.groupdocs.com/v2.0":
            iframe = '<iframe src="https://stage-apps.groupdocs.com/document-viewer/embed/' + pageImage.result.guid + ' frameborder="0" width="720" height="600"><iframe>'


    # If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample23.pt',
        {
            'userId' : clientId,
            'privateKey' : privateKey,
            'fileId' : fileId,
            'iframe' : iframe
        },
        request=request)