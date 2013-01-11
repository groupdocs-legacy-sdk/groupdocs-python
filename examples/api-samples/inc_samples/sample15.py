from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.DocApi import DocApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

# Sample 15
def sample15(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')

    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False:
        return render_to_response('__main__:templates/sample15.pt',
                { 'error' : 'You do not enter all parameters' })

    signer = GroupDocsRequestSigner(privateKey)
    apiClient = ApiClient(signer)
    doc = DocApi(apiClient)
    views = 0

    try:
        response = doc.GetDocumentViews(clientId)
        if response.status == "Ok":
            views = len(response.result.views)

    except Exception, e:
        return render_to_response('__main__:templates/sample15.pt',
                { 'error' : str(e) })

    return render_to_response('__main__:templates/sample15.pt',
            {
            'userId' : clientId,
            'privateKey' : privateKey,
            'views' : views,
        },
        request=request)