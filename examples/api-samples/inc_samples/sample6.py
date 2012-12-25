####<i>This sample will show how to use <b>MoveFile</b> method from Storage Api to copy/move a file in GroupDocs Storage </i>

#Import of classes from libraries
import base64
import json

from pyramid.renderers import render_to_response
from pyramid.response import Response

from groupdocs.ApiClient import ApiClient
from groupdocs.SignatureApi import SignatureApi
from groupdocs.models.SignatureSignDocumentSettings import SignatureSignDocumentSettings
from groupdocs.GroupDocsRequestSigner import GroupDocsRequestSigner

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

####Set variables and get POST data
def sample6(request):
    if request.content_type != 'application/json':
        return render_to_response('__main__:templates/sample6.pt', { })
    #Request to json
    jsonPostData = request.json_body
    #Get parameters
    clientId = jsonPostData.get("userId")
    privateKey = jsonPostData.get("privateKey")
    documents = jsonPostData.get('documents')
    signers = jsonPostData.get('signers')
    #Checking parameters
    if IsNotNull(clientId) == False or IsNotNull(privateKey) == False or IsNotNull(documents) == False or IsNotNull(signers) == False:
        return render_to_response('__main__:templates/sample6.pt', 
                                  { 'error' : 'You do not enter you User id or Private key' })
    #Determination of placeSingatureOn parameter
    for signer in signers:
        signer['placeSingatureOn'] = ''

    ####Create Signer, ApiClient and Storage Api objects

    #Create signer object
    signerReq = GroupDocsRequestSigner(privateKey)
    #Create apiClient object
    apiClient = ApiClient(signerReq)
    #Create Signsture API object
    signatureApi = SignatureApi(apiClient)
    #Create setting variable for signature SignDocument method
    settings = SignatureSignDocumentSettings()
    settings.documents = documents
    settings.signers = signers
####Make a request to Signature Api for sign document

#Sign document using current user id and sign settings
    response = signatureApi.SignDocument(clientId, body = settings)
    #If request was successfull - set variables for template
    if response.status == 'Ok':
        return_data = json.dumps({ 'responseCode' : 200, 'documentId' : response.result.documentId })
        return Response(body = return_data, content_type = 'application/json')
    
    return render_to_response('__main__:templates/sample6.pt', 
                          { 'error' : response.error_message })
