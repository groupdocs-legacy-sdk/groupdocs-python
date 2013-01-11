from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.AntApi import AntApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 13
def sample13(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    fileGuId = request.POST.get('fileId')
    collaborations = request.params.getall('collaborations[]')

    # delete empty items
    collaborations = filter(None, collaborations)

    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(fileGuId) == False or IsNotNull(collaborations) == False:
        return render_to_response('__main__:templates/sample13.pt',
                { 'error' : 'You do not enter all parameters' })

    signer = GroupDocsRequestSigner(privateKey)
    apiClient = ApiClient(signer)
    ant = AntApi(apiClient)

    try:
        # set annotation collaborator
        ant.SetAnnotationCollaborators(clientId, fileGuId, "v2.0", body=collaborations)

    except Exception, e:
        return render_to_response('__main__:templates/sample13.pt',
                { 'error' : str(e) })

    # construct all collaborations list
    collaborationsList = ""
    for x in xrange(len(collaborations)):
        collaborationsList += collaborations[x]
        if x != len(collaborations) - 1:
            collaborationsList += ", "

    return render_to_response('__main__:templates/sample13.pt',
            {
                'userId' : clientId,
                'privateKey' : privateKey,
                'fileId' : fileGuId,
                'collaborationsList' : collaborationsList
            },
        request=request)