from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.AntApi import AntApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 12
def sample12(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    fileGuId = request.POST.get('fileId')

    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(fileGuId) == False:
        return render_to_response('__main__:templates/sample12.pt',
                { 'error' : 'You do not enter all parameters' })

    signer = GroupDocsRequestSigner(privateKey)
    apiClient = ApiClient(signer)
    ant = AntApi(apiClient)

    try:
        response = ant.ListAnnotations(clientId, fileGuId)
    except Exception, e:
        return render_to_response('__main__:templates/sample12.pt',
                { 'error' : str(e) })

    return render_to_response('__main__:templates/sample12.pt',
            { 'userId' : clientId,
              'privateKey' : privateKey,
              'fileId' : fileGuId,
              'response' : response.result.annotations },
        request=request)