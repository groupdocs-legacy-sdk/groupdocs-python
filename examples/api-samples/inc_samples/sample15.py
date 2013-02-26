### This sample will show how to check the number of document's views

# Import of classes from libraries
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.DocApi import DocApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Set variables and get POST data
def sample15(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')

    # Checking required parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample15.pt',
                { 'error' : 'You do not enter all parameters' })

    ### Create Signer, ApiClient, StorageApi and Document Api objects

    # Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    # Create apiClient object
    apiClient = ApiClient(signer)
    # Create DocApi object
    doc = DocApi(apiClient)

    # set total views
    views = 0

    try:
        # Make a request to Document API
        response = doc.GetDocumentViews(clientId)
        if response.status == "Ok":
            views = len(response.result.views)

    except Exception, e:
        return render_to_response('__main__:templates/sample15.pt',
                { 'error' : str(e) })

    # If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample15.pt',
            {
            'userId' : clientId,
            'privateKey' : privateKey,
            'views' : views,
        },
        request=request)