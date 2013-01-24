### This sample will show how to add collaborator to doc with annotations

# Import of classes from libraries
from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.AntApi import AntApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Set variables and get POST data
def sample13(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    fileGuId = request.POST.get('file_id')
    collaborations = request.params.getall('collaborations[]')

    # Delete empty items
    collaborations = filter(None, collaborations)

    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(fileGuId) == False or IsNotNull(collaborations) == False:
        return render_to_response('__main__:templates/sample13.pt',
                { 'error' : 'You do not enter all parameters' })

    #### Create Signer, ApiClient and Annotation Api objects

    # Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    # Create apiClient object
    apiClient = ApiClient(signer)
    # Create Annotation object
    ant = AntApi(apiClient)

    try:
        # Make a request to Annotation API
        ant.SetAnnotationCollaborators(clientId, fileGuId, "v2.0", body=collaborations)

    except Exception, e:
        return render_to_response('__main__:templates/sample13.pt',
                { 'error' : str(e) })

    # Construct all collaborations list
    collaborationsList = ""
    for x in xrange(len(collaborations)):
        collaborationsList += collaborations[x]
        if x != len(collaborations) - 1:
            collaborationsList += ", "

    # If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample13.pt',
            {
                'userId' : clientId,
                'privateKey' : privateKey,
                'fileId' : fileGuId,
                'collaborationsList' : collaborationsList
            },
        request=request)