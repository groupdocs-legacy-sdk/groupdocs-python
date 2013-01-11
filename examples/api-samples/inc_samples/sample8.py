####<i>This sample will show how to use <b>MoveFile</b> method from Storage Api to copy/move a file in GroupDocs Storage </i>

#Import of classes from libraries
import base64

from pyramid.renderers import render_to_response

from groupdocs.ApiClient import ApiClient
from groupdocs.DocApi import DocApi
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

####Set variables and get POST data
def sample8(request):
    clientId = request.POST.get('client_id')
    privateKey = request.POST.get('private_key')
    fileGuId = request.POST.get('fileId')
    pageNumber = request.POST.get('pageNumber') or 0
    #Checking parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(fileGuId) == False:
        return render_to_response('__main__:templates/sample8.pt', 
                                  { 'error' : 'You do not enter all parameters' })
    ####Create Signer, ApiClient and Storage Api objects

    #Create signer object
    signer = GroupDocsRequestSigner(privateKey)
    #Create apiClient object
    apiClient = ApiClient(signer)
    #Create DocApi object
    docApi = DocApi(apiClient)
    ####Make request to DocApi using user id


    try:
        #Obtaining URl of entered page
        url = docApi.GetDocumentPagesImageUrls(clientId, fileGuId, firstPage = int(pageNumber), pageCount = 1, dimension = '600x750')
    except Exception, e:
        return render_to_response('__main__:templates/sample8.pt', 
                                  { 'error' : str(e) })
    #If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample8.pt', 
                              { 
                               'url' : url.result.url[0], 
                               'userId' : clientId, 
                               'privateKey' : privateKey, 
                               'fileId' : fileGuId, 
                               'pageNumber' : pageNumber }, 
                              request=request)
