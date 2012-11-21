import base64

from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.DocApi import DocApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Sample 8
def sample8(request):
    clientId = request.POST.get('client_id');
    privateKey = request.POST.get('private_key');
    fileGuId = request.POST.get('fileId');
    pageNumber = request.POST.get('pageNumber') or 0
    if clientId == None or privateKey == None or fileGuId == None:
        return render_to_response('__main__:templates/sample8.pt', 
                                  { 'error' : 'You do not enter all parameters' })

    signer = GroupDocsRequestSigner(privateKey)
    apiClient = ApiClient(signer)
    docApi = DocApi(apiClient);
    try:
        url = docApi.GetDocumentPagesImageUrls(clientId, fileGuId, firstPage = int(pageNumber), pageCount = 1, dimension = '600x750')
    except Exception, e:
        return render_to_response('__main__:templates/sample8.pt', 
                                  { 'error' : str(e) })

    return render_to_response('__main__:templates/sample8.pt', 
                              { 'url' : url.result.url[0], 'userId' : clientId, 'privateKey' : privateKey, 'fileId' : fileGuId, 'pageNumber' : pageNumber }, 
                              request=request)
